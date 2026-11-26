with open('/home/jaswanth/mathworks_intrevPrep/docs/teslanetsim_style_reference.css', 'r') as f:
    custom_css = f.read()

template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="generator" content="Asciidoctor 2.0.26">
<title>Oppenheim DSP Master Reference • Discrete-Time Signals to Filter Design</title>
<style>
__CUSTOM_CSS__

/* Extra polishing for Print / PDF export and MathJax */
@media print {
  #toc.toc2 { display: none !important; }
  #content { margin-left: 0 !important; width: 100% !important; }
  .toolbar-container { display: none !important; }
  details.module-card { border: 1px solid #ccc !important; break-inside: avoid; }
  details.module-card:not([open]) { display: block !important; }
  .module-body { display: block !important; }
}

.search-box-container {
  margin-top: 10px;
  display: flex;
  gap: 10px;
  align-items: center;
}
.search-input-field {
  padding: 6px 12px;
  border: 1px solid #cbd5e1;
  border-radius: 4px;
  font-size: 13px;
  width: 280px;
  outline: none;
}
.search-input-field:focus {
  border-color: #ba3925;
}
</style>

<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  messageStyle: "none",
  tex2jax: {
    inlineMath: [["\\\\(", "\\\\)"], ["$", "$"]],
    displayMath: [["\\\\[", "\\\\]"], ["$$", "$$"]],
    ignoreClass: "nostem|nolatexmath"
  },
  TeX: { equationNumbers: { autoNumber: "none" } }
});
</script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-MML-AM_CHTML"></script>
<script>
function expandAll() {
  document.querySelectorAll('details.module-card').forEach(d => d.open = true);
}
function collapseAll() {
  document.querySelectorAll('details.module-card').forEach(d => d.open = false);
}
function filterModules(query) {
  const q = query.toLowerCase().trim();
  document.querySelectorAll('details.module-card').forEach(card => {
    if (!q) {
      card.style.display = '';
      return;
    }
    const text = card.innerText.toLowerCase();
    card.style.display = text.includes(q) ? '' : 'none';
  });
}
</script>
</head>
<body class="article toc2 toc-left">

<div id="header">
<h1>Oppenheim DSP Master Reference & Technical Guide</h1>
<div class="details">
<span id="author" class="author">Discrete-Time Signals, Systems, Transforms & Filter Design • Tailored for MathWorks EDG Track</span><br>
</div>
<div id="toc" class="toc2">
<div id="toctitle">Table of Contents</div>
<ul class="sectlevel1">
<li><a href="#_part1_signals_systems"><strong>Part I: Discrete-Time Signals & Systems (Ch. 2)</strong></a>
<ul class="sectlevel2">
<li><a href="#_mod1_dt_signals">Module 1: Signals, Basic Sequences & Discrete Sinusoids</a></li>
<li><a href="#_mod2_lti_systems">Module 2: Discrete-Time Systems, Linearity & Convolution</a></li>
<li><a href="#_mod3_dtft_theorems">Module 3: Frequency-Domain Analysis, DTFT & Theorems</a></li>
</ul>
</li>
<li><a href="#_part2_z_transform"><strong>Part II: The z-Transform & System Functions (Ch. 3)</strong></a>
<ul class="sectlevel2">
<li><a href="#_mod4_z_transform_roc">Module 4: The z-Transform, ROC Properties & Inversion</a></li>
<li><a href="#_mod5_z_lti_systems">Module 5: Transfer Functions, Difference Equations & Causality</a></li>
</ul>
</li>
<li><a href="#_part3_sampling_multirate"><strong>Part III: Sampling of Continuous-Time Signals & Multirate (Ch. 4)</strong></a>
<ul class="sectlevel2">
<li><a href="#_mod6_sampling_aliasing">Module 6: Periodic Sampling, Aliasing & Sinc Reconstruction</a></li>
<li><a href="#_mod7_multirate_dsp">Module 7: Multirate Signal Processing, Decimation & Polyphase</a></li>
<li><a href="#_mod8_quantization_noise">Module 8: A/D Conversion, Quantization Noise & Noise Shaping</a></li>
</ul>
</li>
<li><a href="#_part4_transform_analysis"><strong>Part IV: Transform Analysis of LTI Systems (Ch. 5)</strong></a>
<ul class="sectlevel2">
<li><a href="#_mod9_frequency_response_phase">Module 9: Frequency Response, Phase & Group Delay Distortion</a></li>
<li><a href="#_mod10_allpass_minphase">Module 10: Allpass Systems, Minimum-Phase & Linear-Phase FIR</a></li>
</ul>
</li>
<li><a href="#_part5_filter_structures"><strong>Part V: Structures for Discrete-Time Systems (Ch. 6)</strong></a>
<ul class="sectlevel2">
<li><a href="#_mod11_filter_structures">Module 11: IIR & FIR Filter Realizations (Direct Form II Transposed)</a></li>
<li><a href="#_mod12_finite_wordlength">Module 12: Finite-Precision Numerical Effects & Limit Cycles</a></li>
</ul>
</li>
<li><a href="#_part6_filter_design"><strong>Part VI: Filter Design Techniques (Ch. 7)</strong></a>
<ul class="sectlevel2">
<li><a href="#_mod13_iir_design">Module 13: IIR Filter Design: Impulse Invariance & Bilinear Transform</a></li>
<li><a href="#_mod14_fir_design">Module 14: FIR Filter Design: Windowing & Parks-McClellan Remez</a></li>
</ul>
</li>
<li><a href="#_part7_mathworks_edg"><strong>Part VII: MathWorks EDG Systems, MATLAB & C/DSA</strong></a>
<ul class="sectlevel2">
<li><a href="#_mod15_matlab_toolbox">Module 15: MATLAB Signal Processing Toolbox & Streaming Algorithms</a></li>
<li><a href="#_mod16_c_dsp_dsa">Module 16: C Memory Architecture, Circular Buffers & LeetCode DSA</a></li>
<li><a href="#_mod17_mock_interviews">Module 17: MathWorks Mock Technical Interview Question Bank</a></li>
</ul>
</li>
</ul>
</div>
</div>

<div id="content">

<div id="preamble">
<div class="sectionbody">
<div class="paragraph">
<p>Welcome to the <strong>Oppenheim DSP Master Reference & MathWorks EDG Preparation Portal</strong>. This guide systematically walks through every foundational concept from the index of <em>Alan V. Oppenheim & Ronald W. Schafer’s Discrete-Time Signal Processing</em> up to <strong>Filter Design Techniques (Chapters 2 through 7)</strong>, complemented with production-grade <strong>MATLAB Signal Processing Toolbox idioms</strong>, <strong>C programming memory architectures</strong>, and <strong>real MathWorks technical interview problems</strong>.</p>
</div>

<div class="toolbar-container">
  <div style="font-size: 13px; color: #475569; font-weight: 500;">
    💡 <strong>Module Navigation:</strong> Expand or collapse complete modules below, or filter by keyword.
  </div>
  <div class="toolbar-btn-group">
    <button class="tool-btn" onclick="expandAll()">Expand All Modules</button>
    <button class="tool-btn" onclick="collapseAll()">Collapse All</button>
    <button class="tool-btn tool-btn-primary" onclick="window.print()">Export Full Guide to PDF</button>
  </div>
</div>

<div class="search-box-container">
  <span style="font-size: 13px; font-weight: 600; color: #2c3e50;">🔍 Instant Search:</span>
  <input type="text" class="search-input-field" placeholder="Filter concepts (e.g., aliasing, bilinear, circular buffer)..." oninput="filterModules(this.value)">
</div>

</div>
</div>

<!-- ======================================================== -->
<!-- PART I: DISCRETE-TIME SIGNALS & SYSTEMS                  -->
<!-- ======================================================== -->
<div class="sect1">
<h2 id="_part1_signals_systems">Part I: Discrete-Time Signals & Systems (Oppenheim Chapter 2)</h2>
<div class="sectionbody">

<!-- MODULE 1 -->
<details class="module-card" open id="_mod1_dt_signals">
  <summary class="module-summary">
    <div><span class="module-badge">Oppenheim 2.0 - 2.1</span> Module 1: Discrete-Time Signals, Basic Sequences & Discrete Sinusoids</div>
    <span style="font-size: 14px; color: #64748b;">▼</span>
  </summary>
  <div class="module-body">
    <h3>1.1 Discrete-Time Representation of Sequences</h3>
    <p>A discrete-time signal is represented mathematically as a sequence of numbers $x[n]$ defined only for integer values of $n \in (-\infty, \infty)$. Unlike continuous-time functions $x_a(t)$, $x[n]$ is <em>undefined</em> between integer indices.</p>

    <div class="flow-diagram-container">
      <div class="flow-diagram-title">⚡ Fundamental Elementary Sequences</div>
      <div class="pipeline-grid">
        <div class="pipeline-step">
          <div class="step-num">δ[n]</div>
          <div class="step-info">
            <div class="step-title">Unit Impulse (Kronecker Delta)</div>
            <div class="step-desc">$$\delta[n] = \begin{cases} 1, & n = 0 \\ 0, & n \neq 0 \end{cases}$$ Any arbitrary sequence can be decomposed as a linear combination of weighted impulses: $x[n] = \sum_{k=-\infty}^{\infty} x[k] \delta[n-k]$.</div>
          </div>
        </div>
        <div class="pipeline-step">
          <div class="step-num">u[n]</div>
          <div class="step-info">
            <div class="step-title">Unit Step Sequence</div>
            <div class="step-desc">$$u[n] = \begin{cases} 1, & n \ge 0 \\ 0, & n < 0 \end{cases}, \quad u[n] = \sum_{k=-\infty}^n \delta[k] = \sum_{k=0}^\infty \delta[n-k]$$ Relationship: $\delta[n] = u[n] - u[n-1]$.</div>
          </div>
        </div>
        <div class="pipeline-step">
          <div class="step-num">e^jωn</div>
          <div class="step-info">
            <div class="step-title">Complex Exponential Sequence</div>
            <div class="step-desc">$$x[n] = A \alpha^n = |A| e^{j\phi} (|\alpha| e^{j\omega_0})^n = |A| |\alpha|^n e^{j(\omega_0 n + \phi)}$$ If $|\alpha| = 1$, $x[n] = e^{j\omega_0 n} = \cos(\omega_0 n) + j\sin(\omega_0 n)$.</div>
          </div>
        </div>
      </div>
    </div>

    <h3>1.2 Fundamental Differences Between Continuous and Discrete Sinusoids (MathWorks High-Yield)</h3>
    <p>Oppenheim emphasizes three profound properties that distinguish discrete-time sinusoids $e^{j\omega_0 n}$ from continuous-time $e^{j\Omega_0 t}$:</p>

    <div class="admonitionblock important">
      <table>
        <tr>
          <td class="icon"><div class="title">Important</div></td>
          <td class="content">
            <strong>1. Frequency Periodicity ($2\pi$):</strong><br>
            $$e^{j(\omega_0 + 2\pi) n} = e^{j\omega_0 n} \cdot e^{j 2\pi n} = e^{j\omega_0 n} \cdot 1 = e^{j\omega_0 n}$$
            All discrete frequencies $\omega$ separated by an integer multiple of $2\pi$ are <strong>physically indistinguishable</strong>. We only need to consider frequencies over an interval of length $2\pi$, typically $[-\pi, \pi]$ or $[0, 2\pi]$.<br><br>
            <strong>2. Highest Rate of Oscillation Occurs at $\omega = \pi$:</strong><br>
            As $\omega_0$ increases from $0$ to $\pi$, the oscillation rate increases. At $\omega = \pi$, $x[n] = e^{j\pi n} = (-1)^n$, which alternates signs every single sample (highest rate of variation). As $\omega$ increases from $\pi$ to $2\pi$, the apparent rate of oscillation <em>decreases</em> until $\omega = 2\pi$ corresponds back to DC ($\omega = 0$).<br><br>
            <strong>3. Periodicity of the Sequence in Time:</strong><br>
            A continuous sinusoid $\cos(\Omega_0 t)$ is <em>always</em> periodic in time for any $\Omega_0$. A discrete sinusoid $\cos(\omega_0 n)$ is periodic in time <strong>if and only if</strong> $\omega_0 / (2\pi)$ is a rational number:
            $$\frac{\omega_0}{2\pi} = \frac{k}{N} \implies N = \frac{2\pi k}{\omega_0} \in \mathbb{Z}^+$$
          </td>
        </tr>
      </table>
    </div>
  </div>
</details>

<!-- MODULE 2 -->
<details class="module-card" id="_mod2_lti_systems">
  <summary class="module-summary">
    <div><span class="module-badge">Oppenheim 2.2 - 2.5</span> Module 2: Discrete-Time Systems, Linearity, Convolution & LCCDE</div>
    <span style="font-size: 14px; color: #64748b;">▼</span>
  </summary>
  <div class="module-body">
    <h3>2.1 System Properties & Classification</h3>
    <table class="tableblock">
      <thead>
        <tr>
          <th>Property</th>
          <th>Mathematical Condition</th>
          <th>LTI Impulse Response $h[n]$ Criterion</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Linearity</strong></td>
          <td>$\mathcal{T}\{a x_1[n] + b x_2[n]\} = a \mathcal{T}\{x_1[n]\} + b \mathcal{T}\{x_2[n]\}$</td>
          <td>Satisfied if system consists only of additions, multiplications by constants, and delay elements.</td>
        </tr>
        <tr>
          <td><strong>Time-Invariance</strong></td>
          <td>If $\mathcal{T}\{x[n]\} = y[n]$, then $\mathcal{T}\{x[n - n_0]\} = y[n - n_0]$</td>
          <td>Impulse response $h[n]$ must not vary with the time of excitation: $\mathcal{T}\{\delta[n - k]\} = h[n - k]$.</td>
        </tr>
        <tr>
          <td><strong>Causality</strong></td>
          <td>$y[n_0]$ depends only on $x[n]$ for $n \le n_0$.</td>
          <td><strong>$h[n] = 0$ for all $n < 0$.</strong></td>
        </tr>
        <tr>
          <td><strong>BIBO Stability</strong></td>
          <td>If $|x[n]| \le B_x < \infty$, then $|y[n]| \le B_y < \infty$.</td>
          <td><strong>$S = \sum_{n=-\infty}^{\infty} |h[n]| < \infty$ (Absolutely summable).</strong></td>
        </tr>
      </tbody>
    </table>

    <h3>2.2 The Linear Convolution Sum</h3>
    <p>By linearity and time-invariance, the response of any LTI system to an arbitrary input $x[n] = \sum_{k=-\infty}^\infty x[k]\delta[n-k]$ is given by the convolution sum:</p>
    $$y[n] = x[n] * h[n] = \sum_{k=-\infty}^{\infty} x[k] h[n - k] = \sum_{k=-\infty}^{\infty} h[k] x[n - k]$$

    <div class="admonitionblock tip">
      <table>
        <tr>
          <td class="icon"><div class="title">Tip</div></td>
          <td class="content">
            <strong>Convolution Length Rule:</strong> If $x[n]$ has length $N_1$ ($n \in [0, N_1-1]$) and $h[n]$ has length $N_2$ ($n \in [0, N_2-1]$), the non-zero duration of $y[n]$ is:
            $$L_y = N_1 + N_2 - 1$$
            Interviewers frequently ask this to verify memory preallocation in C or MATLAB!
          </td>
        </tr>
      </table>
    </div>

    <h3>2.3 Linear Constant-Coefficient Difference Equations (LCCDE)</h3>
    <p>An important class of discrete-time LTI systems is described by $N^{\text{th}}$-order difference equations:</p>
    $$\sum_{k=0}^N a_k y[n - k] = \sum_{m=0}^M b_m x[n - m], \quad a_0 \neq 0$$
    <p>For the system to be linear, time-invariant, and causal, it must satisfy the <strong>condition of initial rest</strong>: if $x[n] = 0$ for $n < n_0$, then $y[n] = 0$ for $n < n_0$.</p>
  </div>
</details>

<!-- MODULE 3 -->
<details class="module-card" id="_mod3_dtft_theorems">
  <summary class="module-summary">
    <div><span class="module-badge">Oppenheim 2.6 - 2.10</span> Module 3: Frequency-Domain Analysis, DTFT & Core Theorems</div>
    <span style="font-size: 14px; color: #64748b;">▼</span>
  </summary>
  <div class="module-body">
    <h3>3.1 Eigenfunctions of LTI Systems</h3>
    <p>When an LTI system with impulse response $h[n]$ is excited by a complex exponential $x[n] = e^{j\omega n}$:</p>
    $$y[n] = \sum_{k=-\infty}^\infty h[k] e^{j\omega (n - k)} = \left( \sum_{k=-\infty}^\infty h[k] e^{-j\omega k} \right) e^{j\omega n} = H(e^{j\omega}) e^{j\omega n}$$
    <p>Hence, <strong>complex exponentials are eigenfunctions of LTI systems</strong>, and the eigenvalue $H(e^{j\omega})$ is the <strong>Frequency Response</strong> of the system.</p>

    <h3>3.2 The Discrete-Time Fourier Transform (DTFT)</h3>
    <table class="tableblock">
      <thead>
        <tr>
          <th>Analysis Equation (Forward DTFT)</th>
          <th>Synthesis Equation (Inverse DTFT)</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>$$X(e^{j\omega}) = \sum_{n=-\infty}^{\infty} x[n] e^{-j\omega n}$$</td>
          <td>$$x[n] = \frac{1}{2\pi} \int_{-\pi}^{\pi} X(e^{j\omega}) e^{j\omega n} d\omega$$</td>
        </tr>
      </tbody>
    </table>

    <h3>3.3 Symmetry Properties for Real Sequences</h3>
    <p>If $x[n]$ is real-valued, $X(e^{-j\omega}) = X^*(e^{j\omega})$ (Conjugate Symmetry):</p>
    <ul>
      <li><strong>Real Part $\operatorname{Re}\{X(e^{j\omega})\}$:</strong> Even function of $\omega$ ($\operatorname{Re}\{X(e^{j\omega})\} = \operatorname{Re}\{X(e^{-j\omega})\}$).</li>
      <li><strong>Imaginary Part $\operatorname{Im}\{X(e^{j\omega})\}$:</strong> Odd function of $\omega$ ($\operatorname{Im}\{X(e^{j\omega})\} = -\operatorname{Im}\{X(e^{-j\omega})\}$).</li>
      <li><strong>Magnitude Spectrum $|X(e^{j\omega})|$:</strong> Even function of $\omega$.</li>
      <li><strong>Phase Spectrum $\arg X(e^{j\omega})$:</strong> Odd function of $\omega$.</li>
    </ul>

    <h3>3.4 Essential DTFT Theorems (Oppenheim Table 2.2)</h3>
    <div class="pipeline-grid">
      <div class="pipeline-step">
        <div class="step-num">T1</div>
        <div class="step-info">
          <div class="step-title">Time Shifting & Frequency Shifting</div>
          <div class="step-desc">$$x[n - n_0] \stackrel{\mathcal{F}}{\longleftrightarrow} e^{-j\omega n_0} X(e^{j\omega}), \quad e^{j\omega_0 n} x[n] \stackrel{\mathcal{F}}{\longleftrightarrow} X(e^{j(\omega - \omega_0)})$$</div>
        </div>
      </div>
      <div class="pipeline-step">
        <div class="step-num">T2</div>
        <div class="step-info">
          <div class="step-title">Convolution Theorem</div>
          <div class="step-desc">$$x[n] * h[n] \stackrel{\mathcal{F}}{\longleftrightarrow} X(e^{j\omega}) \cdot H(e^{j\omega})$$ Convolution in the time domain is equivalent to point-by-point multiplication in the frequency domain.</div>
        </div>
      </div>
      <div class="pipeline-step">
        <div class="step-num">T3</div>
        <div class="step-info">
          <div class="step-title">Modulation / Windowing Theorem</div>
          <div class="step-desc">$$x[n] \cdot w[n] \stackrel{\mathcal{F}}{\longleftrightarrow} \frac{1}{2\pi} \int_{-\pi}^{\pi} X(e^{j\theta}) W(e^{j(\omega - \theta)}) d\theta = \frac{1}{2\pi} X(e^{j\omega}) \circledast W(e^{j\omega})$$ Multiplication in time results in periodic circular convolution in frequency (the mathematical source of spectral leakage).</div>
        </div>
      </div>
      <div class="pipeline-step">
        <div class="step-num">T4</div>
        <div class="step-info">
          <div class="step-title">Parseval’s Energy Theorem</div>
          <div class="step-desc">$$E = \sum_{n=-\infty}^\infty |x[n]|^2 = \frac{1}{2\pi} \int_{-\pi}^{\pi} |X(e^{j\omega})|^2 d\omega$$ Total energy in time domain equals total energy in frequency domain.</div>
        </div>
      </div>
    </div>
  </div>
</details>

</div>
</div>

<!-- ======================================================== -->
<!-- PART II: THE Z-TRANSFORM                                 -->
<!-- ======================================================== -->
<div class="sect1">
<h2 id="_part2_z_transform">Part II: The z-Transform & System Functions (Oppenheim Chapter 3)</h2>
<div class="sectionbody">

<!-- MODULE 4 -->
<details class="module-card" id="_mod4_z_transform_roc">
  <summary class="module-summary">
    <div><span class="module-badge">Oppenheim 3.0 - 3.4</span> Module 4: The z-Transform, ROC Properties & Inversion Techniques</div>
    <span style="font-size: 14px; color: #64748b;">▼</span>
  </summary>
  <div class="module-body">
    <h3>4.1 Definition & Relation to DTFT</h3>
    <p>The bilateral $z$-transform generalizes the Fourier transform to complex frequencies $z = r e^{j\omega}$:</p>
    $$X(z) = \sum_{n=-\infty}^{\infty} x[n] z^{-n}$$
    <p>When evaluated on the unit circle ($|z| = r = 1$), the $z$-transform reduces identically to the DTFT: $X(e^{j\omega}) = X(z)\big|_{z = e^{j\omega}}$. For the DTFT to exist, the unit circle must lie within the Region of Convergence (ROC).</p>

    <h3>4.2 All Properties of the Region of Convergence (ROC)</h3>
    <div class="admonitionblock note">
      <table>
        <tr>
          <td class="icon"><div class="title">Note</div></td>
          <td class="content">
            <ol>
              <li>The ROC is a ring or disk in the $z$-plane centered at the origin: $r_R < |z| < r_L$.</li>
              <li>The Fourier transform of $x[n]$ converges absolutely $\iff$ <strong>the ROC includes the unit circle $|z| = 1$</strong>.</li>
              <li>The ROC cannot contain any poles.</li>
              <li>If $x[n]$ is a <strong>finite-duration sequence</strong>, the ROC is the entire $z$-plane, except possibly $z = 0$ (if $x[n]$ has non-zero values for $n > 0$) and/or $z = \infty$ (if $x[n]$ has non-zero values for $n < 0$).</li>
              <li>If $x[n]$ is a <strong>right-sided sequence</strong> (causal-type), the ROC extends outward from the outermost finite pole to infinity: $|z| > r_{\max}$.</li>
              <li>If $x[n]$ is a <strong>left-sided sequence</strong> (anti-causal), the ROC extends inward from the innermost non-zero pole to zero: $|z| < r_{\min}$.</li>
              <li>If $x[n]$ is a <strong>two-sided sequence</strong>, the ROC is an open ring between two concentric circles containing no poles: $r_1 < |z| < r_2$.</li>
            </ol>
          </td>
        </tr>
      </table>
    </div>

    <h3>4.3 Inverse z-Transform by Partial Fraction Expansion</h3>
    <p>For rational system functions $X(z) = \frac{P(z)}{Q(z)}$, expand $X(z)$ in partial fractions of $z^{-1}$:</p>
    $$X(z) = \sum_{k=1}^N \frac{A_k}{1 - d_k z^{-1}}$$
    <p>Each individual term maps according to the specified ROC:</p>
    <ul>
      <li>If ROC is $|z| > |d_k|$ (Right-sided): $\frac{1}{1 - d_k z^{-1}} \longleftrightarrow d_k^n u[n]$</li>
      <li>If ROC is $|z| < |d_k|$ (Left-sided): $\frac{1}{1 - d_k z^{-1}} \longleftrightarrow -d_k^n u[-n - 1]$</li>
    </ul>
  </div>
</details>

<!-- MODULE 5 -->
<details class="module-card" id="_mod5_z_lti_systems">
  <summary class="module-summary">
    <div><span class="module-badge">Oppenheim 3.5 - 3.6</span> Module 5: Transfer Functions, Difference Equations & Causality vs Stability</div>
    <span style="font-size: 14px; color: #64748b;">▼</span>
  </summary>
  <div class="module-body">
    <h3>5.1 The System Function (Transfer Function)</h3>
    <p>Applying the convolution property $\mathcal{Z}\{x[n] * h[n]\} = X(z) H(z)$, the system transfer function is:</p>
    $$H(z) = \frac{Y(z)}{X(z)} = \frac{\sum_{m=0}^M b_m z^{-m}}{1 + \sum_{k=1}^N a_k z^{-k}} = b_0 \frac{\prod_{m=1}^M (1 - c_m z^{-1})}{\prod_{k=1}^N (1 - d_k z^{-1})}$$
    <p>where $c_m$ are system zeros, and $d_k$ are system poles.</p>

    <h3>5.2 Causality and Stability Criteria</h3>
    <div class="flow-diagram-container">
      <div class="flow-diagram-title">⚖️ The Stability & Causality Matrix</div>
      <table class="tableblock">
        <thead>
          <tr>
            <th>System Condition</th>
            <th>Region of Convergence (ROC)</th>
            <th>Pole Locations in the $z$-Plane</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Causal System</strong></td>
            <td>ROC extends outward from outermost pole: $|z| > \max_k |d_k|$</td>
            <td>Poles can be anywhere, but ROC must be exterior of a circle.</td>
          </tr>
          <tr>
            <td><strong>Stable System (BIBO)</strong></td>
            <td>ROC must include the unit circle: $|z| = 1 \in \text{ROC}$</td>
            <td>Unit circle cannot pass through any pole.</td>
          </tr>
          <tr>
            <td><strong>Causal AND Stable System</strong></td>
            <td>ROC: $|z| > \max_k |d_k|$ where $\max_k |d_k| < 1$</td>
            <td><strong>ALL poles must lie STRICTLY INSIDE the unit circle: $|d_k| < 1$ for all $k$.</strong></td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</details>

</div>
</div>

<!-- ======================================================== -->
<!-- PART III: SAMPLING & MULTIRATE                           -->
<!-- ======================================================== -->
<div class="sect1">
<h2 id="_part3_sampling_multirate">Part III: Sampling of Continuous-Time Signals & Multirate (Oppenheim Chapter 4)</h2>
<div class="sectionbody">

<!-- MODULE 6 -->
<details class="module-card" id="_mod6_sampling_aliasing">
  <summary class="module-summary">
    <div><span class="module-badge">Oppenheim 4.0 - 4.4</span> Module 6: Periodic Sampling, Aliasing & Sinc Reconstruction</div>
    <span style="font-size: 14px; color: #64748b;">▼</span>
  </summary>
  <div class="module-body">
    <h3>6.1 Periodic Sampling & Spectral Replication</h3>
    <p>Sampling a continuous signal $x_a(t)$ with interval $T$ creates discrete sequence $x[n] = x_a(n T)$. In the frequency domain, the spectrum of the sampled sequence $X(e^{j\omega})$ is an infinite periodic sum of shifted replicas of $X_a(j\Omega)$:</p>
    $$X(e^{j\omega}) = \frac{1}{T} \sum_{k=-\infty}^{\infty} X_a\left( j\left(\frac{\omega - 2\pi k}{T}\right) \right)$$
    <p>where continuous frequency $\Omega$ and discrete frequency $\omega$ are linked by: $\omega = \Omega T$.</p>

    <h3>6.2 The Nyquist-Shannon Sampling Theorem</h3>
    <div class="admonitionblock important">
      <table>
        <tr>
          <td class="icon"><div class="title">Important</div></td>
          <td class="content">
            Let $x_a(t)$ be a bandlimited continuous signal with $X_a(j\Omega) = 0$ for $|\Omega| > \Omega_N$. Then $x_a(t)$ is uniquely determined by its samples $x[n] = x_a(nT)$ if and only if:
            $$\Omega_s = \frac{2\pi}{T} \ge 2 \Omega_N \iff f_s \ge 2 f_N$$
            If $f_s < 2 f_N$, spectral copies overlap, corrupting the signal by <strong>aliasing</strong>. Frequencies fold back according to:
            $$f_{\text{alias}} = |f_0 - k f_s| \le \frac{f_s}{2}$$
          </td>
        </tr>
      </table>
    </div>

    <h3>6.3 Ideal Reconstruction (Whittaker-Shannon Sinc Interpolation)</h3>
    <p>Passing the impulse-modulated sampled signal through an ideal analog lowpass reconstruction filter with gain $T$ and cutoff $\Omega_c = \pi / T$ recovers the continuous signal exactly:</p>
    $$x_a(t) = \sum_{n=-\infty}^{\infty} x[n] \cdot \operatorname{sinc}\left( \frac{t - n T}{T} \right), \quad \text{where } \operatorname{sinc}(u) = \frac{\sin(\pi u)}{\pi u}$$
  </div>
</details>

<!-- MODULE 7 -->
<details class="module-card" id="_mod7_multirate_dsp">
  <summary class="module-summary">
    <div><span class="module-badge">Oppenheim 4.6 - 4.7</span> Module 7: Multirate Signal Processing, Decimation, Interpolation & Polyphase</div>
    <span style="font-size: 14px; color: #64748b;">▼</span>
  </summary>
  <div class="module-body">
    <h3>7.1 Decimation by Integer Factor $M$ (Downsampling)</h3>
    <p>Decimation reduces the sampling rate by factor $M$. To prevent aliasing at the lower rate, the signal must first pass through a digital anti-aliasing lowpass filter with cutoff $\omega_c = \pi / M$, followed by a compressor that retains every $M^{\text{th}}$ sample:</p>
    $$y[m] = x[m M], \quad Y(e^{j\omega}) = \frac{1}{M} \sum_{k=0}^{M-1} X\left(e^{j\frac{\omega - 2\pi k}{M}}\right)$$

    <h3>7.2 Interpolation by Integer Factor $L$ (Upsampling)</h3>
    <p>Interpolation increases the sampling rate by factor $L$ in two stages:</p>
    <ol>
      <li><strong>Expander (Zero-insertion):</strong> Inserts $L-1$ zeros between samples: $x_e[n] = x[n/L]$ for $n = 0, \pm L, \dots$ (compresses frequency spectrum by factor $L$, producing $L-1$ unwanted spectral images).</li>
      <li><strong>Anti-Imaging Filter:</strong> Digital lowpass filter with cutoff $\omega_c = \pi / L$ and gain $L$ to remove spectral images and interpolate values.</li>
    </ol>

    <h3>7.3 Polyphase Decomposition & Computational Savings</h3>
    <p>A transfer function $H(z)$ can be decomposed into $M$ polyphase components:</p>
    $$H(z) = \sum_{k=0}^{M-1} z^{-k} E_k(z^M)$$
    <div class="admonitionblock tip">
      <table>
        <tr>
          <td class="icon"><div class="title">Tip</div></td>
          <td class="content">
            <strong>The Noble Identity:</strong> Filtering by $E_k(z^M)$ followed by downsampling by $M$ is mathematically identical to downsampling by $M$ first, then filtering by $E_k(z)$.<br>
            <strong>Computational Benefit:</strong> Filtering occurs at the <em>low decimated sampling rate $f_s/M$</em> rather than the high rate $f_s$, reducing arithmetic operations by a factor of $M$!
          </td>
        </tr>
      </table>
    </div>
  </div>
</details>

<!-- MODULE 8 -->
<details class="module-card" id="_mod8_quantization_noise">
  <summary class="module-summary">
    <div><span class="module-badge">Oppenheim 4.8 - 4.9</span> Module 8: A/D Conversion, Quantization Noise & Noise Shaping</div>
    <span style="font-size: 14px; color: #64748b;">▼</span>
  </summary>
  <div class="module-body">
    <h3>8.1 Statistical Model of Quantization Errors</h3>
    <p>When an analog voltage is quantized by a $(B+1)$-bit uniform analog-to-digital converter with full-scale range $[-X_m, X_m]$, the quantization step size is:</p>
    $$\Delta = \frac{2 X_m}{2^{B+1}} = \frac{X_m}{2^B}$$
    <p>Assuming the quantization error $e[n]$ is uniformly distributed between $[-\Delta/2, \Delta/2]$ and uncorrelated with the input signal, the quantization noise variance is:</p>
    $$\sigma_e^2 = \frac{\Delta^2}{12} = \frac{X_m^2 2^{-2B}}{12}$$

    <h3>8.2 The 6 dB Per Bit Rule (SQNR)</h3>
    <p>For a full-scale sinusoidal input of amplitude $X_m$, the signal power is $\sigma_x^2 = X_m^2 / 2$. The Signal-to-Quantization-Noise Ratio is:</p>
    $$\text{SQNR} = 10 \log_{10}\left( \frac{\sigma_x^2}{\sigma_e^2} \right) = 10 \log_{10}\left( \frac{X_m^2 / 2}{X_m^2 2^{-2B} / 12} \right) = 10 \log_{10}(1.5 \cdot 2^{2B}) \approx 6.02 B + 1.76 \text{ dB}$$
    <p><strong>Every additional bit of ADC wordlength improves dynamic range by approximately $6\text{ dB}$.</strong></p>

    <h3>8.3 Oversampling & Noise Shaping (Sigma-Delta $\Sigma\Delta$)</h3>
    <p>Oversampling by ratio $\text{OSR} = f_s / (2 f_B)$ spreads the fixed quantization noise $\sigma_e^2$ over a wider frequency band $[0, f_s/2]$. Adding a feedback integrator (first-order noise shaping) filters the noise by transfer function $H_n(z) = 1 - z^{-1}$, pushing noise power out of the low-frequency audio/sensor band into high frequencies where it is removed by a simple digital decimation filter.</p>
  </div>
</details>

</div>
</div>

<!-- ======================================================== -->
<!-- PART IV: TRANSFORM ANALYSIS                              -->
<!-- ======================================================== -->
<div class="sect1">
<h2 id="_part4_transform_analysis">Part IV: Transform Analysis of LTI Systems (Oppenheim Chapter 5)</h2>
<div class="sectionbody">

<!-- MODULE 9 -->
<details class="module-card" id="_mod9_frequency_response_phase">
  <summary class="module-summary">
    <div><span class="module-badge">Oppenheim 5.0 - 5.3</span> Module 9: Frequency Response, Phase & Group Delay Distortion</div>
    <span style="font-size: 14px; color: #64748b;">▼</span>
  </summary>
  <div class="module-body">
    <h3>9.1 Phase and Group Delay</h3>
    <p>The frequency response of an LTI system is a complex function of frequency: $H(e^{j\omega}) = |H(e^{j\omega})| e^{j\theta(\omega)}$.</p>
    <ul>
      <li><strong>Phase Response:</strong> $\theta(\omega) = \arg H(e^{j\omega})$</li>
      <li><strong>Phase Delay:</strong> $\tau_p(\omega) = -\frac{\theta(\omega)}{\omega}$</li>
      <li><strong>Group Delay:</strong> $\tau_g(\omega) = -\frac{d}{d\omega} \left[ \theta(\omega) \right]$</li>
    </ul>

    <h3>9.2 Physical Meaning of Group Delay Distortion</h3>
    <div class="admonitionblock warning">
      <table>
        <tr>
          <td class="icon"><div class="title">Warning</div></td>
          <td class="content">
            Group delay represents the effective time delay experienced by a narrow-band wave packet centered at frequency $\omega$. If $\tau_g(\omega)$ is constant for all $\omega$, all frequency components travel through the system with identical delay, preserving waveform fidelity.<br><br>
            If $\tau_g(\omega)$ varies with frequency (as in all non-linear phase IIR filters), different frequency components arrive at different times. This causes <strong>dispersion</strong>, severely distorting ECG pulses in biomedical instruments and causing Inter-Symbol Interference (ISI) in high-speed digital communications!
          </td>
        </tr>
      </table>
    </div>

    <h3>9.3 Geometric Evaluation of Magnitude & Phase from Pole-Zero Plots</h3>
    <p>Given $H(z) = b_0 \frac{\prod_{m=1}^M (z - c_m)}{\prod_{k=1}^N (z - d_k)}$, evaluating at $z = e^{j\omega}$ on the unit circle:</p>
    $$|H(e^{j\omega})| = |b_0| \frac{\prod_{m=1}^M |e^{j\omega} - c_m|}{\prod_{k=1}^N |e^{j\omega} - d_k|}, \quad \arg H(e^{j\omega}) = \arg(b_0) + \sum_{m=1}^M \arg(e^{j\omega} - c_m) - \sum_{k=1}^N \arg(e^{j\omega} - d_k)$$
    <p>As point $e^{j\omega}$ traverses the unit circle, proximity to a pole produces a peak in $|H(e^{j\omega})|$, while proximity to a zero produces a notch or valley.</p>
  </div>
</details>

<!-- MODULE 10 -->
<details class="module-card" id="_mod10_allpass_minphase">
  <summary class="module-summary">
    <div><span class="module-badge">Oppenheim 5.4 - 5.6</span> Module 10: Allpass Systems, Minimum-Phase & Generalized Linear Phase FIR</div>
    <span style="font-size: 14px; color: #64748b;">▼</span>
  </summary>
  <div class="module-body">
    <h3>10.1 Allpass Systems</h3>
    <p>An allpass system has a constant magnitude response across all frequencies: $|H_{\text{ap}}(e^{j\omega})| = 1$ for all $\omega$. Its transfer function is a cascade of first- and second-order sections exhibiting reciprocal pole-zero symmetry:</p>
    $$H_{\text{ap}}(z) = \prod_{k=1}^N \frac{z^{-1} - d_k^*}{1 - d_k z^{-1}}$$
    <p>For every pole at $z = d_k$ inside the unit circle, there is a corresponding zero at $z = 1/d_k^*$ outside the unit circle. Allpass systems are widely used as <strong>phase equalizers</strong>.</p>

    <h3>10.2 Minimum-Phase Systems & Canonical Decomposition</h3>
    <p>A stable, causal LTI system is <strong>minimum-phase</strong> if and only if <strong>all of its poles AND all of its zeros lie strictly inside the unit circle</strong>.</p>
    <div class="admonitionblock note">
      <table>
        <tr>
          <td class="icon"><div class="title">Note</div></td>
          <td class="content">
            <strong>Key Properties of Minimum-Phase Systems:</strong>
            <ol>
              <li><strong>Minimum Phase-Lag & Minimum Group Delay:</strong> Among all systems having the exact same magnitude response, the minimum-phase system has the smallest phase lag and smallest group delay.</li>
              <li><strong>Minimum Energy Delay:</strong> Energy is concentrated as close to the time origin $n=0$ as possible.</li>
              <li><strong>Stable & Causal Inverse:</strong> Because all zeros are inside the unit circle, the inverse system $H_i(z) = 1/H(z)$ is also causal and stable!</li>
              <li><strong>Unique Factorization:</strong> Any rational system can be factored uniquely into a minimum-phase system and an allpass system:
              $$H(z) = H_{\min}(z) \cdot H_{\text{ap}}(z)$$</li>
            </ol>
          </td>
        </tr>
      </table>
    </div>

    <h3>10.3 The Four Types of Linear-Phase FIR Systems (Oppenheim Table 5.1)</h3>
    <p>Linear phase requires the impulse response to exhibit symmetry: $h[n] = \pm h[M - n]$ where $M$ is the filter order (length $N = M+1$).</p>
    <table class="tableblock">
      <thead>
        <tr>
          <th>Type</th>
          <th>Symmetry</th>
          <th>Order $M$ / Length $N$</th>
          <th>Mandatory Inherent Zeros</th>
          <th>Supported Filter Applications</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Type I</strong></td>
          <td>Symmetric ($h[n] = h[M-n]$)</td>
          <td>$M$ Even, $N$ Odd</td>
          <td>None</td>
          <td><strong>Lowpass, Highpass, Bandpass, Bandstop (Universal)</strong></td>
        </tr>
        <tr>
          <td><strong>Type II</strong></td>
          <td>Symmetric ($h[n] = h[M-n]$)</td>
          <td>$M$ Odd, $N$ Even</td>
          <td>Zero at $z = -1$ ($\omega = \pi$)</td>
          <td>Lowpass, Bandpass. <strong>Cannot design Highpass or Bandstop!</strong></td>
        </tr>
        <tr>
          <td><strong>Type III</strong></td>
          <td>Antisymmetric ($h[n] = -h[M-n]$)</td>
          <td>$M$ Even, $N$ Odd</td>
          <td>Zeros at $z = 1$ ($\omega = 0$) and $z = -1$ ($\omega = \pi$)</td>
          <td>Differentiators, Hilbert Transformers. <strong>Cannot design LP/HP!</strong></td>
        </tr>
        <tr>
          <td><strong>Type IV</strong></td>
          <td>Antisymmetric ($h[n] = -h[M-n]$)</td>
          <td>$M$ Odd, $N$ Even</td>
          <td>Zero at $z = 1$ ($\omega = 0$)</td>
          <td>Highpass, Differentiators, Hilbert Transformers.</td>
        </tr>
      </tbody>
    </table>
  </div>
</details>

</div>
</div>

<!-- ======================================================== -->
<!-- PART V: FILTER STRUCTURES & NUMERICAL EFFECTS            -->
<!-- ======================================================== -->
<div class="sect1">
<h2 id="_part5_filter_structures">Part V: Structures for Discrete-Time Systems (Oppenheim Chapter 6)</h2>
<div class="sectionbody">

<!-- MODULE 11 -->
<details class="module-card" id="_mod11_filter_structures">
  <summary class="module-summary">
    <div><span class="module-badge">Oppenheim 6.0 - 6.6</span> Module 11: IIR & FIR Filter Realizations (Direct Form II Transposed)</div>
    <span style="font-size: 14px; color: #64748b;">▼</span>
  </summary>
  <div class="module-body">
    <h3>11.1 Comparison of Basic Filter Realization Structures</h3>
    <table class="tableblock">
      <thead>
        <tr>
          <th>Realization Structure</th>
          <th>Delay Registers</th>
          <th>Internal Overflow Risk</th>
          <th>Practical MathWorks / DSP Application</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Direct Form I</strong></td>
          <td>$M + N$ (Non-canonical)</td>
          <td>Low</td>
          <td>Simple hardware with separate zero/pole stages.</td>
        </tr>
        <tr>
          <td><strong>Direct Form II (Canonical)</strong></td>
          <td>$\max(M, N)$ (Canonical)</td>
          <td><span style="color: #bf0000; font-weight: bold;">High</span> (Intermediate node $w[n]$ overflows)</td>
          <td>Textbook canonical form; avoided in fixed-point processors.</td>
        </tr>
        <tr>
          <td><strong>Direct Form II Transposed</strong></td>
          <td>$\max(M, N)$ (Canonical)</td>
          <td><span style="color: #4a7a15; font-weight: bold;">Minimal</span> (Direct delay accumulation)</td>
          <td><strong>Standard implementation used by MATLAB <code>filter.m</code> and DSP chips!</strong></td>
        </tr>
        <tr>
          <td><strong>Cascade Form (SOS / Biquads)</strong></td>
          <td>$\max(M, N)$</td>
          <td>Very Low</td>
          <td><strong>Mandatory for high-order IIR filters</strong> to eliminate pole sensitivity.</td>
        </tr>
      </tbody>
    </table>

    <h3>11.2 Direct Form II Transposed Signal Flow (Tellegen's Theorem)</h3>
    <p>By Transposition Theorem, reversing all signal paths, swapping branch points with summing nodes, and interchanging input/output leaves the transfer function identical:</p>
    $$y[n] = b_0 x[n] + s_1[n-1]$$
    $$s_k[n] = b_k x[n] - a_k y[n] + s_{k+1}[n-1]$$
    <div class="admonitionblock tip">
      <table>
        <tr>
          <td class="icon"><div class="title">Tip</div></td>
          <td class="content">
            <strong>Why MATLAB <code>filter</code> uses Direct Form II Transposed:</strong> Products $b_k x[n]$ and $-a_k y[n]$ are accumulated directly into delay registers before storage. Modern CPUs execute this using hardware Fused Multiply-Accumulate (FMA) instructions, minimizing quantization noise and completely preventing internal node dynamic overflow.
          </td>
        </tr>
      </table>
    </div>

    <h3>11.3 Cascade Realization (Second-Order Sections / Biquads)</h3>
    <p>High-order direct form polynomials have extreme <strong>pole sensitivity</strong>: a tiny perturbation in high-order polynomial coefficients $a_k$ causes clustered poles to migrate outside the unit circle ($|d_k| \ge 1$), inducing violent instability! To prevent this, always factor $H(z)$ into second-order biquads:</p>
    $$H(z) = b_0 \prod_{k=1}^K \frac{1 + \beta_{1k} z^{-1} + \beta_{2k} z^{-2}}{1 + \alpha_{1k} z^{-1} + \alpha_{2k} z^{-2}}$$
  </div>
</details>

<!-- MODULE 12 -->
<details class="module-card" id="_mod12_finite_wordlength">
  <summary class="module-summary">
    <div><span class="module-badge">Oppenheim 6.7 - 6.10</span> Module 12: Finite-Precision Numerical Effects & Limit Cycles</div>
    <span style="font-size: 14px; color: #64748b;">▼</span>
  </summary>
  <div class="module-body">
    <h3>12.1 Sources of Finite-Wordlength Errors</h3>
    <div class="pipeline-grid">
      <div class="pipeline-step">
        <div class="step-num">E1</div>
        <div class="step-info">
          <div class="step-title">A/D Input Quantization</div>
          <div class="step-desc">Quantizing continuous sensor samples to $B+1$ bits introduces white additive noise of variance $\sigma_e^2 = \Delta^2 / 12$.</div>
        </div>
      </div>
      <div class="pipeline-step">
        <div class="step-num">E2</div>
        <div class="step-info">
          <div class="step-title">Coefficient Quantization</div>
          <div class="step-desc">Truncating filter coefficients $b_k, a_k$ shifts pole and zero locations in the $z$-plane, distorting cutoff frequency and risking instability.</div>
        </div>
      </div>
      <div class="pipeline-step">
        <div class="step-num">E3</div>
        <div class="step-info">
          <div class="step-title">Arithmetic Round-Off & Accumulation Noise</div>
          <div class="step-desc">Multiplying two $(B+1)$-bit numbers yields a $2B$-bit product. Quantizing back to $(B+1)$ bits injects round-off noise into the feedback loop.</div>
        </div>
      </div>
      <div class="pipeline-step">
        <div class="step-num">E4</div>
        <div class="step-info">
          <div class="step-title">Dynamic Range Overflow & Limit Cycles</div>
          <div class="step-desc">In Two's complement arithmetic, positive overflow wraps around to large negative numbers, exciting sustained non-linear periodic oscillations (limit cycles).</div>
        </div>
      </div>
    </div>

    <h3>12.2 Zero-Input Limit Cycles</h3>
    <p>In fixed-point recursive IIR filters with zero input ($x[n] = 0$), two distinct non-linear limit cycles can occur:</p>
    <ol>
      <li><strong>Granular Limit Cycles (Round-Off Deadbands):</strong> Small-amplitude oscillations trapped within the round-off deadband around zero.</li>
      <li><strong>Overflow Limit Cycles:</strong> Large-amplitude, full-scale rail-to-rail square wave oscillations caused by Two's complement wrap-around overflow.</li>
    </ol>
    <div class="admonitionblock important">
      <table>
        <tr>
          <td class="icon"><div class="title">Important</div></td>
          <td class="content">
            <strong>How to Eliminate Overflow Limit Cycles:</strong> Replace standard Two's complement wrap-around addition with <strong>saturation arithmetic</strong>! When an addition exceeds the maximum positive representation, it is clamped to $+1.0$ (or $+32767$ in Q15), completely breaking the feedback cycle.
          </td>
        </tr>
      </table>
    </div>
  </div>
</details>

</div>
</div>

<!-- ======================================================== -->
<!-- PART VI: FILTER DESIGN TECHNIQUES                        -->
<!-- ======================================================== -->
<div class="sect1">
<h2 id="_part6_filter_design">Part VI: Filter Design Techniques (Oppenheim Chapter 7)</h2>
<div class="sectionbody">

<!-- MODULE 13 -->
<details class="module-card" id="_mod13_iir_design">
  <summary class="module-summary">
    <div><span class="module-badge">Oppenheim 7.0 - 7.4</span> Module 13: IIR Filter Design: Impulse Invariance & Bilinear Transformation</div>
    <span style="font-size: 14px; color: #64748b;">▼</span>
  </summary>
  <div class="module-body">
    <h3>13.1 Filter Design Specifications</h3>
    <p>Filter requirements are defined in four parameters:</p>
    <ul>
      <li>Passband cutoff: $\omega_p$, Passband ripple: $\delta_1$ (or $R_p = -20\log_{10}(1 - \delta_1)\text{ dB}$)</li>
      <li>Stopband cutoff: $\omega_s$, Stopband attenuation: $\delta_2$ (or $A_s = -20\log_{10}(\delta_2)\text{ dB}$)</li>
      <li>Transition band: $\Delta\omega = \omega_s - \omega_p$</li>
    </ul>

    <h3>13.2 Design by Impulse Invariance</h3>
    <p>Samples continuous impulse response: $h[n] = T_s h_a(n T_s)$, which maps continuous poles to discrete poles via: $s_k \longrightarrow z_k = e^{s_k T_s}$.</p>
    <div class="admonitionblock warning">
      <table>
        <tr>
          <td class="icon"><div class="title">Warning</div></td>
          <td class="content">
            <strong>Fatal Limitation of Impulse Invariance:</strong> Because continuous frequency maps linearly to discrete frequency ($\omega = \Omega T$), <strong>aliasing is unavoidable</strong> unless the analog prototype is strictly bandlimited to $|\Omega| < \pi / T$. Consequently, Impulse Invariance <em>cannot</em> be used to design Highpass or Bandstop filters!
          </td>
        </tr>
      </table>
    </div>

    <h3>13.3 Design by Bilinear Transformation (BLT)</h3>
    <p>Conformal algebraic mapping from analog $s$-plane to discrete $z$-plane:</p>
    $$s = \frac{2}{T_s} \frac{1 - z^{-1}}{1 + z^{-1}}$$
    <table class="tableblock">
      <thead>
        <tr>
          <th>Bilinear Transform Property</th>
          <th>Mathematical Derivation / Result</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>No Aliasing</strong></td>
          <td>Compresses entire infinite imaginary axis $-\infty < \Omega < \infty$ onto unit circle $-\pi < \omega < \pi$.</td>
        </tr>
        <tr>
          <td><strong>Guaranteed Stability</strong></td>
          <td>Maps Left-Half $s$-plane ($\operatorname{Re}(s) < 0$) strictly inside unit circle ($|z| < 1$).</td>
        </tr>
        <tr>
          <td><strong>Frequency Warping</strong></td>
          <td>$$\omega = 2 \arctan\left(\frac{\Omega T_s}{2}\right) \iff \Omega = \frac{2}{T_s} \tan\left(\frac{\omega}{2}\right)$$</td>
        </tr>
        <tr>
          <td><strong>Mandatory Pre-Warping</strong></td>
          <td>$$\Omega_c = \frac{2}{T_s} \tan\left(\frac{\omega_c}{2}\right)$$ Prevents cutoff distortion.</td>
        </tr>
      </tbody>
    </table>

    <h3>13.4 Classic Continuous-Time Prototypes</h3>
    <ul>
      <li><strong>Butterworth:</strong> Maximally flat passband, monotonic roll-off in stopband.</li>
      <li><strong>Chebyshev Type I:</strong> Equiripple in passband, monotonic in stopband. Faster transition than Butterworth.</li>
      <li><strong>Chebyshev Type II:</strong> Monotonic in passband, equiripple in stopband (maximally flat delay at DC).</li>
      <li><strong>Elliptic (Cauer):</strong> Equiripple in both passband and stopband. Achieves steepest transition for a given filter order!</li>
    </ul>
  </div>
</details>

<!-- MODULE 14 -->
<details class="module-card" id="_mod14_fir_design">
  <summary class="module-summary">
    <div><span class="module-badge">Oppenheim 7.5 - 7.8</span> Module 14: FIR Filter Design: Windowing Method & Parks-McClellan Optimal Remez</div>
    <span style="font-size: 14px; color: #64748b;">▼</span>
  </summary>
  <div class="module-body">
    <h3>14.1 FIR Design by Windowing</h3>
    <p>Truncates ideal infinite impulse response $h_d[n] = \frac{\sin(\omega_c (n - M/2))}{\pi (n - M/2)}$ by multiplying with a finite window $w[n]$:</p>
    $$h[n] = h_d[n] \cdot w[n]$$
    <div class="admonitionblock important">
      <table>
        <tr>
          <td class="icon"><div class="title">Important</div></td>
          <td class="content">
            <strong>Gibbs Phenomenon:</strong> Truncating with a Rectangular window produces an unavoidable $\approx 9\%$ ripple overshoot ($-21\text{ dB}$ stopband attenuation) near band discontinuities, regardless of how large filter order $M$ is!<br>
            To suppress ripples, apply smooth tapered windows:
          </td>
        </tr>
      </table>
    </div>

    <table class="tableblock">
      <thead>
        <tr>
          <th>Window Type</th>
          <th>Mainlobe Width ($\Delta\omega$)</th>
          <th>Peak Sidelobe (dB)</th>
          <th>Stopband Attenuation (dB)</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><strong>Rectangular</strong></td><td>$4\pi / M$</td><td>$-13\text{ dB}$</td><td>$-21\text{ dB}$</td></tr>
        <tr><td><strong>Hanning (Hann)</strong></td><td>$8\pi / M$</td><td>$-31\text{ dB}$</td><td>$-44\text{ dB}$</td></tr>
        <tr><td><strong>Hamming</strong></td><td>$8\pi / M$</td><td>$-41\text{ dB}$</td><td>$-53\text{ dB}$</td></tr>
        <tr><td><strong>Blackman</strong></td><td>$12\pi / M$</td><td>$-58\text{ dB}$</td><td>$-74\text{ dB}$</td></tr>
        <tr><td><strong>Kaiser ($\beta$)</strong></td><td>Tunable by parameter $\beta$</td><td>Tunable (up to $-100\text{ dB}$)</td><td>Empirical formulas by J. F. Kaiser</td></tr>
      </tbody>
    </table>

    <h3>14.2 Optimal Equiripple FIR: Parks-McClellan (Remez Exchange)</h3>
    <p>Formulates filter design as a Chebyshev minimax approximation problem: minimize the maximum approximation error over passband and stopband:</p>
    $$\min_{h[n]} \max_{\omega \in F} W(\omega) \left| A(e^{j\omega}) - D(\omega) \right|$$
    <div class="admonitionblock tip">
      <table>
        <tr>
          <td class="icon"><div class="title">Tip</div></td>
          <td class="content">
            <strong>Alternation Theorem:</strong> An optimal Type I lowpass filter of order $M$ has an equiripple error curve exhibiting at least $r = M/2 + 2$ alternating local extrema. The Parks-McClellan algorithm uses the Remez exchange iteration to converge onto these optimal extremal frequencies.
          </td>
        </tr>
      </table>
    </div>
  </div>
</details>

</div>
</div>

<!-- ======================================================== -->
<!-- PART VII: MATHWORKS EDG PRACTICE                         -->
<!-- ======================================================== -->
<div class="sect1">
<h2 id="_part7_mathworks_edg">Part VII: MathWorks EDG Implementation, MATLAB & C/DSA</h2>
<div class="sectionbody">

<!-- MODULE 15 -->
<details class="module-card" id="_mod15_matlab_toolbox">
  <summary class="module-summary">
    <div><span class="module-badge">MATLAB Mastery</span> Module 15: MATLAB Signal Processing Toolbox & Streaming Algorithms</div>
    <span style="font-size: 14px; color: #64748b;">▼</span>
  </summary>
  <div class="module-body">
    <h3>15.1 Vectorization Patterns Expected at MathWorks</h3>
    <pre><code>% In-place sliding moving average using cumulative sums (O(1) execution!)
function y = fast_movavg(x, N)
    cs = cumsum([0, x(:).']);
    y = (cs(N+1:end) - cs(1:end-N)) / N;
end</code></pre>

    <h3>15.2 Zero-Phase Forward-Backward Filtering (<code>filtfilt</code>)</h3>
    <p>In offline biomedical or radar signal processing, <code>filtfilt(b, a, x)</code> performs forward-backward filtering to cancel phase distortion ($\angle H(\omega) \equiv 0$), doubling magnitude attenuation ($|H(e^{j\omega})|^2$). In contrast, real-time live streaming audio requires causal <code>filter(b, a, x)</code> or DSP System Objects (<code>dsp.FIRFilter</code>).</p>
  </div>
</details>

<!-- MODULE 16 -->
<details class="module-card" id="_mod16_c_dsp_dsa">
  <summary class="module-summary">
    <div><span class="module-badge">C Systems & DSA</span> Module 16: C Memory Architecture, Circular Buffers & LeetCode DSA</div>
    <span style="font-size: 14px; color: #64748b;">▼</span>
  </summary>
  <div class="module-body">
    <h3>16.1 O(1) Circular Buffer for Streaming DSP in C</h3>
    <pre><code>#include &lt;stdlib.h&gt;
#include &lt;stdbool.h&gt;

typedef struct {
    float *buffer;
    size_t capacity;
    size_t head;
    size_t count;
    double running_sum;
} RingBufferFilter;

RingBufferFilter* ring_init(size_t window_size) {
    RingBufferFilter *f = (RingBufferFilter *)malloc(sizeof(RingBufferFilter));
    if (!f) return NULL;
    f->buffer = (float *)calloc(window_size, sizeof(float));
    if (!f->buffer) { free(f); return NULL; }
    f->capacity = window_size;
    f->head = 0;
    f->count = 0;
    f->running_sum = 0.0;
    return f;
}

float ring_process(RingBufferFilter *f, float sample) {
    f->running_sum -= f->buffer[f->head];      // Subtract oldest sample
    f->buffer[f->head] = sample;               // Insert new sample
    f->running_sum += sample;
    
    // Power of 2 bitwise modulo optimization:
    f->head = (f->head + 1) % f->capacity;
    if (f->count < f->capacity) f->count++;
    return (float)(f->running_sum / f->count);
}</code></pre>

    <h3>16.2 In-Place 90° Clockwise Matrix Rotation (LeetCode 48)</h3>
    <pre><code>void rotate_matrix(int n, int matrix[n][n]) {
    // Step 1: Transpose matrix along diagonal
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            int tmp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = tmp;
        }
    }
    // Step 2: Reverse each row horizontally
    for (int i = 0; i < n; ++i) {
        int l = 0, r = n - 1;
        while (l < r) {
            int tmp = matrix[i][l];
            matrix[i][l] = matrix[i][r];
            matrix[i][r] = tmp;
            l++; r--;
        }
    }
}</code></pre>
  </div>
</details>

<!-- MODULE 17 -->
<details class="module-card" id="_mod17_mock_interviews">
  <summary class="module-summary">
    <div><span class="module-badge">Mock Screening</span> Module 17: MathWorks Mock Technical Interview Question Bank</div>
    <span style="font-size: 14px; color: #64748b;">▼</span>
  </summary>
  <div class="module-body">
    <h3>17.1 Real MathWorks EDG Screening Questions</h3>
    <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 6px; padding: 16px; margin-bottom: 16px;">
      <p style="font-weight: bold; color: #1e293b; margin-top: 0;">Q1: Multi-Tone Sampling & Aliasing</p>
      <p>Given $x(t) = 3\cos(600\pi t) + 2\cos(1800\pi t) + \sin(3000\pi t)$ sampled at $f_s = 1200\text{ Hz}$: What is the Nyquist rate, and what discrete frequencies appear in the sampled signal?</p>
      <p style="color: #64748b; font-size: 13.5px;"><strong>Model Answer:</strong> Frequencies are $300\text{ Hz}$, $900\text{ Hz}$, and $1500\text{ Hz}$. Nyquist rate $2 f_{\max} = 3000\text{ Hz}$. Folding limit is $f_s/2 = 600\text{ Hz}$. $300\text{ Hz}$ remains at $300\text{ Hz}$; $900\text{ Hz}$ aliases to $|900 - 1200| = 300\text{ Hz}$; $1500\text{ Hz}$ aliases to $|1500 - 1200| = 300\text{ Hz}$. All three tones collapse into the single alias frequency of $300\text{ Hz}$!</p>
    </div>

    <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 6px; padding: 16px;">
      <p style="font-weight: bold; color: #1e293b; margin-top: 0;">Q2: Why does MATLAB <code>filter</code> implement Direct Form II Transposed?</p>
      <p style="color: #64748b; font-size: 13.5px;"><strong>Model Answer:</strong> It uses canonical $\max(M, N)$ delay elements, sums multiplications directly into delay registers (optimal for hardware FMA instructions), eliminates internal summing node overflow inherent to standard Direct Form II, and achieves superior fixed-point round-off noise performance.</p>
    </div>
  </div>
</details>

</div>
</div>

</div>

<div id="footer">
<div id="footer-text">
Oppenheim DSP Master Reference • Prepared for MathWorks EDG Candidates • Ready for GitHub Pages
</div>
</div>

</body>
</html>
"""

final_html = template.replace("__CUSTOM_CSS__", custom_css)
with open('/home/jaswanth/mathworks_intrevPrep/index.html', 'w') as f:
    f.write(final_html)

print("index.html generated successfully! Length:", len(final_html))
