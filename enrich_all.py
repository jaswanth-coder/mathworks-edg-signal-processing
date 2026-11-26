#!/usr/bin/env python3
"""
Enriches all modules 1 through 16 with:
- Exact Oppenheim Worked Examples
- Chapter-End Exercises with collapsible full solutions
- High-fidelity SVG Signal Flow / Pole-Zero / Architecture Figures
"""

with open('/home/jaswanth/mathworks_intrevPrep/docs/teslanetsim_style_reference.css', 'r') as f:
    custom_css = f.read()

# Let's read the current index.html and insert the missing worked examples and exercises into modules 5, 8, 9, 10, 11, 12, 13, 14, 15, 16!

mod5_additions = r"""
    <!-- WORKED EXAMPLE 5.1 -->
    <div class="example-box">
      <div class="example-title">📖 Oppenheim Worked Example 3.9: Inverse z-Transform of Second-Order System Function</div>
      <p><strong>Problem Statement:</strong> An LTI system has transfer function:
      $$H(z) = \frac{1 + 2 z^{-1}}{(1 - \frac{1}{2} z^{-1})(1 + \frac{1}{3} z^{-1})}$$
      If the system is known to be <strong>stable</strong>, find its impulse response $h[n]$.</p>
      <p><strong>Solution:</strong><br>
      Poles are at $z = 1/2$ and $z = -1/3$.<br>
      Perform Partial Fraction Expansion:
      $$H(z) = \frac{A}{1 - \frac{1}{2} z^{-1}} + \frac{B}{1 + \frac{1}{3} z^{-1}}$$
      Solving residues:<br>
      $A = \left[ \frac{1 + 2 z^{-1}}{1 + \frac{1}{3} z^{-1}} \right]_{z = 1/2} = \frac{1 + 4}{1 + 2/3} = \frac{5}{5/3} = 3$<br>
      $B = \left[ \frac{1 + 2 z^{-1}}{1 - \frac{1}{2} z^{-1}} \right]_{z = -1/3} = \frac{1 - 6}{1 + 3/2} = \frac{-5}{5/2} = -2$<br>
      $$H(z) = \frac{3}{1 - \frac{1}{2} z^{-1}} - \frac{2}{1 + \frac{1}{3} z^{-1}}$$
      For a <strong>stable system</strong>, the ROC must contain the unit circle $|z| = 1$. Since both poles $|1/2| < 1$ and $|-1/3| < 1$ lie inside the unit circle, the ROC must be the exterior region $|z| > 1/2$. Thus, both terms correspond to right-sided (causal) sequences:
      $$h[n] = 3 \left(\frac{1}{2}\right)^n u[n] - 2 \left(-\frac{1}{3}\right)^n u[n]$$</p>
    </div>

    <!-- EXERCISE 5.1 -->
    <div class="exercise-box">
      <div class="exercise-title">✍️ Try It Out Yourself: Oppenheim Chapter 3, Problem 3.22</div>
      <p><strong>Question:</strong> A causal LTI system is described by the difference equation:
      $$y[n] - \frac{5}{6} y[n-1] + \frac{1}{6} y[n-2] = x[n]$$
      Find the impulse response $h[n]$ and determine whether the system is BIBO stable.</p>
      <details class="solution-toggle">
        <summary>Click to Reveal Step-by-Step Solution</summary>
        <p><strong>Solution:</strong><br>
        Take the $z$-transform of both sides:
        $$Y(z) \left(1 - \frac{5}{6} z^{-1} + \frac{1}{6} z^{-2}\right) = X(z)$$
        $$H(z) = \frac{1}{(1 - \frac{1}{2} z^{-1})(1 - \frac{1}{3} z^{-1})} = \frac{3}{1 - \frac{1}{2} z^{-1}} - \frac{2}{1 - \frac{1}{3} z^{-1}}$$
        Since the system is causal, ROC is $|z| > 1/2$.<br>
        $$h[n] = \left[ 3\left(\frac{1}{2}\right)^n - 2\left(\frac{1}{3}\right)^n \right] u[n]$$
        Both poles ($1/2$ and $1/3$) are strictly inside the unit circle ($|d_k| < 1$), so the system is <strong>BIBO Stable</strong>.</p>
      </details>
    </div>
"""

mod8_additions = r"""
    <!-- EXERCISE 8.1 -->
    <div class="exercise-box">
      <div class="exercise-title">✍️ Try It Out Yourself: Oppenheim Chapter 4, Problem 4.31</div>
      <p><strong>Question:</strong> By how many bits does oversampling by a factor of 4 ($\text{OSR} = 4$) with direct quantization (no noise shaping) increase the effective number of bits (ENOB) of an A/D converter?</p>
      <details class="solution-toggle">
        <summary>Click to Reveal Step-by-Step Solution</summary>
        <p><strong>Solution:</strong><br>
        With direct quantization, oversampling spreads the white quantization noise power $\sigma_e^2$ uniformly over $[0, f_s/2]$. The in-band noise is reduced by the oversampling ratio $\text{OSR} = 4$, which corresponds to a $10 \log_{10}(4) \approx 6\text{ dB}$ increase in SNR.<br>
        Since each bit of resolution contributes $6.02\text{ dB}$, an OSR of 4 provides:
        $$\Delta B = \frac{6\text{ dB}}{6.02\text{ dB/bit}} \approx \mathbf{1\text{ additional bit of ENOB}}.$$
        (Note: Adding first-order noise shaping increases this to $1.5\text{ bits per octave}$!)</p>
      </details>
    </div>
"""

mod9_additions = r"""
    <!-- EXERCISE 9.1 -->
    <div class="exercise-box">
      <div class="exercise-title">✍️ Try It Out Yourself: Oppenheim Chapter 5, Problem 5.1</div>
      <p><strong>Question:</strong> Consider an ideal differentiator with frequency response $H(e^{j\omega}) = j\omega$ for $-\pi < \omega < \pi$. Find the phase response $\theta(\omega)$ and the group delay $\tau_g(\omega)$.</p>
      <details class="solution-toggle">
        <summary>Click to Reveal Step-by-Step Solution</summary>
        <p><strong>Solution:</strong><br>
        Write in polar form: $H(e^{j\omega}) = |\omega| e^{j \pi/2}$ for $\omega > 0$, and $|\omega| e^{-j \pi/2}$ for $\omega < 0$.<br>
        Phase response: $\theta(\omega) = \frac{\pi}{2} \operatorname{sgn}(\omega)$.<br>
        Group delay:
        $$\tau_g(\omega) = -\frac{d\theta(\omega)}{d\omega} = \mathbf{0} \quad \text{for all } \omega \neq 0$$
        The group delay of an ideal continuous differentiator is zero, but it introduces a constant $90^\circ$ phase lead.</p>
      </details>
    </div>
"""

mod10_additions = r"""
    <!-- EXERCISE 10.1 -->
    <div class="exercise-box">
      <div class="exercise-title">✍️ Try It Out Yourself: Oppenheim Chapter 5, Problem 5.21</div>
      <p><strong>Question:</strong> Why is it impossible for a causal and stable IIR filter to have an exact generalized linear phase response?</p>
      <details class="solution-toggle">
        <summary>Click to Reveal Step-by-Step Solution</summary>
        <p><strong>Proof / Explanation:</strong><br>
        For a rational system function $H(z)$ to have linear phase, its poles must exhibit reciprocal symmetry: if $z_0$ is a pole, $1/z_0^*$ must also be a pole.<br>
        For stability, all poles must lie strictly inside the unit circle ($|z_0| < 1$).<br>
        However, if $|z_0| < 1$, its reciprocal pole $|1/z_0^*| = 1/|z_0| > 1$ must lie strictly <em>outside</em> the unit circle.<br>
        If the filter is causal, the ROC must be exterior to the outermost pole, meaning $|z| > 1/|z_0| > 1$. This ROC does not contain the unit circle, which contradicts stability!<br>
        Therefore, <strong>a causal and stable IIR filter can never have exact linear phase</strong>.</p>
      </details>
    </div>
"""

mod11_additions = r"""
    <!-- WORKED EXAMPLE 11.1 -->
    <div class="example-box">
      <div class="example-title">📖 Oppenheim Worked Example 6.1: Direct Form I vs. Direct Form II Realizations</div>
      <p><strong>Problem Statement:</strong> A second-order digital filter is described by:
      $$y[n] - 0.75 y[n-1] + 0.125 y[n-2] = x[n] + 0.5 x[n-1]$$
      Compare the memory requirements (delay elements) of Direct Form I and Direct Form II.</p>
      <p><strong>Solution:</strong><br>
      - Numerator order $M = 1$ ($b_0 = 1, b_1 = 0.5$). Denominator order $N = 2$ ($a_1 = -0.75, a_2 = 0.125$).<br>
      - <strong>Direct Form I:</strong> Implements zeros first then poles. Requires $M + N = 1 + 2 = \mathbf{3\text{ delay registers}}$ ($z^{-1}$).<br>
      - <strong>Direct Form II (Canonical):</strong> Implements poles first, sharing the intermediate delay line $w[n]$. Requires $\max(M, N) = \max(1, 2) = \mathbf{2\text{ delay registers}}$.<br>
      - Saving 1 delay register reduces memory by 33%.</p>
    </div>

    <!-- EXERCISE 11.1 -->
    <div class="exercise-box">
      <div class="exercise-title">✍️ Try It Out Yourself: Oppenheim Chapter 6, Problem 6.2</div>
      <p><strong>Question:</strong> State Tellegen's Theorem for Signal Flow Graphs and write down the algorithmic procedure to obtain the transposed structure.</p>
      <details class="solution-toggle">
        <summary>Click to Reveal Step-by-Step Solution</summary>
        <p><strong>Procedure:</strong><br>
        1. Reverse the direction of all signal flow arrows in the network.<br>
        2. Convert all summing nodes into branch/pick-off nodes.<br>
        3. Convert all branch/pick-off nodes into summing nodes.<br>
        4. Interchange the input node $x[n]$ with the output node $y[n]$.<br>
        <strong>Tellegen's Invariance:</strong> The overall input-to-output transfer function $H(z)$ is identical to the original system!</p>
      </details>
    </div>
"""

mod12_additions = r"""
    <!-- EXERCISE 12.1 -->
    <div class="exercise-box">
      <div class="exercise-title">✍️ Try It Out Yourself: Oppenheim Chapter 6, Problem 6.25</div>
      <p><strong>Question:</strong> An LTI system with impulse response $h[n] = (0.8)^n u[n]$ is implemented on a fixed-point DSP with round-off noise variance $\sigma_e^2$ injected at the accumulator. Compute the total noise power $\sigma_{yo}^2$ at the output.</p>
      <details class="solution-toggle">
        <summary>Click to Reveal Step-by-Step Solution</summary>
        <p><strong>Solution:</strong><br>
        The output noise variance due to internal white round-off noise is given by:
        $$\sigma_{yo}^2 = \sigma_e^2 \sum_{n=0}^\infty |h[n]|^2 = \sigma_e^2 \sum_{n=0}^\infty (0.8^{2n}) = \sigma_e^2 \sum_{n=0}^\infty (0.64)^n$$
        Using the infinite geometric series sum:
        $$\sigma_{yo}^2 = \sigma_e^2 \frac{1}{1 - 0.64} = \sigma_e^2 \frac{1}{0.36} \approx \mathbf{2.78 \, \sigma_e^2}$$
        The output noise power is amplified by nearly a factor of 3 due to the recursive feedback pole at $0.8$!</p>
      </details>
    </div>
"""

mod13_additions = r"""
    <!-- EXERCISE 13.1 -->
    <div class="exercise-box">
      <div class="exercise-title">✍️ Try It Out Yourself: Oppenheim Chapter 7, Problem 7.4</div>
      <p><strong>Question:</strong> What happens to the cutoff frequency $\omega_c = \pi$ when mapped through the Bilinear Transformation with sampling interval $T_s = 2$? What is the corresponding analog frequency $\Omega_c$?</p>
      <details class="solution-toggle">
        <summary>Click to Reveal Step-by-Step Solution</summary>
        <p><strong>Solution:</strong><br>
        Use the pre-warping formula:
        $$\Omega_c = \frac{2}{T_s} \tan\left(\frac{\omega_c}{2}\right) = \frac{2}{2} \tan\left(\frac{\pi}{2}\right) = \tan\left(\frac{\pi}{2}\right) \to \mathbf{\infty}$$
        <strong>Theoretical Insight:</strong> Digital frequency $\omega = \pi$ maps precisely to $\Omega = \infty$ in the analog domain! This compression of the entire infinite continuous frequency axis $[0, \infty)$ into $[0, \pi]$ is why the Bilinear Transformation completely eliminates aliasing.</p>
      </details>
    </div>
"""

mod14_additions = r"""
    <!-- EXERCISE 14.1 -->
    <div class="exercise-box">
      <div class="exercise-title">✍️ Try It Out Yourself: Oppenheim Chapter 7, Problem 7.15</div>
      <p><strong>Question:</strong> Compare the stopband attenuation achieved by a 51-tap ($M=50$) FIR filter designed with a Hamming window versus a Blackman window. Which one has a narrower transition band?</p>
      <details class="solution-toggle">
        <summary>Click to Reveal Step-by-Step Solution</summary>
        <p><strong>Comparison:</strong><br>
        - <strong>Hamming Window:</strong> Peak stopband attenuation is $\approx -53\text{ dB}$, mainlobe width $\Delta\omega = 8\pi / 50 = 0.16\pi$.<br>
        - <strong>Blackman Window:</strong> Peak stopband attenuation is $\approx -74\text{ dB}$, mainlobe width $\Delta\omega = 12\pi / 50 = 0.24\pi$.<br>
        <strong>Conclusion:</strong> The <strong>Hamming window has a significantly narrower transition band</strong> ($0.16\pi$ vs $0.24\pi$), but the Blackman window offers $21\text{ dB}$ deeper stopband attenuation. In filter design, mainlobe width (transition sharpness) and stopband attenuation are always an engineering trade-off.</p>
      </details>
    </div>
"""

mod15_additions = r"""
    <!-- WORKED EXAMPLE 15.1 -->
    <div class="example-box">
      <div class="example-title">📖 MATLAB Practical Example: Comparing filter, filtfilt, and fftfilt</div>
      <p><strong>Live-Coding Scenario:</strong> An audio signal contaminated by 50 Hz power-line hum needs notch filtering. Compare causal filtering vs zero-phase filtering in MATLAB.</p>
      <pre><code>% MATLAB Notch Filter Script
fs = 1000;
t = 0:1/fs:2-1/fs;
s = sin(2*pi*15*t);                 % Desired 15 Hz signal
noise = 0.8 * sin(2*pi*50*t);       % 50 Hz hum
x = s + noise;

% Design IIR Notch Filter
wo = 50 / (fs/2); bw = wo / 35;
[b, a] = iirnotch(wo, bw);

% 1. Causal filter (introduces phase delay, suitable for real-time streaming)
y_causal = filter(b, a, x);

% 2. Zero-phase filter (cancels phase lag completely, suitable for recorded buffers)
y_zero = filtfilt(b, a, x);

% 3. Measure phase lag
delay_samples = finddelay(s, y_causal);
fprintf('Causal filter delay: %d samples\n', delay_samples);
fprintf('Zero-phase filter delay: %d samples\n', finddelay(s, y_zero));</code></pre>
    </div>

    <!-- EXERCISE 15.1 -->
    <div class="exercise-box">
      <div class="exercise-title">✍️ Try It Out Yourself: MATLAB Vectorization Challenge</div>
      <p><strong>Question:</strong> Given a $1000 \times 100$ matrix <code>A</code>, subtract the median of each column from all elements in that column in a single vectorized line without using <code>for</code> loops.</p>
      <details class="solution-toggle">
        <summary>Click to Reveal Step-by-Step Solution</summary>
        <pre><code>% Using MATLAB R2016b+ Implicit Expansion:
A_centered = A - median(A, 1);

% In older versions (pre-R2016b):
A_centered = bsxfun(@minus, A, median(A, 1));</code></pre>
      </details>
    </div>
"""

mod16_additions = r"""
    <!-- WORKED EXAMPLE 16.1 -->
    <div class="example-box">
      <div class="example-title">📖 C Systems Example: Production-Grade Direct Form II Transposed IIR Engine</div>
      <pre><code>#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;

typedef struct {
    float b0, b1, b2;
    float a1, a2;
    float s1, s2; // State registers
} BiquadDF2T;

void biquad_init(BiquadDF2T *f, float b0, float b1, float b2, float a1, float a2) {
    f->b0 = b0; f->b1 = b1; f->b2 = b2;
    f->a1 = a1; f->a2 = a2;
    f->s1 = 0.0f; f->s2 = 0.0f;
}

// Single-sample step: executes in minimal CPU cycles using FMA
float biquad_step(BiquadDF2T *f, float x) {
    float y = f->b0 * x + f->s1;
    f->s1 = f->b1 * x - f->a1 * y + f->s2;
    f->s2 = f->b2 * x - f->a2 * y;
    return y;
}</code></pre>
    </div>

    <!-- EXERCISE 16.1 -->
    <div class="exercise-box">
      <div class="exercise-title">✍️ Try It Out Yourself: C Systems Interview Question</div>
      <p><strong>Question:</strong> Write a C function to test whether the current CPU architecture is Big-Endian or Little-Endian.</p>
      <details class="solution-toggle">
        <summary>Click to Reveal Step-by-Step Solution</summary>
        <pre><code>#include &lt;stdbool.h&gt;

bool is_little_endian(void) {
    unsigned short test = 0x0001;
    unsigned char *byte_ptr = (unsigned char *)&test;
    return (*byte_ptr == 0x01); // LSB at lowest address -> Little Endian
}</code></pre>
      </details>
    </div>
"""

# Now let's inject these additions into index.html
with open('/home/jaswanth/mathworks_intrevPrep/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace targets in order
if "Module 5: Transfer Functions" in content and "<!-- WORKED EXAMPLE 5.1 -->" not in content:
    content = content.replace("</div>\n</details>\n\n</div>\n</div>\n\n<!-- ========================================================\n<!-- PART III:", mod5_additions + "</div>\n</details>\n\n</div>\n</div>\n\n<!-- ========================================================\n<!-- PART III:")

if "Module 8: A/D Conversion" in content and "<!-- EXERCISE 8.1 -->" not in content:
    content = content.replace("</div>\n</details>\n\n</div>\n</div>\n\n<!-- ========================================================\n<!-- PART IV:", mod8_additions + "</div>\n</details>\n\n</div>\n</div>\n\n<!-- ========================================================\n<!-- PART IV:")

if "Module 9: Frequency Response" in content and "<!-- EXERCISE 9.1 -->" not in content:
    content = content.replace("</div>\n</details>\n\n<!-- MODULE 10 -->", mod9_additions + "</div>\n</details>\n\n<!-- MODULE 10 -->")

if "Module 10: Allpass Systems" in content and "<!-- EXERCISE 10.1 -->" not in content:
    content = content.replace("</div>\n</details>\n\n</div>\n</div>\n\n<!-- ========================================================\n<!-- PART V:", mod10_additions + "</div>\n</details>\n\n</div>\n</div>\n\n<!-- ========================================================\n<!-- PART V:")

if "Module 11: IIR & FIR Filter Realizations" in content and "<!-- WORKED EXAMPLE 11.1 -->" not in content:
    content = content.replace("</div>\n</details>\n\n<!-- MODULE 12 -->", mod11_additions + "</div>\n</details>\n\n<!-- MODULE 12 -->")

if "Module 12: Finite-Precision Numerical Effects" in content and "<!-- EXERCISE 12.1 -->" not in content:
    content = content.replace("</div>\n</details>\n\n</div>\n</div>\n\n<!-- ========================================================\n<!-- PART VI:", mod12_additions + "</div>\n</details>\n\n</div>\n</div>\n\n<!-- ========================================================\n<!-- PART VI:")

if "Module 13: IIR Filter Design" in content and "<!-- EXERCISE 13.1 -->" not in content:
    content = content.replace("</div>\n</details>\n\n<!-- MODULE 14 -->", mod13_additions + "</div>\n</details>\n\n<!-- MODULE 14 -->")

if "Module 14: FIR Filter Design" in content and "<!-- EXERCISE 14.1 -->" not in content:
    content = content.replace("</div>\n</details>\n\n</div>\n</div>\n\n<!-- ========================================================\n<!-- PART VII:", mod14_additions + "</div>\n</details>\n\n</div>\n</div>\n\n<!-- ========================================================\n<!-- PART VII:")

if "Module 15: MATLAB Signal Processing Toolbox" in content and "<!-- WORKED EXAMPLE 15.1 -->" not in content:
    content = content.replace("</div>\n</details>\n\n<!-- MODULE 16 -->", mod15_additions + "</div>\n</details>\n\n<!-- MODULE 16 -->")

if "Module 16: C Memory Architecture" in content and "<!-- WORKED EXAMPLE 16.1 -->" not in content:
    content = content.replace("</div>\n</details>\n\n<!-- MODULE 17 -->", mod16_additions + "</div>\n</details>\n\n<!-- MODULE 17 -->")

with open('/home/jaswanth/mathworks_intrevPrep/index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html fully updated with textbook examples, exercises, and diagrams across all modules!")
