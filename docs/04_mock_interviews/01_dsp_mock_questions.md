# MathWorks EDG Mock Interview Questions & Model Answers: Digital Signal Processing (DSP)

---

### Question 1: Sampling & Aliasing in Multi-Tone Signals
**Interviewer:**  
"Suppose we have a continuous-time signal:
$$x_a(t) = 3\cos(600\pi t) + 2\cos(1800\pi t) + \sin(3000\pi t)$$
1. What is the minimum Nyquist sampling rate $f_s$ required to avoid aliasing?
2. If this signal is sampled at $f_s = 1200\text{ samples/sec}$, what discrete frequency components will appear in the discrete-time signal $x[n]$ within the principal frequency range $[0, f_s/2]$?"

#### Model Answer:
**Part 1: Nyquist Rate**
* Let's convert radian frequencies $\Omega$ to cyclic frequencies $f$ in Hz:
  * Tone 1: $\Omega_1 = 600\pi \implies f_1 = \frac{600\pi}{2\pi} = 300\text{ Hz}$.
  * Tone 2: $\Omega_2 = 1800\pi \implies f_2 = \frac{1800\pi}{2\pi} = 900\text{ Hz}$.
  * Tone 3: $\Omega_3 = 3000\pi \implies f_3 = \frac{3000\pi}{2\pi} = 1500\text{ Hz}$.
* Maximum frequency component $f_{\max} = 1500\text{ Hz}$.
* Therefore, the Nyquist sampling rate is:
  $$f_{\text{Nyquist}} = 2 \cdot f_{\max} = 2 \times 1500 = 3000\text{ Hz (or samples/sec)}$$

**Part 2: Sampling at $f_s = 1200\text{ Hz}$**
* Nyquist folding frequency $f_N = f_s / 2 = 600\text{ Hz}$.
* Let's calculate the apparent alias frequency $f_{\text{alias}} = |f - k f_s|$ inside $[0, 600]\text{ Hz}$ for each tone:
  * **Tone 1 ($300\text{ Hz}$):** $300\text{ Hz} \le 600\text{ Hz}$, no aliasing. Appears as **$300\text{ Hz}$** ($\omega_1 = 2\pi \frac{300}{1200} = 0.5\pi\text{ rad/sample}$).
  * **Tone 2 ($900\text{ Hz}$):** Aliased! $k=1 \implies |900 - 1200| = 300\text{ Hz}$. Folds back on top of Tone 1 at **$300\text{ Hz}$**!
  * **Tone 3 ($1500\text{ Hz}$):** Aliased! $k=1 \implies |1500 - 1200| = 300\text{ Hz}$.
* **Crucial Insight:** All three tones fold onto the exact same frequency of **$300\text{ Hz}$**, resulting in constructive/destructive interference and total loss of original signal integrity.

---

### Question 2: FIR vs. IIR Filter Selection & Linear Phase
**Interviewer:**  
"In a biomedical ECG monitoring application or high-speed telecommunications receiver, why is linear phase strictly preferred over non-linear phase? When would you choose an IIR filter instead of FIR, and what are the trade-offs?"

#### Model Answer:
* **Why Linear Phase is Critical:**
  * Linear phase $\phi(\omega) = -\alpha \omega$ means that the **group delay** $\tau_g = -\frac{d\phi}{d\omega} = \alpha$ is constant across all frequencies.
  * Every frequency component in the signal is delayed by the exact same amount of time.
  * If group delay is frequency-dependent (as in IIR filters), different frequency components arrive at different times (**dispersion**). In an ECG signal, this distorts the QRS-complex and ST-segment, leading to false medical diagnoses; in digital communications, it causes severe **Inter-Symbol Interference (ISI)**.
* **When to choose IIR:**
  * When sharp frequency transitions (steep cutoff skirts) are required under severe computation or memory constraints (e.g., low-power battery-operated DSPs or microcontrollers).
  * An IIR filter can meet the same magnitude specifications with a filter order that is 5 to 10 times lower than an equivalent FIR filter.
  * If phase linearity is required offline (not real-time streaming), we can use IIR with `filtfilt` in MATLAB (zero-phase forward-backward filtering).
* **Summary Trade-Off Table:**
  * FIR: Always stable, linear phase achievable, higher order, higher latency/computation.
  * IIR: Lower order, low latency, non-linear phase, conditionally stable (must monitor pole locations).

---

### Question 3: FFT vs. DFT Complexity & Twiddle Factor Symmetry
**Interviewer:**  
"Explain how the Cooley-Tukey Radix-2 FFT reduces the computational complexity from $O(N^2)$ to $O(N \log N)$. Which mathematical properties of the twiddle factor $W_N$ make this possible?"

#### Model Answer:
* **Properties of the Twiddle Factor $W_N = e^{-j 2\pi / N}$:**
  1. **Periodicity:** $W_N^{k + N} = W_N^k$
  2. **Symmetry (Half-period inversion):** $W_N^{k + N/2} = -W_N^k$
  3. **Index Squaring (Scale reduction):** $W_N^{2k} = W_{N/2}^k$
* **Mechanism:**
  * By splitting an $N$-point DFT into two $N/2$-point DFTs (even-indexed samples $E[k]$ and odd-indexed samples $O[k]$):
    $$X[k] = E[k] + W_N^k O[k]$$
    $$X[k + N/2] = E[k] - W_N^k O[k]$$
  * The term $W_N^k O[k]$ is computed **once** and reused for both $X[k]$ and $X[k + N/2]$. This eliminates half the multiplications in each stage.
  * Recursing this divide-and-conquer strategy gives $\log_2 N$ stages. Each stage performs $N/2$ butterflies, where each butterfly requires 1 complex multiplication and 2 complex additions.
  * Total complex multiplications: $\frac{N}{2} \log_2 N$.
  * Total complex additions: $N \log_2 N$.

---

### Question 4: Bilinear Transformation & Frequency Warping
**Interviewer:**  
"How does the Bilinear Transformation map the analog $s$-plane to the digital $z$-plane? Why is frequency pre-warping necessary?"

#### Model Answer:
* **Transformation Equation:**
  $$s = \frac{2}{T_s} \frac{1 - z^{-1}}{1 + z^{-1}}$$
* **Geometric Mapping:**
  * Evaluating on $s = j\Omega$ and $z = e^{j\omega}$:
    $$j\Omega = \frac{2}{T_s} \frac{1 - e^{-j\omega}}{1 + e^{-j\omega}} = j \frac{2}{T_s} \tan\left(\frac{\omega}{2}\right)$$
  * The entire infinite imaginary axis of the $s$-plane ($-\infty < \Omega < \infty$) is compressed and mapped non-linearly onto the finite circumference of the unit circle in the $z$-plane ($-\pi \le \omega \le \pi$).
  * The Left-Half Plane ($\operatorname{Re}(s) < 0$) is mapped strictly inside the unit circle ($|z| < 1$), guaranteeing stability.
* **Why Pre-Warping is Necessary:**
  * Due to the non-linear tangent relationship $\omega = 2 \arctan\left(\frac{\Omega T_s}{2}\right)$, the frequency scale is compressed (**warped**), especially at higher frequencies.
  * To ensure the designed digital filter meets exact cutoff/passband specifications at desired digital frequency $\omega_c$, we must "pre-warp" the analog prototype cutoff frequency using:
    $$\Omega_c = \frac{2}{T_s} \tan\left(\frac{\omega_c}{2}\right)$$
  * Without pre-warping, the digital filter's cutoff would shift significantly from the target.

---

### Question 5: Direct Form I vs. Direct Form II Transposed
**Interviewer:**  
"Why does MATLAB’s `filter` function implement Direct Form II Transposed instead of Direct Form I or standard Direct Form II?"

#### Model Answer:
1. **Memory Minimization:** Direct Form I requires $M + N$ state registers, whereas Direct Form II Transposed is canonical and requires only $\max(M, N)$ states.
2. **Elimination of Intermediate Node Overflow:** Standard Direct Form II computes an internal intermediate feedback node $w[n] = x[n] - \sum a_k w[n-k]$. In resonant filters with poles near the unit circle, $|w[n]|$ can grow very large even when the input and final output are small, causing internal clipping/overflow in fixed-point and floating-point registers.
3. **Pipelining and Accumulation into Delays:** In Direct Form II Transposed, products are summed directly into the state delay registers before storage:
   $$s_k[n] = b_k x[n] - a_k y[n] + s_{k+1}[n-1]$$
   This enables fused multiply-accumulate (FMA) instructions on modern CPUs and DSP chips, minimizes round-off noise, and makes it numerically far more stable.
