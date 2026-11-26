# MathWorks EDG Interview Preparation Kit: Signal Processing Track

Comprehensive preparation and revision package for the **MathWorks Engineering Development Group (EDG) — Signal Processing Track**.

---

## 📂 Repository Structure

```
.
├── index.html                                 <- Interactive Web Dashboard (Deployable to GitHub Pages & Local Browser)
├── README.md                                  <- This Guide & Deployment Instructions
│
├── docs/
│   ├── 01_dsp_theory/
│   │   ├── 01_dsp_learning_guide.md           <- In-depth DSP Theory & Mathematical Formulations
│   │   └── 02_dsp_cheatsheet.md               <- Formula Sheets, Decision Trees & Gotchas
│   │
│   ├── 02_matlab_dsp/
│   │   ├── 01_matlab_dsp_learning.md          <- Signal Processing Toolbox, DSP System Toolbox & Coding Patterns
│   │   └── 02_matlab_dsp_cheatsheet.md        <- Key MATLAB Commands, Vectorization & Snippets
│   │
│   ├── 03_c_programming_dsa/
│   │   ├── 01_c_dsa_learning_guide.md         <- C Memory Architecture, Low-level DSP in C, Core DSA
│   │   └── 02_c_dsa_cheatsheet.md             <- Quick Reference, Bit Manipulation & Complexities
│   │
│   └── 04_mock_interviews/
│       ├── 01_dsp_mock_questions.md           <- Core DSP Mock Technical Questions with Model Answers
│       ├── 02_matlab_mock_questions.md        <- MATLAB Algorithmic & Toolbox Questions
│       └── 03_c_dsa_mock_questions.md         <- C Live-Coding, Pointer Debugging & LeetCode Matrix Qs
│
└── [Textbooks in Root Directory]
    ├── Oppenheim & Schafer: Discrete-Time Signal Processing
    ├── Sanjit K. Mitra: Digital Signal Processing: A Computer-Based Approach
    └── Vinay K. Ingle & John G. Proakis: Digital Signal Processing using MATLAB
```

---

## 🌐 Webpage (GitHub Pages) vs. Presentation vs. PDF: Which is Better?

> **Verdict: The Webpage deployed on GitHub Pages is far superior, with built-in 1-click PDF export!**

| Feature | Interactive Webpage (GitHub Pages) | Slide Presentation | Static PDF |
| :--- | :--- | :--- | :--- |
| **Interactive Diagrams & Signal Flows** | ✅ SVG & dynamic visualizations | ❌ Static images | ❌ Static images |
| **Mock Interview Practice** | ✅ Collapsible reveal-on-click answers & hints | ❌ Inconvenient | ❌ Answers visible right away |
| **Copyable Code Snippets** | ✅ 1-Click copy to MATLAB / C IDE | ❌ Manual retyping | ⚠️ Formatting breaks on copy |
| **Search & Filtering** | ✅ Live instant keyword search bar | ❌ Clunky | ⚠️ Basic text find |
| **Export to PDF** | ✅ Supported natively via **"Export PDF" / `Ctrl+P`** | ❌ Clunky export | Native |

You get the best of both worlds: an interactive learning portal on your desktop/mobile phone, plus clean printable PDF output whenever you want offline reading.

---

## 🚀 How to View & Deploy to GitHub Pages

### 1. View Locally Right Now:
You can open `index.html` directly in any web browser:
```bash
# Option A: Open directly in your browser
google-chrome index.html
# or
xdg-open index.html

# Option B: Run a lightweight local HTTP server
python3 -m http.server 8000
# Then visit http://localhost:8000 in your browser
```

### 2. Deploy to GitHub Pages in 3 Simple Steps:
1. Initialize git and commit:
   ```bash
   cd /home/jaswanth/mathworks_intrevPrep
   git init
   git add index.html README.md docs/
   git commit -m "Initial commit: MathWorks EDG Signal Processing prep portal"
   ```
2. Create a repository on GitHub (e.g. `mathworks-signal-processing-prep`), and push:
   ```bash
   git branch -M main
   git remote add origin https://github.com/<your-username>/mathworks-signal-processing-prep.git
   git push -u origin main
   ```
3. Enable GitHub Pages:
   - Go to your repository **Settings** $\to$ **Pages**
   - Under **Build and deployment** $\to$ **Source**, choose **Deploy from a branch**
   - Select branch `main` and folder `/ (root)`, then click **Save**
   - Your live revision portal will be active at: `https://<your-username>.github.io/mathworks-signal-processing-prep/`

---

## 🎯 Syllabus Summary for MathWorks EDG Signal Processing

### 1. Digital Signal Processing (DSP):
* **LTI Systems:** Linearity, Time-Invariance, Causality, BIBO Stability ($\sum |h[n]| < \infty$), Linear Convolution.
* **Sampling & Aliasing:** Nyquist theorem ($f_s \ge 2 f_{\max}$), folding frequency calculation ($f_{\text{alias}} = |f_0 - k f_s|$), anti-aliasing lowpass filters.
* **Transforms:** DTFT vs DFT vs DFS vs Z-Transform. ROC properties, pole-zero stability mapping (all poles inside unit circle $|z| < 1$).
* **Fast Fourier Transform (FFT):** Radix-2 Cooley-Tukey DIT/DIF, twiddle factor symmetries ($W_N^{k + N/2} = -W_N^k$), bit-reversal, computational reduction from $O(N^2)$ to $O(N \log N)$.
* **Digital Filters:** FIR (linear phase Type I-IV, windowing, Parks-McClellan equiripple) vs IIR (Butterworth, Chebyshev, Elliptic, Bilinear Transformation, frequency warping, pre-warping).
* **Filter Structures:** Direct Form I, Direct Form II, Direct Form II Transposed (why MATLAB `filter` uses DF-II Transposed), Biquad Cascades.
* **Multirate DSP:** Decimation ($M$), Interpolation ($L$), Noble identities, Polyphase decomposition.
* **Random Signals & Spectral Estimation:** Autocorrelation, Cross-correlation, Wiener-Khinchin theorem, Periodogram vs Welch's method (`pwelch`).

### 2. MATLAB & Toolboxes:
* **Vectorization & Memory:** Contiguous preallocation, column-major cache locality, logical indexing, elimination of slow `for` loops.
* **Signal Generation:** Setting up time and frequency axes properly ($t = 0:1/fs:T-1/fs$, `fft`, `fftshift`, single-sided amplitude scaling).
* **Signal Processing Toolbox:** `filter`, `filtfilt` (zero-phase forward-backward), `fftfilt` (overlap-add), `findpeaks`, `butter`, `firpm`, `designfilt`, `pwelch`.
* **DSP System Toolbox:** Streaming paradigm with System Objects (`dsp.FIRFilter`, `dsp.AsyncBuffer`), frame-based execution, `%#codegen` readiness for C/C++ generation.
* **MathWorks Live-Coding Favorites:** In-place sliding moving average, numerical integration (`trapz`), matrix rotation, peak detection.

### 3. C Programming & Data Structures (DSA):
* **C Memory & Systems:** Pointers, double pointers, dynamic memory allocation (`malloc`, `calloc`, `realloc`, `free`), memory leak prevention, dangling pointer avoidance, struct padding, `volatile`, `static`, bit manipulation (power of 2, bit reversal, endianness).
* **DSP in C:** 1D linear convolution, $O(1)$ streaming moving average with circular buffer, Direct Form II Transposed filter engine, peak detection with plateau resolution, numerical integration (Trapezoid), Q15 fixed-point saturation arithmetic.
* **DSA Patterns:** Circular queue/ring buffer, in-place matrix rotation ($O(1)$ space), find peak element in $O(\log N)$ time, linked list reversal and cycle detection.
