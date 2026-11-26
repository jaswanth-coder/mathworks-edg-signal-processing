# Digital Signal Processing (DSP) Core Mastery & Theory Guide
### Tailored for MathWorks EDG (Engineering Development Group) - Signal Processing Track

---

## 1. Signals, Systems & LTI Fundamentals

### 1.1 Discrete-Time Signals
* **Unit Impulse (Dirac / Kronecker Delta):**
  $$\delta[n] = \begin{cases} 1, & n = 0 \\ 0, & n \neq 0 \end{cases}$$
* **Unit Step:**
  $$u[n] = \begin{cases} 1, & n \ge 0 \\ 0, & n < 0 \end{cases}, \quad u[n] = \sum_{k=-\infty}^{n} \delta[k]$$
* **Complex Exponential:** $x[n] = e^{j\omega_0 n} = \cos(\omega_0 n) + j\sin(\omega_0 n)$
  * *Crucial Distinction from Continuous-Time:* Discrete complex exponentials with frequencies separated by $2\pi k$ are identical: $e^{j(\omega_0 + 2\pi)n} = e^{j\omega_0 n}$. The highest rate of oscillation occurs at $\omega = \pi$ (or $-\pi$), NOT as $\omega \to \infty$.

### 1.2 System Properties (Standard Interview Screening)
A system $\mathcal{T}\{\cdot\}$ maps an input sequence $x[n]$ to an output $y[n] = \mathcal{T}\{x[n]\}$.
1. **Linearity:**
   $$\mathcal{T}\{a x_1[n] + b x_2[n]\} = a\mathcal{T}\{x_1[n]\} + b\mathcal{T}\{x_2[n]\}$$
   *MathWorks Trap:* Check if there is an additive constant (e.g., $y[n] = 2x[n] + 3$ is **non-linear** because $x[n]=0 \implies y[n]=3 \neq 0$).
2. **Time-Invariance:**
   $$\text{If } \mathcal{T}\{x[n]\} = y[n], \text{ then } \mathcal{T}\{x[n - n_0]\} = y[n - n_0]$$
   *MathWorks Trap:* Time-varying coefficients (e.g., $y[n] = n x[n]$) or time-scaling (e.g., $y[n] = x[2n]$) make a system **Time-Varying**.
3. **Causality:**
   * Output $y[n_0]$ depends only on current and past inputs $x[n]$ for $n \le n_0$.
   * For an LTI system: Causality $\iff h[n] = 0$ for all $n < 0$.
4. **BIBO Stability (Bounded-Input Bounded-Output):**
   * If $|x[n]| \le B_x < \infty \implies |y[n]| \le B_y < \infty$.
   * **Necessary & Sufficient condition for LTI stability:** The impulse response must be absolutely summable:
     $$\sum_{n=-\infty}^{\infty} |h[n]| < \infty$$

### 1.3 Linear Convolution & LTI Response
Any LTI system is completely characterized by its impulse response $h[n] = \mathcal{T}\{\delta[n]\}$.
$$y[n] = x[n] * h[n] = \sum_{k=-\infty}^{\infty} x[k] h[n - k] = \sum_{k=-\infty}^{\infty} h[k] x[n - k]$$
* **Length Property:** If $x[n]$ has length $L_x$ and $h[n]$ has length $L_h$, the output $y[n]$ has length:
  $$L_y = L_x + L_h - 1$$
* **Commutative, Associative, and Distributive:**
  $$x * h = h * x, \quad x * (h_1 * h_2) = (x * h_1) * h_2, \quad x * (h_1 + h_2) = x * h_1 + x * h_2$$

---

## 2. Sampling Theorem, Aliasing & Reconstruction

### 2.1 The Nyquist-Shannon Sampling Theorem
To uniquely reconstruct a continuous-time bandlimited signal $x_a(t)$ with maximum frequency component $f_{\max}$ (or bandwidth $B = f_{\max}$):
$$f_s \ge 2 f_{\max} = f_{\text{Nyquist}}$$
* **Nyquist Rate:** $2 f_{\max}$ (minimum rate to avoid aliasing).
* **Nyquist Frequency (Folding Frequency):** $f_N = f_s / 2$.

### 2.2 Frequency Domain Interpretation & Aliasing
Sampling in time by period $T_s = 1/f_s$ causes periodic replication of the continuous spectrum $X_a(F)$ in the frequency domain with period $f_s$:
$$X_s(F) = \frac{1}{T_s} \sum_{k=-\infty}^{\infty} X_a\left(F - k f_s\right)$$
* If $f_s < 2 f_{\max}$, neighboring replicas overlap. High-frequency content "folds" back into the baseband $(0 \text{ to } f_s/2)$, permanently corrupting the signal.
* **Apparent Frequency Formula:**
  If a continuous tone of frequency $f_0$ is sampled at $f_s$, the observed discrete frequency alias is:
  $$f_{\text{alias}} = |f_0 - k f_s| \quad \text{such that } 0 \le f_{\text{alias}} \le \frac{f_s}{2}$$
  *Example (MathWorks classic):* $x(t) = \cos(2\pi \cdot 800 t)$ sampled at $f_s = 1000\text{ Hz}$.
  $f_{\text{alias}} = |800 - 1000| = 200\text{ Hz}$. The digitized signal is indistinguishable from a $200\text{ Hz}$ sine wave.

### 2.3 Anti-Aliasing Filter & Ideal Reconstruction
* **Anti-Aliasing Filter:** An analog low-pass filter (LPF) placed *before* the ADC with cutoff $f_c \le f_s/2$ to attenuate frequencies above the Nyquist limit.
* **Ideal Reconstruction (Whittaker-Shannon Interpolation):**
  $$x_a(t) = \sum_{n=-\infty}^{\infty} x[n] \cdot \operatorname{sinc}\left(\frac{t - n T_s}{T_s}\right), \quad \text{where } \operatorname{sinc}(u) = \frac{\sin(\pi u)}{\pi u}$$

---

## 3. Transforms: CTFT, DTFT, Z-Transform, DFT

### 3.1 Comparison of Four Fourier Representations
| Transform | Time Domain | Frequency Domain | Forward Transform |
| :--- | :--- | :--- | :--- |
| **CTFT** | Continuous, Aperiodic | Continuous, Aperiodic | $X(F) = \int_{-\infty}^{\infty} x(t) e^{-j 2\pi F t} dt$ |
| **CTFS** | Continuous, Periodic ($T$) | Discrete, Aperiodic | $c_k = \frac{1}{T}\int_T x(t) e^{-j k \frac{2\pi}{T} t} dt$ |
| **DTFT** | Discrete, Aperiodic | **Continuous, Periodic ($2\pi$)** | $X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n}$ |
| **DFT** | **Discrete, Finite ($N$)** | **Discrete, Finite ($N$)** | $X[k] = \sum_{n=0}^{N-1} x[n] e^{-j \frac{2\pi}{N} k n}$ |

### 3.2 Discrete-Time Fourier Transform (DTFT)
* **Properties:**
  * Periodic with period $2\pi$: $X(e^{j(\omega + 2\pi)}) = X(e^{j\omega})$.
  * If $x[n]$ is real: $|X(e^{j\omega})|$ is even, $\angle X(e^{j\omega})$ is odd (Conjugate Symmetry: $X(e^{-j\omega}) = X^*(e^{j\omega})$).
  * Convolution in time $\iff$ Multiplication in frequency:
    $$\mathcal{DTFT}\{x[n] * h[n]\} = X(e^{j\omega}) \cdot H(e^{j\omega})$$

### 3.3 The Z-Transform & Region of Convergence (ROC)
The Z-transform generalizes DTFT by introducing a complex variable $z = r e^{j\omega}$:
$$X(z) = \sum_{n=-\infty}^{\infty} x[n] z^{-n}$$
* **DTFT is the Z-Transform evaluated on the unit circle:** $X(e^{j\omega}) = X(z)\Big|_{z = e^{j\omega}}$ (valid only if the unit circle $|z|=1$ lies within the ROC).
* **ROC Rules (Crucial for stability & causality checks):**
  1. ROC is a ring or disk centered at the origin in the $z$-plane.
  2. ROC cannot contain any poles.
  3. **Causal signal:** ROC extends outward from the outermost pole to $\infty$: $|z| > r_{\max}$.
  4. **Anti-causal signal:** ROC extends inward from innermost pole to $0$: $|z| < r_{\min}$.
  5. **Two-sided signal:** ROC is an annular ring $r_1 < |z| < r_2$.
  6. **BIBO Stability:** The LTI system is BIBO stable if and only if the **ROC includes the unit circle $|z| = 1$**.
     * Hence, a **causal LTI system** is stable $\iff$ **all poles strictly lie inside the unit circle** ($|p_i| < 1$).

### 3.4 Discrete Fourier Transform (DFT)
Sampling the continuous DTFT $X(e^{j\omega})$ at $N$ equally spaced frequencies $\omega_k = \frac{2\pi k}{N}$ ($k = 0, 1, \dots, N-1$):
$$X[k] = \sum_{n=0}^{N-1} x[n] W_N^{kn}, \quad x[n] = \frac{1}{N} \sum_{k=0}^{N-1} X[k] W_N^{-kn}$$
where $W_N = e^{-j\frac{2\pi}{N}}$ is the twiddle factor.
* **Frequency Resolution:**
  $$\Delta f = \frac{f_s}{N} = \frac{1}{N T_s} = \frac{1}{T_{\text{record}}}$$
* **Zero-Padding vs Increasing Record Length:**
  * *Zero-padding ($N_{\text{padded}} > N$):* Does NOT increase true physical resolution; it interpolates the DTFT spectrum (spectral interpolation) and gives smoother visual curves.
  * *Increasing physical duration ($T_{\text{record}} = N \cdot T_s$):* Increases true frequency resolution, allowing two closely spaced sinusoids to be resolved.
* **Circular Convolution Property:**
  $$X_1[k] \cdot X_2[k] \stackrel{\mathcal{DFT}_N}{\longleftrightarrow} x_1[n] \circledast_N x_2[n] = \sum_{m=0}^{N-1} x_1[m] x_2[(n - m) \bmod N]$$
  * **To perform linear convolution of length $L_1$ and $L_2$ via DFT/FFT:**
    You must zero-pad both sequences to at least:
    $$N \ge L_1 + L_2 - 1$$
    before computing FFT, multiplying point-by-point, and computing IFFT. Otherwise, **time-domain aliasing (wrap-around)** occurs!

---

## 4. Fast Fourier Transform (FFT) Algorithms

### 4.1 Radix-2 Cooley-Tukey Algorithm
Direct DFT requires $N^2$ complex multiplications and $N(N-1)$ complex additions.
The Cooley-Tukey algorithm breaks down an $N$-point DFT (where $N = 2^M$) into two $N/2$-point DFTs using divide-and-conquer.

#### Decimation-in-Time (DIT-FFT):
Split $x[n]$ into even-indexed and odd-indexed samples:
$$X[k] = \sum_{m=0}^{N/2 - 1} x[2m] W_N^{2mk} + \sum_{m=0}^{N/2 - 1} x[2m+1] W_N^{(2m+1)k}$$
Using $W_N^{2mk} = W_{N/2}^{mk}$:
$$X[k] = E[k] + W_N^k O[k]$$
Using symmetry property $W_N^{k + N/2} = -W_N^k$:
$$\begin{aligned}
X[k] &= E[k] + W_N^k O[k], \quad &k = 0, 1, \dots, \frac{N}{2}-1 \\
X\left[k + \frac{N}{2}\right] &= E[k] - W_N^k O[k], \quad &k = 0, 1, \dots, \frac{N}{2}-1
\end{aligned}$$
This fundamental computation is the **Butterfly Operation**:
* 1 complex multiplication ($W_N^k O[k]$).
* 2 complex additions/subtractions.

```
       E[k] ----------------+------------> X[k] = E[k] + W_N^k * O[k]
                             \          /
                              \   -1   /
                               \  /   /
       O[k] ----( * W_N^k )-----+----+---> X[k + N/2] = E[k] - W_N^k * O[k]
```

### 4.2 Computational Complexity Comparison
| Operation | Direct DFT | Radix-2 FFT | Speedup ($N=1024$) |
| :--- | :--- | :--- | :--- |
| Complex Multiplications | $N^2$ | $\frac{N}{2} \log_2 N$ | $\frac{1024^2}{512 \times 10} \approx 205\times$ |
| Complex Additions | $N(N-1)$ | $N \log_2 N$ | $\approx 100\times$ |

### 4.3 Bit-Reversal Permutation
In Radix-2 DIT-FFT, if the output spectrum is in natural order, the input samples must be loaded in **bit-reversed order**:
* Index $3$ for $N=8$: Binary `011` $\to$ Reversal `110` = Index $6$.
* Index $1$ for $N=8$: Binary `001` $\to$ Reversal `100` = Index $4$.

---

## 5. Digital Filter Design: FIR vs. IIR

### 5.1 Comprehensive Tradeoff Matrix
| Feature | FIR (Finite Impulse Response) | IIR (Infinite Impulse Response) |
| :--- | :--- | :--- |
| **Impulse Response** | Finite length $M+1$ | Infinite duration (exponential tail) |
| **Difference Equation** | $y[n] = \sum_{k=0}^{M} b_k x[n-k]$ (All-zero) | $y[n] = \sum_{k=0}^{M} b_k x[n-k] - \sum_{k=1}^{N} a_k y[n-k]$ (Poles + Zeros) |
| **Stability** | **Always unconditionally stable** (all poles at $z=0$) | Conditional: Stable $\iff$ all poles inside unit circle |
| **Phase Response** | **Can guarantee exact linear phase** (no phase distortion) | Non-linear phase (requires allpass phase equalizers) |
| **Filter Order** | High order for sharp cutoff transitions | **Much lower order** (typically 5x to 10x fewer taps than FIR) |
| **Computational Cost** | High memory & computation for steep skirts | Low memory & computation |
| **Sensitivity to Quantization** | Low sensitivity (robust to coefficient truncation) | High sensitivity (pole locations near unit circle may drift outside $\implies$ instability/limit cycles) |

### 5.2 FIR Filter Design & Linear Phase Types
For linear phase, the impulse response must exhibit symmetry: $h[n] = \pm h[M - n]$.
* **Constant Group Delay:** $\tau_g = -\frac{d\phi(\omega)}{d\omega} = \frac{M}{2}$ samples (constant delay for all frequencies).
* **Four Types of Linear Phase FIR Filters:**
  1. **Type I:** Symmetric ($h[n] = h[M-n]$), $M$ is **Even** (odd length $N = M+1$). Can design: LPF, HPF, BPF, BSF.
  2. **Type II:** Symmetric ($h[n] = h[M-n]$), $M$ is **Odd** (even length $N$). Zero at $\omega = \pi$. **Cannot design Highpass or Bandstop filters!**
  3. **Type III:** Antisymmetric ($h[n] = -h[M-n]$), $M$ is **Even**. Zeros at $\omega = 0$ and $\omega = \pi$. Suitable for Differentiators & Hilbert transformers. **Cannot design Lowpass or Highpass!**
  4. **Type IV:** Antisymmetric ($h[n] = -h[M-n]$), $M$ is **Odd**. Zero at $\omega = 0$. Suitable for Differentiators and Highpass.

#### FIR Design Methods:
1. **Windowing Method:**
   Multiply ideal infinite impulse response $h_d[n] = \frac{\sin(\omega_c (n - M/2))}{\pi (n - M/2)}$ by a finite window $w[n]$:
   $$h[n] = h_d[n] \cdot w[n]$$
   * **Gibbs Phenomenon:** Truncation with a Rectangular window causes an unavoidable $\approx 9\%$ overshoot ($-21\text{ dB}$ stopband attenuation) near band discontinuities, regardless of how large $M$ is.
   * **Window Tradeoffs:**
     * *Rectangular:* Mainlobe width $\frac{4\pi}{M}$, peak sidelobe $-13\text{ dB}$ (poor attenuation).
     * *Hanning:* Mainlobe $\frac{8\pi}{M}$, peak sidelobe $-31\text{ dB}$.
     * *Hamming:* Mainlobe $\frac{8\pi}{M}$, peak sidelobe $-41\text{ dB}$, stopband attenuation $\sim 53\text{ dB}$.
     * *Blackman:* Mainlobe $\frac{12\pi}{M}$, peak sidelobe $-58\text{ dB}$, stopband attenuation $\sim 74\text{ dB}$.
     * *Kaiser Window:* Parameter $\beta$ allows continuous tradeoff between mainlobe width and stopband ripple.
2. **Parks-McClellan (Remez Exchange) Algorithm:**
   * Formulates filter design as a Chebyshev approximation problem.
   * Produces **equiripple** error in passband and stopband.
   * Optimal in the minimax sense (minimizes the maximum peak approximation error for a given order).

### 5.3 IIR Filter Design: Bilinear Transformation (BLT)
Map analog transfer function $H_a(s)$ to discrete transfer function $H(z)$ via the trapezoidal numerical integration conformal mapping:
$$s = \frac{2}{T_s} \frac{1 - z^{-1}}{1 + z^{-1}}$$
* **Properties of BLT:**
  * Maps entire imaginary axis $s = j\Omega$ in $s$-plane monotonically onto the unit circle $z = e^{j\omega}$ in $z$-plane.
  * Maps Left Half of $s$-plane ($\operatorname{Re}\{s\} < 0$) strictly inside unit circle ($|z| < 1$).
  * **Completely eliminates aliasing**, unlike the Impulse Invariance method!
* **Frequency Warping:**
  $$\omega = 2 \arctan\left(\frac{\Omega T_s}{2}\right) \iff \Omega = \frac{2}{T_s} \tan\left(\frac{\omega}{2}\right)$$
* **Pre-Warping Step:** To place cutoff frequency exactly at desired digital frequency $\omega_c$, pre-warp analog prototype cutoff:
  $$\Omega_c = \frac{2}{T_s} \tan\left(\frac{\omega_c}{2}\right)$$

---

## 6. Filter Realization Structures

### 6.1 Direct Form I vs. Direct Form II
Consider general IIR filter:
$$y[n] = \sum_{k=0}^{M} b_k x[n-k] - \sum_{k=1}^{N} a_k y[n-k]$$

* **Direct Form I:**
  * Implements zeros first, then poles.
  * Requires $M + N$ delay registers ($z^{-1}$).
* **Direct Form II (Canonical):**
  * Implements poles first, then zeros:
    $$w[n] = x[n] - \sum_{k=1}^N a_k w[n-k], \quad y[n] = \sum_{k=0}^M b_k w[n-k]$$
  * Requires only $\max(M, N)$ delay registers. **Canonical in delay elements.**
  * *Disadvantage:* Internal node $w[n]$ is susceptible to overflow in fixed-point implementations.

```
Direct Form II (Canonical):
             x[n] --->(+)--------------------------->(+)---> y[n]
                       ^                              ^
                       |     +------------------+     |
                       |     |     w[n-1]       |     |
                       |--(-a1)---[ z^-1 ]---(b1)-----+
                       |     |                  |     |
                       |     |     w[n-2]       |     |
                       +--(-a2)---[ z^-1 ]---(b2)-----+
```

### 6.2 Direct Form II Transposed (MATLAB Default `filter`)
Obtained by applying the Transposition (Tellegen's) Theorem:
1. Reverse direction of all signal paths.
2. Replace branch points with sum nodes, and sum nodes with branch points.
3. Swap input and output.
* **Why MathWorks uses DF-II Transposed for `filter.m`:**
  * Canonical with $\max(M, N)$ delays.
  * Numerator and denominator operations are interleaved: products are accumulated directly into delay registers before storage, drastically minimizing roundoff noise and eliminating fixed-point internal node overflow!

### 6.3 Cascade (Biquad / Second-Order Sections - SOS)
High-order direct form filters are notoriously unstable due to **pole sensitivity**: a tiny perturbation in polynomial coefficients $\{a_k\}$ moves high-order clustered poles outside the unit circle!
* **Solution:** Factor transfer function into a product of second-order sections (biquads):
  $$H(z) = b_0 \prod_{k=1}^{K} \frac{1 + \beta_{1k} z^{-1} + \beta_{2k} z^{-2}}{1 + \alpha_{1k} z^{-1} + \alpha_{2k} z^{-2}}$$
* Always pair poles with their nearest zeros and order sections from lowest Q (broadest resonance) to highest Q to avoid dynamic range clipping.

---

## 7. Multirate DSP: Decimation, Interpolation & Polyphase

### 7.1 Downsampling (Decimation by $M$)
1. **Anti-Aliasing Filter:** Digital LPF with cutoff $\omega_c = \frac{\pi}{M}$.
2. **Downsampler:** Discard $M-1$ of every $M$ samples:
   $$y[m] = x[m M]$$
   Spectrum expands: $Y(e^{j\omega}) = \frac{1}{M} \sum_{k=0}^{M-1} X\left(e^{j\frac{\omega - 2\pi k}{M}}\right)$.

### 7.2 Upsampling (Interpolation by $L$)
1. **Zero-Inserter (Expander):** Insert $L-1$ zeros between original samples:
   $$x_e[n] = \begin{cases} x[n/L], & n = 0, \pm L, \pm 2L, \dots \\ 0, & \text{otherwise} \end{cases}$$
   Spectrum compresses: $X_e(e^{j\omega}) = X(e^{j\omega L})$ (creates $L-1$ spectral images).
2. **Anti-Imaging Filter:** Digital LPF with cutoff $\omega_c = \frac{\pi}{L}$ and gain $L$ to remove replicas and interpolate values.

### 7.3 Polyphase Decomposition & Noble Identities
* **Noble Identity for Decimation:** Filtering by $H(z^M)$ followed by downsampler $M$ is equivalent to downsampling by $M$ followed by filtering by $H(z)$.
* **Polyphase Efficiency:** Instead of filtering at high sample rate $f_s$ and discarding $(M-1)/M$ computed samples, split $H(z)$ into $M$ polyphase branches:
  $$H(z) = \sum_{k=0}^{M-1} z^{-k} E_k(z^M)$$
  Computations run at the **decimated low sampling rate $f_s/M$**, yielding an **$M$-fold reduction** in operations per second!

---

## 8. Random Signals, Correlation & Spectral Estimation

### 8.1 Autocorrelation & Cross-Correlation
* **Deterministic Sequences:**
  $$r_{xx}[k] = \sum_{n=-\infty}^{\infty} x[n] x^*[n-k] = x[k] * x^*[-k]$$
* **Stationary Random Process:**
  $$\gamma_{xx}[k] = E\{X[n] X^*[n-k]\}$$
* **Properties:**
  * Maximum at origin: $|r_{xx}[k]| \le r_{xx}[0] = \text{Energy (or Average Power)}$.
  * Conjugate symmetric: $r_{xx}[-k] = r_{xx}^*[k]$.

### 8.2 Power Spectral Density (PSD) & Wiener-Khinchin Theorem
The Power Spectral Density $S_{xx}(e^{j\omega})$ is the DTFT of the autocorrelation sequence:
$$S_{xx}(e^{j\omega}) = \sum_{k=-\infty}^{\infty} \gamma_{xx}[k] e^{-j\omega k}$$
* $S_{xx}(e^{j\omega}) \ge 0$ for all $\omega$ (always real and non-negative).
* For an LTI system with input $x[n]$ and output $y[n]$:
  $$S_{yy}(e^{j\omega}) = |H(e^{j\omega})|^2 S_{xx}(e^{j\omega})$$

### 8.3 Non-Parametric Spectral Estimation
* **Periodogram:** $\hat{P}_{per}(\omega) = \frac{1}{N} \left|\sum_{n=0}^{N-1} x[n] e^{-j\omega n}\right|^2$.
  * *Fatal flaw:* Asymptotically unbiased, but **inconsistent estimator** (variance does NOT decrease to zero as $N \to \infty$; variance $\approx P^2(\omega)$).
* **Welch’s Method (Industry Standard - `pwelch` in MATLAB):**
  1. Divide $N$ samples into $K$ overlapping segments (typically 50% overlap) of length $L$.
  2. Window each segment (Hamming/Hann) to minimize spectral leakage.
  3. Compute modified periodogram for each segment.
  4. Average all $K$ periodograms.
  * **Result:** Reduces variance by a factor of $\approx K$, trading off a small amount of frequency resolution for a dramatically cleaner spectrum estimate.
