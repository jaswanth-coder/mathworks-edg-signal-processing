# MATLAB Signal Processing Mastery & Algorithmic Implementation Guide
### Tailored for MathWorks EDG (Signal Processing Track)

---

## 1. MATLAB Idioms & Core Execution Model

### 1.1 Vectorization vs Loops (The #1 MathWorks Standard)
MathWorks interviewers pay extreme attention to vectorization, memory preallocation, and matrix efficiency.
* **Never grow arrays in a loop:**
  ```matlab
  % BAD (O(N^2) memory reallocation every iteration)
  y = [];
  for k = 1:N
      y(k) = k^2;
  end

  % GOOD (O(N) with contiguous block preallocation)
  y = zeros(1, N);
  for k = 1:N
      y(k) = k^2;
  end

  % BEST (Vectorized single instruction)
  k = 1:N;
  y = k.^2;
  ```

### 1.2 Matrix Storage & Memory Layout
* MATLAB stores 2D arrays in **Column-Major order** (Fortran convention), unlike C which is Row-Major!
* Accessing elements column-by-column ($A(i, j)$ where inner loop varies $i$) is dramatically faster than row-by-row due to CPU L1/L2 cache locality.

### 1.3 Logical Indexing & Thresholding
```matlab
% Given noisy signal x, clamp all negative values to zero without loops:
x(x < 0) = 0;

% Find indices where signal exceeds 3*sigma:
sigma = std(x);
outlier_indices = find(abs(x - mean(x)) > 3 * sigma);
```

---

## 2. Signal Generation & Frequency Scaling

### 2.1 The Golden Pattern for Time & Frequency Axes
```matlab
fs = 1000;              % Sampling frequency (Hz)
Ts = 1 / fs;            % Sampling period (seconds)
T  = 2.0;               % Duration (seconds)
t  = 0:Ts:(T - Ts);     % Time vector (exact length N = fs * T)
N  = length(t);

% Synthetic multi-tone signal with noise
f1 = 50;  f2 = 120;
x = 2.0 * sin(2*pi*f1*t) + 1.5 * cos(2*pi*f2*t) + 0.5 * randn(size(t));

% FFT and Frequency Axis Setup:
X = fft(x);

% 1. Two-sided unshifted spectrum (0 to fs - fs/N):
f_onesided = (0:N-1) * (fs / N);

% 2. Two-sided centered spectrum (-fs/2 to fs/2 - fs/N):
X_centered = fftshift(X);
f_centered = (-N/2 : N/2 - 1) * (fs / N);   % For even N

% 3. Single-sided amplitude spectrum:
P2 = abs(X / N);
P1 = P2(1:N/2+1);
P1(2:end-1) = 2 * P1(2:end-1);              % Conserve total energy
f_ss = (0:(N/2)) * (fs / N);
```

---

## 3. Signal Processing Toolbox Core Functions & Workflows

### 3.1 Peak Detection (`findpeaks`)
Crucial MathWorks interview topic!
```matlab
% Syntax:
[pks, locs, w, p] = findpeaks(data, ...
    'MinPeakHeight', 0.5, ...       % Minimum amplitude
    'MinPeakDistance', 20, ...      % Minimum sample separation (avoids noise clustering)
    'MinPeakProminence', 0.8, ...   % Prominence relative to neighboring valleys
    'Threshold', 0.1);              % Difference from adjacent neighbors
```

### 3.2 Filtering: `filter` vs `filtfilt` vs `fftfilt`
| Command | Filter Type | Phase Distortion | Causality | Application |
| :--- | :--- | :--- | :--- | :--- |
| `filter(b, a, x)` | IIR / FIR | Non-linear (IIR), delay $M/2$ (FIR) | **Causal** (Real-time stream) | Real-time processing, DSP chips |
| `filtfilt(b, a, x)` | IIR / FIR | **Zero-phase** ($\phi(\omega) \equiv 0$) | **Non-causal** (Needs full signal) | Offline biomedical, audio post |
| `fftfilt(b, x)` | FIR only | Linear phase | Uses Overlap-Add FFT | Long signals or high-order FIR |

#### How `filtfilt` works under the hood:
1. Filters signal in forward direction: $y_1[n] = x[n] * h[n]$.
2. Reverses $y_1[n]$ in time: $y_1^R[n] = y_1[-n]$.
3. Filters reversed signal: $y_2[n] = y_1^R[n] * h[n]$.
4. Reverses back: $y[n] = y_2[-n]$.
* Resulting transfer function: $H_{\text{total}}(e^{j\omega}) = H(e^{j\omega}) \cdot H^*(e^{j\omega}) = |H(e^{j\omega})|^2$.
* Phase response is identically **zero**; filter attenuation is **doubled** in dB!

### 3.3 Modern Filter Design: `designfilt` vs Classic Functions
```matlab
% Modern Object-Oriented Design (Recommended by MathWorks):
d = designfilt('lowpassiir', ...
    'PassbandFrequency', 150, ...
    'StopbandFrequency', 200, ...
    'PassbandRipple', 1, ...         % dB
    'StopbandAttenuation', 60, ...   % dB
    'SampleRate', 1000);

y = filter(d, x);
fvtool(d);   % Interactive Filter Visualization Tool

% Classic Filter Design (Classic interview questions):
% 1. Butterworth IIR:
[b_iir, a_iir] = butter(4, 0.4, 'low');   % Order 4, Wn = 0.4*(fs/2)

% 2. Parks-McClellan Optimal Equiripple FIR:
f = [0 0.3 0.4 1];          % Normalized frequency bands [0, 1]
a = [1 1 0 0];              % Desired amplitude
b_pm = firpm(30, f, a);     % Order 30 FIR

% 3. Window-based FIR:
b_win = fir1(48, 0.35, hamming(49));
```

### 3.4 Spectral Estimation: `periodogram` vs `pwelch`
```matlab
% Welch's Overlapped Segment Averaging:
window = hann(256);
noverlap = 128;      % 50% overlap
nfft = 512;
[Pxx, f] = pwelch(x, window, noverlap, nfft, fs);

plot(f, 10*log10(Pxx));
xlabel('Frequency (Hz)'); ylabel('Power/Frequency (dB/Hz)');
grid on;
```

---

## 4. DSP System Toolbox & Streaming Architecture

### 4.1 System Objects (`dsp.*`)
System Objects are specialized C++ backed MATLAB objects optimized for iterative/streaming execution:
* Fast state management (no manual pointer book-keeping).
* Support variable frame size.
* Optimized for code generation (C/C++ via MATLAB Coder).

```matlab
% Audio streaming simulation using System Objects
fileReader = dsp.AudioFileReader('speech_dft.wav');
spectrumAnalyzer = dsp.SpectrumAnalyzer('SampleRate', fileReader.SampleRate);
firFilter = dsp.FIRFilter('Numerator', fir1(32, 0.3));

while ~isDone(fileReader)
    audioFrame = fileReader();              % Read frame of samples
    filteredFrame = firFilter(audioFrame);  % Process frame (internal state preserved)
    spectrumAnalyzer(filteredFrame);        % Visualize frame
end

release(fileReader);
release(firFilter);
release(spectrumAnalyzer);
```

### 4.2 MATLAB Coder Readiness (`%#codegen`)
When MathWorks engineers write DSP algorithms intended for C/C++ generation:
1. Add `%#codegen` pragma at top of file.
2. Preallocate all variables with explicit size and type.
3. Avoid dynamic resizing and recursion.
```matlab
function y = apply_fir(b, x) %#codegen
    % Preallocate output with fixed type and size
    Nx = length(x);
    Nb = length(b);
    y = zeros(1, Nx, 'like', x);
    
    % Direct Form I FIR Implementation
    for n = 1:Nx
        acc = 0;
        for k = 1:Nb
            if (n - k + 1) >= 1
                acc = acc + b(k) * x(n - k + 1);
            end
        end
        y(n) = acc;
    end
end
```
