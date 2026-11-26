#!/usr/bin/env python3
"""
update_modules_15_16.py
Upgrades Modules 15 (MATLAB DSP Mastery) and 16 (C Systems & DSA) with:
- Ascending levels of complexity (from basic primitives to production book-level)
- Exact algorithms and idioms from Proakis & Ingle and Sanjit K. Mitra
- Detailed breakdown of what EACH sub-part of the code does
- KaTeX-formatted math and clean syntax-highlighted code blocks
"""

mod15_html = r"""<!-- MODULE 15 -->
<details class="module-card" open id="_mod15_matlab_toolbox">
  <summary class="module-summary">
    <div><span class="module-badge">MATLAB Mastery</span> Module 15: MATLAB Signal Processing Toolbox & Algorithmic Implementations (Ascending Levels)</div>
    <span style="font-size: 14px; color: #64748b;">▼</span>
  </summary>
  <div class="module-body">
    <p>This module presents core MATLAB signal processing implementations structured in <strong>ascending order of algorithmic complexity</strong>, synthesizing practical patterns from <em>Vinay K. Ingle & John G. Proakis (Digital Signal Processing using MATLAB)</em> and <em>Sanjit K. Mitra (Digital Signal Processing: A Computer-Based Approach)</em>. Every code listing is dissected to explain what each sub-part accomplishes under the hood.</p>

    <!-- ======================================================== -->
    <!-- LEVEL 1: SEQUENCE ARITHMETIC & PRECISION AXES            -->
    <!-- ======================================================== -->
    <h3>Level 1: Precision Time/Frequency Axes & Convolution with Arbitrary Index Support</h3>
    <p>In continuous math, signals are defined on $t \in (-\infty, \infty)$. In MATLAB, signals are discrete vectors starting at index 1. A classic pitfall in MathWorks interviews is failing to track the time origin when signals have negative or offset indices.</p>

    <div class="example-box">
      <div class="example-title">📖 Proakis & Ingle Algorithm 2.1: Modified Convolution (conv_m) with True Support Tracking</div>
      <p>MATLAB’s built-in <code>conv(x, h)</code> computes the raw product samples but provides <em>no timing information</em>. If $x[n]$ starts at $n_{x1}$ and $h[n]$ starts at $n_{h1}$, the convolution result $y[n]$ starts at $n_{y1} = n_{x1} + n_{h1}$ and ends at $n_{y2} = n_{x2} + n_{h2}$.</p>
      
      <pre><code>function [y, ny] = conv_m(x, nx, h, nh)
% Modified linear convolution with exact support tracking
% [y, ny] = conv_m(x, nx, h, nh)
% ------------------------------------------------------
% Part A: Compute the beginning and ending indices of the output
nyb = nx(1) + nh(1);                  % First non-zero index of output
nye = nx(end) + nh(end);              % Last non-zero index of output
ny  = nyb : nye;                      % Complete discrete time axis for y[n]

% Part B: Compute analytical convolution sum
y   = conv(x, h);                     % Vectorized linear convolution
end</code></pre>

      <table class="tableblock">
        <thead>
          <tr>
            <th>Code Sub-Part</th>
            <th>MATLAB Operation</th>
            <th>Mathematical & Algorithmic Explanation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>nyb = nx(1) + nh(1)</code></td>
            <td>Lower Index Bound</td>
            <td>The earliest non-zero sample in convolution $x[k]h[n-k]$ occurs when the leading edges of both sequences overlap at $n = n_{x1} + n_{h1}$.</td>
          </tr>
          <tr>
            <td><code>nye = nx(end) + nh(end)</code></td>
            <td>Upper Index Bound</td>
            <td>The trailing edge overlaps until $n = n_{x2} + n_{h2}$. Total length is automatically $L_y = L_x + L_h - 1$.</td>
          </tr>
          <tr>
            <td><code>y = conv(x, h)</code></td>
            <td>Polynomial Multiplication</td>
            <td>Executes fast linear convolution using contiguous memory arrays in $O(N_1 N_2)$ time.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- ======================================================== -->
    <!-- LEVEL 2: DIFFERENCE EQUATION & INITIAL CONDITIONS        -->
    <!-- ======================================================== -->
    <h3>Level 2: Difference Equation Simulation with Non-Zero Initial Conditions (filtic & filter)</h3>
    <p>Most candidates know <code>y = filter(b, a, x)</code> for zero initial conditions ($y[-1] = y[-2] = 0$). However, MathWorks interviewers routinely test handling of <strong>historical state memory</strong> (transient response due to non-zero past inputs and outputs).</p>

    <div class="example-box">
      <div class="example-title">📖 Proakis & Ingle Section 2.4: Total Response = Zero-Input + Zero-State Response</div>
      <p>Simulate $y[n] - 0.75 y[n-1] + 0.125 y[n-2] = x[n] + 0.5 x[n-1]$ given past states $y[-1] = 1, y[-2] = 2$ and past inputs $x[-1] = 1$.</p>
      
      <pre><code>% Coefficients of Difference Equation
b = [1,  0.5];                        % Numerator coefficients (Feedforward)
a = [1, -0.75, 0.125];                % Denominator coefficients (Feedback)

% Historical conditions: past outputs Y0 = [y(-1), y(-2)], past inputs X0 = [x(-1)]
Y0 = [1, 2];
X0 = [1];

% Part A: Convert historical states to Direct Form II Transposed delay states
z0 = filtic(b, a, Y0, X0);

% Part B: Excite system with input signal x[n] for n = 0:10
n = 0:10;
x = (0.5).^n;

% Part C: Filter signal incorporating initial state vector z0
[y, zf] = filter(b, a, x, z0);</code></pre>

      <table class="tableblock">
        <thead>
          <tr>
            <th>Code Sub-Part</th>
            <th>MATLAB Function</th>
            <th>Under-The-Hood Mechanics</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>filtic(b, a, Y0, X0)</code></td>
            <td>State Vector Translation</td>
            <td>Translates past scalar values into the initial register contents $z_0$ of the Direct Form II Transposed structure so that delay lines begin with exact energy levels.</td>
          </tr>
          <tr>
            <td><code>filter(b, a, x, z0)</code></td>
            <td>DF-II-T Iteration</td>
            <td>Computes the total solution: $y[n] = y_{\text{zi}}[n] + y_{\text{zs}}[n]$ (Zero-Input natural response + Zero-State forced response).</td>
          </tr>
          <tr>
            <td><code>zf</code></td>
            <td>Final Delay States</td>
            <td>Preserves the internal delay registers at sample $n=10$. This allows <strong>streaming continuous audio</strong> by passing <code>zf</code> as <code>z0</code> into the next frame!</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- ======================================================== -->
    <!-- LEVEL 3: HIGH-SPEED BLOCK FFT CONVOLUTION (OVERLAP-ADD) -->
    <!-- ======================================================== -->
    <h3>Level 3: Block Convolution for Long Sequences: Overlap-Add (OLA) Method</h3>
    <p>When filtering a massive streaming signal (e.g., 1 hour of audio with millions of samples) with an FIR filter of length $M$, computing global convolution requires prohibitive memory and introduces massive latency. The <strong>Overlap-Add (OLA)</strong> method divides $x[n]$ into small blocks of length $L$, computes fast FFT-based circular convolution of length $N = L + M - 1$, and adds the overlapping tails.</p>

    <div class="flow-diagram-container">
      <div class="flow-diagram-title">🔄 Overlap-Add (OLA) Block Convolution Architecture (Proakis & Ingle Fig 5.16)</div>
      <div class="svg-diagram-card">
        <svg width="640" height="130" viewBox="0 0 640 130" xmlns="http://www.w3.org/2000/svg">
          <!-- Blocks -->
          <rect x="20" y="30" width="100" height="40" rx="4" fill="#f8fafc" stroke="#2c3e50" stroke-width="1.5"/>
          <text x="70" y="55" font-size="11" text-anchor="middle" font-weight="bold">Block xm[n]</text>
          <text x="70" y="67" font-size="9" fill="#64748b" text-anchor="middle">Length L</text>

          <line x1="120" y1="50" x2="160" y2="50" stroke="#2c3e50" stroke-width="1.5"/>

          <rect x="160" y="25" width="120" height="50" rx="4" fill="#f8fafc" stroke="#0284c7" stroke-width="1.5"/>
          <text x="220" y="47" font-size="11" text-anchor="middle" font-weight="bold">Zero-Pad to N</text>
          <text x="220" y="62" font-size="10" fill="#0284c7" text-anchor="middle">N = L + M - 1</text>

          <line x1="280" y1="50" x2="320" y2="50" stroke="#2c3e50" stroke-width="1.5"/>

          <rect x="320" y="25" width="130" height="50" rx="4" fill="#f8fafc" stroke="#ba3925" stroke-width="1.5"/>
          <text x="385" y="47" font-size="11" text-anchor="middle" font-weight="bold">IFFT( FFT·FFT )</text>
          <text x="385" y="62" font-size="10" fill="#ba3925" text-anchor="middle">Fast Convolution</text>

          <line x1="450" y1="50" x2="490" y2="50" stroke="#2c3e50" stroke-width="1.5"/>

          <rect x="490" y="30" width="130" height="40" rx="4" fill="#f8fafc" stroke="#16a34a" stroke-width="1.5"/>
          <text x="555" y="50" font-size="11" text-anchor="middle" font-weight="bold">Overlap-Add Tails</text>
          <text x="555" y="64" font-size="9" fill="#16a34a" text-anchor="middle">(M-1) Overlap</text>
        </svg>
        <div class="svg-diagram-caption">Figure 15.1: The Overlap-Add algorithm. Each block of length L is padded with M-1 zeros. The resulting output blocks overlap by M-1 samples and are summed together.</div>
      </div>
    </div>

    <div class="example-box">
      <div class="example-title">📖 Proakis & Ingle Function ovrlpadd.m: Exact Book Implementation</div>
      <pre><code>function [y] = ovrlpadd(x, h, N)
% Overlap-Add block convolution method using FFT
% [y] = ovrlpadd(x, h, N)
% ---------------------------------------------
% Part A: Compute block lengths and pre-calculate Filter FFT
M = length(h);                        % Filter length
L = N - M + 1;                        % Non-zero block length (L < N)
H = fft(h, N);                        % N-point FFT of impulse response (precomputed)

% Part B: Frame partitioning and zero preallocation
Nx = length(x);
K  = ceil(Nx / L);                    % Total number of input blocks
x_padded = [x, zeros(1, K*L - Nx)];   % Zero-pad input to exact multiple of L
y  = zeros(1, K*L + M - 1);           % Preallocate final output array

% Part C: Iterative Block-by-Block Processing
for k = 0 : K-1
    % 1. Extract k-th block of length L
    xk = x_padded(k*L + 1 : (k+1)*L);
    
    % 2. Zero-pad block to length N and compute N-point circular convolution via FFT
    Xk = fft(xk, N);
    Yk = Xk .* H;
    yk = real(ifft(Yk));              % Linear convolution of block with filter
    
    % 3. Overlap-add the result into output vector
    start_idx = k*L + 1;
    stop_idx  = start_idx + N - 1;
    y(start_idx : stop_idx) = y(start_idx : stop_idx) + yk;
end
end</code></pre>

      <table class="tableblock">
        <thead>
          <tr>
            <th>Algorithm Sub-Part</th>
            <th>Role in Overlap-Add</th>
            <th>Why it is Mathematically Required</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>N = L + M - 1</code></td>
            <td>FFT Size</td>
            <td>To avoid <strong>time-domain circular wrap-around aliasing</strong>, the FFT length $N$ must equal or exceed the linear convolution length $L + M - 1$.</td>
          </tr>
          <tr>
            <td><code>H = fft(h, N)</code></td>
            <td>Offline Precomputation</td>
            <td>Filter coefficients do not change during streaming. Precomputing $H[k]$ saves $K-1$ FFT transforms.</td>
          </tr>
          <tr>
            <td><code>y(...) = y(...) + yk</code></td>
            <td>Accumulating Overlap</td>
            <td>The trailing $M-1$ samples of block $k$ coincide in time with the leading $M-1$ samples of block $k+1$. Adding them reconstructs linear convolution identically.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- ======================================================== -->
    <!-- LEVEL 4: CASCADE SOS FORM CONVERSIONS                    -->
    <!-- ======================================================== -->
    <h3>Level 4: High-Order IIR Design & Second-Order Sections (SOS) Conversion</h3>
    <p>In textbook theory, filters are represented as rational transfer functions $H(z) = \frac{\sum b_k z^{-k}}{1 + \sum a_k z^{-k}}$. However, in real MATLAB software engineering, high-order polynomial representations suffer from catastrophic <strong>coefficient quantization sensitivity</strong>: roots of polynomials are hypersensitive to tiny numerical perturbations.</p>

    <div class="example-box">
      <div class="example-title">📖 Sanjit K. Mitra Lab 7: tf2sos and sosfilt vs. Direct Form filter</div>
      <pre><code>% 1. Design an 8th-order Elliptic Lowpass Filter
[b, a] = ellip(8, 0.5, 60, 0.3);      % High-order direct form coefficients

% 2. Convert direct form [b, a] to Second-Order Sections (SOS) matrix
[sos, g] = tf2sos(b, a);              % sos is an 4x6 matrix of biquad sections

% 3. Filter signal using Cascade Biquads
fs = 1000; t = 0:1/fs:1-1/fs;
x = sin(2*pi*50*t) + randn(size(t));

% BAD (Sensitive to coefficient truncation):
y_direct = filter(b, a, x);

% GOOD (Numerically stable biquad cascade):
y_sos = sosfilt(sos, x) * g;</code></pre>

      <div class="admonitionblock tip">
        <table>
          <tr>
            <td class="icon"><div class="title">Tip</div></td>
            <td class="content">
              <strong>Why MathWorks Recommends <code>sosfilt</code>:</strong> <code>tf2sos</code> pairs complex conjugate poles with their nearest zeros and orders sections in increasing resonance (Q-factor). This distributes gain evenly across sections and prevents arithmetic clipping in fixed-point and floating-point registers.
            </td>
          </tr>
        </table>
      </div>
    </div>

    <!-- ======================================================== -->
    <!-- LEVEL 5: SPECTRAL ESTIMATION & PEAK DETECTION            -->
    <!-- ======================================================== -->
    <h3>Level 5: Spectral Analysis (Welch's Method) & In-Place Peak Detection</h3>
    <div class="example-box">
      <div class="example-title">📖 Sanjit K. Mitra Lab 11: Welch's Averaged Periodogram (pwelch)</div>
      <pre><code>% Synthetic noisy multi-tone signal
fs = 1000;
t  = 0:1/fs:2-1/fs;
x  = 2*sin(2*pi*70*t) + 1.5*cos(2*pi*150*t) + 1.2*randn(size(t));

% Welch's Method Parameters
win      = hamming(256);             % 256-sample Hamming window (attenuates sidelobes)
noverlap = 128;                      % 50% overlap (conserves data variance)
nfft     = 512;                      % 512-point FFT (interpolates frequency bins)

% Part A: Compute Power Spectral Density (PSD)
[Pxx, f] = pwelch(x, win, noverlap, nfft, fs);

% Part B: Peak Detection to Extract Exact Tone Frequencies
[pks, locs] = findpeaks(10*log10(Pxx), f, ...
    'MinPeakHeight', -10, ...        % Must exceed -10 dB/Hz
    'MinPeakDistance', 20);          % Minimum 20 Hz separation between tones</code></pre>
    </div>
  </div>
</details>
"""

mod16_html = r"""<!-- MODULE 16 -->
<details class="module-card" id="_mod16_c_dsp_dsa">
  <summary class="module-summary">
    <div><span class="module-badge">C Systems & DSA</span> Module 16: C Memory Architecture, Circular Buffers & LeetCode DSA (Ascending Levels)</div>
    <span style="font-size: 14px; color: #64748b;">▼</span>
  </summary>
  <div class="module-body">
    <p>This module provides low-level C programming architectures and data structures tailored specifically for the <strong>MathWorks EDG Signal Processing track</strong>, progressing in <strong>ascending levels of complexity</strong> from foundational memory and pointer semantics to book-level embedded filter engines and LeetCode algorithmic rounds.</p>

    <!-- ======================================================== -->
    <!-- LEVEL 1: POINTERS & BIT MANIPULATION                    -->
    <!-- ======================================================== -->
    <h3>Level 1: Memory Alignment, Pointer Safety & Bitwise Primitives</h3>
    <p>MathWorks code generation engines (MATLAB Coder) interface directly with compiled C code. Interviewers thoroughly test pointer arithmetic, buffer boundary enforcement, and low-level bit operations.</p>

    <div class="example-box">
      <div class="example-title">💻 Level 1 C Primitives: Fast Bit Manipulation for DSP Systems</div>
      <pre><code>#include &lt;stdio.h&gt;
#include &lt;stdbool.h&gt;
#include &lt;stdint.h&gt;

// Sub-part 1: Check if buffer size is Power of 2 (Crucial for Radix-2 FFT and Ring Buffers)
bool is_power_of_two(uint32_t n) {
    // If n is power of 2, binary representation has exactly one set bit (e.g., 0b1000).
    // Subtracting 1 flips all lower bits (0b0111). Bitwise AND yields zero.
    return (n > 0) && ((n & (n - 1)) == 0);
}

// Sub-part 2: Bit-Reversal for Radix-2 DIT-FFT index unscrambling
uint32_t reverse_bits(uint32_t index, uint32_t num_bits) {
    uint32_t rev = 0;
    for (uint32_t i = 0; i < num_bits; ++i) {
        if (index & (1U << i)) {
            rev |= (1U << (num_bits - 1 - i));
        }
    }
    return rev;
}

// Sub-part 3: CPU Endianness Check using Byte Pointers
bool is_little_endian(void) {
    uint16_t test_val = 0x0001;
    uint8_t *byte_ptr = (uint8_t *)&test_val;
    // In Little-Endian, Least Significant Byte (0x01) is stored at lowest address.
    return (*byte_ptr == 0x01);
}</code></pre>
    </div>

    <!-- ======================================================== -->
    <!-- LEVEL 2: LINEAR CONVOLUTION WITH BOUNDARY SAFETY         -->
    <!-- ======================================================== -->
    <h3>Level 2: 1D Linear Convolution with Strict Heap & Boundary Safety</h3>
    <p>A classic live-coding problem at MathWorks: implement $y[n] = \sum x[k] h[n-k]$ in C without out-of-bounds pointer reads or heap corruption.</p>

    <div class="example-box">
      <div class="example-title">💻 Level 2 C Algorithm: Safe 1D Linear Convolution</div>
      <pre><code>#include &lt;stdlib.h&gt;

float* convolve_1d_safe(const float *x, size_t len_x, const float *h, size_t len_h, size_t *out_len) {
    // Sub-part A: Input validation and null check
    if (!x || !h || len_x == 0 || len_h == 0) {
        *out_len = 0;
        return NULL;
    }

    // Sub-part B: Output allocation with exact size Ly = Lx + Lh - 1
    *out_len = len_x + len_h - 1;
    float *y = (float *)calloc(*out_len, sizeof(float));
    if (!y) return NULL; // Always check for allocation failure!

    // Sub-part C: Bounded convolution sum loops
    for (size_t n = 0; n < *out_len; ++n) {
        double acc = 0.0; // Double accumulator prevents intermediate float precision loss
        
        // Compute active overlapping index limits
        size_t k_min = (n >= len_h - 1) ? n - (len_h - 1) : 0;
        size_t k_max = (n < len_x - 1)   ? n : len_x - 1;

        for (size_t k = k_min; k <= k_max; ++k) {
            acc += (double)x[k] * (double)h[n - k];
        }
        y[n] = (float)acc;
    }
    return y;
}</code></pre>

      <table class="tableblock">
        <thead>
          <tr>
            <th>Sub-Part</th>
            <th>Safety Mechanism</th>
            <th>Interview Screening Point</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>calloc(*out_len, ...)</code></td>
            <td>Contiguous Zero Initialization</td>
            <td>Prevents reading uninitialized heap memory.</td>
          </tr>
          <tr>
            <td><code>k_min & k_max</code></td>
            <td>Clamped Loop Limits</td>
            <td>Ensures $k \in [0, \text{len\_x}-1]$ and $n-k \in [0, \text{len\_h}-1]$ simultaneously. <strong>Completely prevents buffer overflow segmentation faults!</strong></td>
          </tr>
          <tr>
            <td><code>double acc</code></td>
            <td>High-Precision Accumulator</td>
            <td>Prevents round-off truncation when accumulating thousands of product terms.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- ======================================================== -->
    <!-- LEVEL 3: ZERO-COPY CIRCULAR BUFFER                      -->
    <!-- ======================================================== -->
    <h3>Level 3: Zero-Copy Circular Ring Buffer for O(1) Streaming DSP</h3>
    <p>Real-time audio, radar, and sensor buffers cannot afford $O(N)$ memory copying every time a sample arrives. A circular buffer achieves $O(1)$ sample insertion and retrieval using wrap-around pointer arithmetic.</p>

    <div class="flow-diagram-container">
      <div class="flow-diagram-title">🔄 Circular Buffer Memory Architecture & Head Pointer Wrap-Around</div>
      <div class="svg-diagram-card">
        <svg width="550" height="110" viewBox="0 0 550 110" xmlns="http://www.w3.org/2000/svg">
          <g transform="translate(60, 30)">
            <rect x="0" y="0" width="45" height="45" fill="#f8fafc" stroke="#2c3e50" rx="3"/>
            <text x="22" y="27" font-size="11" text-anchor="middle">s[0]</text>
            <rect x="55" y="0" width="45" height="45" fill="#f8fafc" stroke="#2c3e50" rx="3"/>
            <text x="77" y="27" font-size="11" text-anchor="middle">s[1]</text>
            <rect x="110" y="0" width="45" height="45" fill="#f8fafc" stroke="#2c3e50" rx="3"/>
            <text x="132" y="27" font-size="11" text-anchor="middle">s[2]</text>
            <rect x="165" y="0" width="45" height="45" fill="#fed7aa" stroke="#c2410c" stroke-width="2" rx="3"/>
            <text x="187" y="27" font-size="11" font-weight="bold" fill="#c2410c" text-anchor="middle">head</text>
            <rect x="220" y="0" width="45" height="45" fill="#f8fafc" stroke="#2c3e50" rx="3"/>
            <text x="242" y="27" font-size="11" text-anchor="middle">s[4]</text>
            <rect x="275" y="0" width="45" height="45" fill="#f8fafc" stroke="#2c3e50" rx="3"/>
            <text x="297" y="27" font-size="11" text-anchor="middle">s[5]</text>
            <rect x="330" y="0" width="45" height="45" fill="#f8fafc" stroke="#2c3e50" rx="3"/>
            <text x="352" y="27" font-size="11" text-anchor="middle">s[6]</text>
            <rect x="385" y="0" width="45" height="45" fill="#f8fafc" stroke="#2c3e50" rx="3"/>
            <text x="407" y="27" font-size="11" text-anchor="middle">s[7]</text>
          </g>
          <text x="275" y="98" font-size="11" fill="#64748b" text-anchor="middle">Next write: head = (head + 1) & (capacity - 1) for power-of-2 capacity</text>
        </svg>
        <div class="svg-diagram-caption">Figure 16.1: Zero-copy ring buffer. New incoming sample overwrites the oldest sample in-place without memory movement.</div>
      </div>
    </div>

    <div class="example-box">
      <div class="example-title">💻 Level 3 C Algorithm: O(1) Sliding Moving-Average Filter Engine</div>
      <pre><code>#include &lt;stdlib.h&gt;

typedef struct {
    float *buffer;           // Contiguous circular sample array
    size_t capacity;         // Fixed window length (preferably power of 2)
    size_t head;             // Index of next incoming write slot
    size_t count;            // Valid samples currently stored
    double running_sum;      // Persistent running sum of current window
} StreamingMovAvg;

StreamingMovAvg* movavg_create(size_t window_size) {
    StreamingMovAvg *f = (StreamingMovAvg *)malloc(sizeof(StreamingMovAvg));
    if (!f) return NULL;
    f->buffer = (float *)calloc(window_size, sizeof(float));
    if (!f->buffer) { free(f); return NULL; }
    f->capacity = window_size;
    f->head = 0;
    f->count = 0;
    f->running_sum = 0.0;
    return f;
}

// O(1) Update executed inside high-speed audio interrupt
float movavg_update(StreamingMovAvg *f, float new_sample) {
    // Sub-part 1: Subtract oldest sample currently at head position
    f->running_sum -= f->buffer[f->head];

    // Sub-part 2: Overwrite slot with newest incoming sample
    f->buffer[f->head] = new_sample;
    f->running_sum += new_sample;

    // Sub-part 3: Advance circular pointer with bitwise mask or modulo
    f->head = (f->head + 1) % f->capacity;
    if (f->count < f->capacity) {
        f->count++;
    }

    // Sub-part 4: Return current moving average
    return (float)(f->running_sum / f->count);
}

void movavg_free(StreamingMovAvg *f) {
    if (f) {
        free(f->buffer);
        free(f);
    }
}</code></pre>
    </div>

    <!-- ======================================================== -->
    <!-- LEVEL 4: PRODUCTION DF-II-T BIQUAD & Q15 SATURATION     -->
    <!-- ======================================================== -->
    <h3>Level 4: Direct Form II Transposed Biquad & Fixed-Point Q15 Saturation</h3>
    <p>In embedded DSP chips without floating-point units (FPUs), filter math is executed in 16-bit integer fixed-point (Q15 format: 1 sign bit, 15 fractional bits). Standard Two's complement addition wraps around upon overflow, causing catastrophic audio clipping distortion (full rail-to-rail square waves). Saturation arithmetic clamps the accumulator to $+32767$ or $-32768$.</p>

    <div class="example-box">
      <div class="example-title">💻 Level 4 C Implementation: Saturating Math & Persistent Biquad Filter</div>
      <pre><code>#include &lt;stdint.h&gt;

// Q15 fixed-point format: Range [-1.0, 0.999969]
typedef int16_t q15_t;

// Sub-part A: Saturating 16-bit addition
static inline q15_t q15_add_sat(q15_t a, q15_t b) {
    int32_t sum = (int32_t)a + (int32_t)b;
    if (sum > 32767)  return 32767;
    if (sum < -32768) return -32768;
    return (q15_t)sum;
}

// Sub-part B: Saturating 16-bit multiplication (Q15 * Q15 = Q30 -> shifted to Q15)
static inline q15_t q15_mul_sat(q15_t a, q15_t b) {
    int32_t prod = ((int32_t)a * (int32_t)b) >> 15;
    if (prod > 32767)  return 32767;
    if (prod < -32768) return -32768;
    return (q15_t)prod;
}

// Sub-part C: Persistent Direct Form II Transposed Biquad Filter Struct
typedef struct {
    float b0, b1, b2;        // Numerator coefficients
    float a1, a2;            // Denominator coefficients (a0 normalized to 1.0)
    float s1, s2;            // Delay state registers
} BiquadDF2T;

void biquad_init(BiquadDF2T *f, float b0, float b1, float b2, float a1, float a2) {
    f->b0 = b0; f->b1 = b1; f->b2 = b2;
    f->a1 = a1; f->a2 = a2;
    f->s1 = 0.0f; f->s2 = 0.0f;
}

// Sub-part D: Single-Sample Processing Step
float biquad_process_sample(BiquadDF2T *f, float x) {
    // Output equation: y[n] = b0 * x[n] + s1[n-1]
    float y = f->b0 * x + f->s1;

    // State update 1: s1[n] = b1 * x[n] - a1 * y[n] + s2[n-1]
    f->s1 = f->b1 * x - f->a1 * y + f->s2;

    // State update 2: s2[n] = b2 * x[n] - a2 * y[n]
    f->s2 = f->b2 * x - f->a2 * y;

    return y;
}</code></pre>

      <table class="tableblock">
        <thead>
          <tr>
            <th>Sub-Part</th>
            <th>Operation</th>
            <th>Significance in Embedded DSP</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code>int32_t sum = (int32_t)a + b</code></td>
            <td>32-bit Headroom</td>
            <td>Computes sum in wider 32-bit register to catch overflow before clamping.</td>
          </tr>
          <tr>
            <td><code>prod >> 15</code></td>
            <td>Fractional Alignment</td>
            <td>Multiplying two 15-bit fractional numbers produces 30 fractional bits. Shifting right by 15 restores proper Q15 scaling.</td>
          </tr>
          <tr>
            <td><code>f->s1 & f->s2</code></td>
            <td>State Persistence</td>
            <td>Enables true streaming audio across frame boundaries without phase clicks.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- ======================================================== -->
    <!-- LEVEL 5: LEETCODE / MATHWORKS INTERVIEW DSA             -->
    <!-- ======================================================== -->
    <h3>Level 5: High-Frequency MathWorks Technical Interview DSA Problems</h3>

    <div class="example-box">
      <div class="example-title">💻 Problem 1: In-Place 90° Clockwise Matrix Rotation (LeetCode 48)</div>
      <p>Given an $N \times N$ 2D matrix representing an image or filter kernel, rotate it 90 degrees clockwise in-place with $O(1)$ extra memory.</p>
      <pre><code>void rotate_matrix_90_clockwise(int n, int matrix[n][n]) {
    // Step 1: Transpose matrix along the main diagonal
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            int temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }

    // Step 2: Reverse each row horizontally (two-pointer swap)
    for (int i = 0; i < n; ++i) {
        int left = 0, right = n - 1;
        while (left < right) {
            int temp = matrix[i][left];
            matrix[i][left] = matrix[i][right];
            matrix[i][right] = temp;
            left++;
            right--;
        }
    }
}</code></pre>
    </div>

    <div class="example-box">
      <div class="example-title">💻 Problem 2: Find Peak Element in O(log N) Time (LeetCode 162)</div>
      <p>A peak element is an element strictly greater than its neighbors. Given array <code>nums</code> where <code>nums[i] != nums[i+1]</code>, find any peak index in $O(\log N)$ time.</p>
      <pre><code>int findPeakElement(int* nums, int numsSize) {
    int left = 0, right = numsSize - 1;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] > nums[mid + 1]) {
            // Downward slope: a peak must exist to the left (including mid)
            right = mid;
        } else {
            // Upward slope: a peak must exist to the right
            left = mid + 1;
        }
    }
    return left; // left == right points to a local peak!
}</code></pre>
    </div>
  </div>
</details>
"""

# Read index.html
with open('/home/jaswanth/mathworks_intrevPrep/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# Replace Module 15
mod15_pattern = re.compile(r'(<!-- MODULE 15 -->\s*).*?(?=<!-- MODULE 16 -->)', re.DOTALL)
content = mod15_pattern.sub(lambda m: m.group(1) + mod15_html + '\n\n', content)

# Replace Module 16
mod16_pattern = re.compile(r'(<!-- MODULE 16 -->\s*).*?(?=<!-- MODULE 17 -->)', re.DOTALL)
content = mod16_pattern.sub(lambda m: m.group(1) + mod16_html + '\n\n', content)

with open('/home/jaswanth/mathworks_intrevPrep/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Modules 15 and 16 updated in index.html with ascending levels and sub-part explanations!")
