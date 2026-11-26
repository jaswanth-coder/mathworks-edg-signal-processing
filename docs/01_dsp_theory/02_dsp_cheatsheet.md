# DSP Quick Revision Cheatsheet & Rapid Recall Matrix

---

## 1. Quick Formula Sheet

| Concept | Continuous-Time ($t$) | Discrete-Time ($n$) | Key Condition / Notes |
| :--- | :--- | :--- | :--- |
| **Convolution** | $(x * h)(t) = \int_{-\infty}^{\infty} x(\tau)h(t-\tau)d\tau$ | $(x * h)[n] = \sum_k x[k]h[n-k]$ | Length $L = N_1 + N_2 - 1$ |
| **Fourier Transform** | $X(F) = \int x(t)e^{-j2\pi F t}dt$ | $X(e^{j\omega}) = \sum x[n]e^{-j\omega n}$ | DTFT is $2\pi$-periodic |
| **Discrete Fourier (DFT)** | - | $X[k] = \sum_{n=0}^{N-1} x[n] e^{-j\frac{2\pi}{N} kn}$ | $\Delta f = \frac{f_s}{N}$ |
| **Inverse DFT (IDFT)**| - | $x[n] = \frac{1}{N}\sum_{k=0}^{N-1} X[k] e^{j\frac{2\pi}{N} kn}$ | Factor $1/N$ in IDFT |
| **Z-Transform** | $\mathcal{L}\{x(t)\} = \int x(t)e^{-st}dt$ | $X(z) = \sum x[n]z^{-n}$ | $z = r e^{j\omega}$, Unit Circle $r=1$ |
| **Nyquist Criterion** | $f_s \ge 2 f_{\max}$ | $\omega_s \ge 2\omega_{\max}$ | $f_{\text{alias}} = \|f_0 - k f_s\|$ |
| **Linear Phase Delay**| Group Delay: $\tau_g = -\frac{d\phi}{d\omega}$ | Phase Delay: $\tau_p = -\frac{\phi(\omega)}{\omega}$ | FIR symmetry $h[n]=h[M-n] \implies \tau_g = M/2$ |
| **Bilinear Transform**| $s = \frac{2}{T}\frac{1-z^{-1}}{1+z^{-1}}$ | $\Omega = \frac{2}{T}\tan(\omega/2)$ | Always pre-warp: $\Omega_c = \frac{2}{T}\tan(\omega_c/2)$ |
| **Wiener-Khinchin** | $S_{xx}(F) = \mathcal{F}\{R_{xx}(\tau)\}$ | $S_{xx}(e^{j\omega}) = \mathcal{DTFT}\{r_{xx}[k]\}$ | $S_{xx} \ge 0$, real, even |

---

## 2. Decision Tree: Filter Selection

```
Need a Digital Filter?
          |
  -----------------
  |               |
Phase critical?   Phase delay can be equalized?
(Audio, ECG,      (Control loops, low-latency comms)
 Radar, Comms)    |
  |               v
  v         Is lowest computational power & lowest order primary?
Use FIR           |
  |         +-----+-----+
  |         | YES       | NO
  |         v           v
  |     Use IIR        Use FIR
  |
  +-> Linear Phase Type:
      - Lowpass / Bandpass / Bandstop -> Type I (Symmetric, M Even, N Odd)
      - Highpass                     -> Type I or Type IV
      - Hilbert / Differentiator     -> Type III or Type IV
```

---

## 3. High-Yield Interview Gotchas & Traps

1. **"Can an IIR filter have exact linear phase?"**
   * *Answer:* NO, a causal and stable IIR filter cannot have exact linear phase. A linear phase system requires its poles to be symmetric with respect to the unit circle: if $p$ is a pole, $1/p^*$ must also be a pole. If all poles are strictly inside the unit circle for stability ($|p| < 1$), the reciprocal poles $|1/p^*| > 1$ must be outside, violating causality.
   * *Workaround in MATLAB:* Use `filtfilt` (forward-backward zero-phase filtering) for offline/batch signals.

2. **"Does zero-padding in time increase FFT resolution?"**
   * *Answer:* NO. Zero-padding increases spectral sample density (interpolation of the DTFT curve), but the true physical resolution is determined solely by total observation time: $\Delta f_{\text{phys}} = \frac{1}{T_{\text{record}}} = \frac{1}{N T_s}$.

3. **"Why can't Type II FIR filters be used for Highpass filtering?"**
   * *Answer:* In Type II FIR ($h[n] = h[M-n]$ with $M$ odd, even length $N$), the frequency response $H(e^{j\omega})$ has an inherent zero at $\omega = \pi$. Therefore, it cannot pass frequencies at or near $\pi$ (the highest discrete frequency), making Highpass and Bandstop designs impossible.

4. **"Circular Convolution vs Linear Convolution:"**
   * *Trap:* Multiplying two DFTs and taking IDFT performs **circular convolution**, NOT linear convolution.
   * *Rule:* Zero-pad both sequences to length $L \ge L_1 + L_2 - 1$.

5. **"Why does MATLAB `filter` use Direct Form II Transposed?"**
   * *Answer:* It requires minimal memory states ($\max(M,N)$), eliminates internal summation node overflow, and significantly reduces roundoff noise accumulation when running on fixed-point or double-precision architectures.
