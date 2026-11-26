# MATLAB Signal Processing Toolbox & Algorithms Cheatsheet

---

## 1. Quick Syntax & Essential Commands

| Category | Command | Description & Syntax |
| :--- | :--- | :--- |
| **Transforms** | `fft(x, N)` | $N$-point Discrete Fourier Transform |
| | `ifft(X, N)` | Inverse $N$-point DFT |
| | `fftshift(X)` | Shifts zero-frequency component to center of spectrum |
| | `ifftshift(X)` | Inverse zero-frequency shift |
| **Filtering** | `filter(b, a, x)` | Direct Form II Transposed IIR/FIR filter ($a_0 = 1$) |
| | `filtfilt(b, a, x)` | Zero-phase forward-backward filtering |
| | `fftfilt(b, x, N)` | Overlap-add FFT-based FIR filtering for long signals |
| | `conv(u, v)` | Convolution of two 1D vectors |
| | `deconv(w, v)` | Deconvolution and polynomial division |
| **Filter Analysis**| `freqz(b, a, N, fs)`| Frequency response of digital filter |
| | `zplane(b, a)` | Pole-zero plot in complex $z$-plane |
| | `grpdelay(b, a)` | Group delay of filter |
| | `impz(b, a, N)` | Impulse response of digital filter |
| **Filter Design** | `fir1(n, Wn, win)` | Window-based FIR filter design ($W_n \in [0, 1]$ where $1 = f_s/2$) |
| | `firpm(n, f, a)` | Parks-McClellan equiripple optimal FIR design |
| | `butter(n, Wn)` | Butterworth IIR filter (maximally flat passband) |
| | `cheby1(n, Rp, Wn)`| Chebyshev Type I IIR (equiripple passband) |
| | `cheby2(n, Rs, Wn)`| Chebyshev Type II IIR (equiripple stopband) |
| | `ellip(n, Rp, Rs, Wn)`| Elliptic IIR filter (equiripple in both pass & stopband) |
| | `designfilt(...)` | Modern object-oriented filter designer |
| **Signal Ops** | `findpeaks(x, ...)` | Local maxima / peak detection with thresholds |
| | `resample(x, p, q)` | Resamples by rational factor $p/q$ using polyphase FIR |
| | `decimate(x, r)` | Lowpass filter followed by downsampling by $r$ |
| | `interp(x, r)` | Upsampling by $r$ followed by anti-imaging interpolation |
| | `xcorr(x, y)` | Cross-correlation of sequences |
| | `xcov(x, y)` | Cross-covariance (mean subtracted) |
| | `pwelch(x, win, nov, nfft, fs)` | Welch's power spectral density estimate |

---

## 2. High-Frequency Interview MATLAB Snippets

### 2.1 Fast In-Place Sliding Moving Average
```matlab
% Compute N-point moving average using cumulative sum (O(1) per element!)
function y = fast_moving_avg(x, N)
    cs = cumsum([0, x]);
    y = (cs(N+1:end) - cs(1:end-N)) / N;
end
```

### 2.2 Numerical Integration (Trapezoidal Rule)
MathWorks interviewers often ask candidates to implement `trapz` from scratch:
```matlab
function integral_val = my_trapz(x, y)
    % y is f(x). Assumes non-uniform or uniform spacing in x.
    dx = diff(x);
    mid_y = (y(1:end-1) + y(2:end)) / 2;
    integral_val = sum(dx .* mid_y);
end
```

### 2.3 90-Degree Matrix Rotation Without Built-in `rot90`
```matlab
function M_rot = my_rot90_clockwise(M)
    % Clockwise rotation: Transpose, then flip left-to-right
    M_rot = fliplr(M.');
end

function M_rot = my_rot90_counter_clockwise(M)
    % Counter-clockwise rotation: Transpose, then flip up-to-down
    M_rot = flipud(M.');
end
```
