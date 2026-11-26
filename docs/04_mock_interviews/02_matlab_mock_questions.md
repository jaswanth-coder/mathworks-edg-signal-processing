# MathWorks EDG Mock Interview Questions: MATLAB Signal Processing & Algorithms

---

### Question 1: In-Place Peak Detection with Constraints
**Interviewer:**  
"Suppose you have a 1D vector `x` representing a noisy sensor signal. Without using the Signal Processing Toolbox function `findpeaks`, write a clean MATLAB function that returns the indices and values of all local peaks. A peak is defined as a point that is strictly greater than both its immediate neighbors and exceeds a specified amplitude threshold `T`. What is the time complexity?"

#### Model Answer:
```matlab
function [peak_indices, peak_values] = my_findpeaks(x, T)
    % Ensure column or row vector consistency
    x = x(:).'; 
    N = length(x);
    
    if N < 3
        peak_indices = [];
        peak_values = [];
        return;
    end
    
    % Fully vectorized implementation:
    % Peak condition: x(i) > x(i-1) AND x(i) > x(i+1) AND x(i) >= T
    % We slice the interior elements [2 to N-1]
    is_greater_than_left  = x(2:N-1) > x(1:N-2);
    is_greater_than_right = x(2:N-1) > x(3:N);
    is_above_thresh       = x(2:N-1) >= T;
    
    % Boolean mask for interior peaks
    peak_mask = is_greater_than_left & is_greater_than_right & is_above_thresh;
    
    % Extract indices (shift index by +1 because interior starts at index 2)
    peak_indices = find(peak_mask) + 1;
    peak_values  = x(peak_indices);
end
```
* **Complexity:** Time complexity is $O(N)$ because slicing and logical vector comparisons run in single linear scans. Space complexity is $O(N)$ for masks.
* **MathWorks Follow-Up:** "What if the signal contains flat plateaus (e.g., `[1, 3, 3, 3, 1]`)? How would your algorithm adapt?"
* *Follow-Up Answer:* Standard `x(2:N-1) > x(3:N)` fails on flat tops. We must run a run-length compression pass or state-machine loop that tracks the start of a plateau and checks if the signal drops on the other side, marking the center of the plateau as the peak index.

---

### Question 2: Zero-Phase Filtering (`filter` vs `filtfilt`)
**Interviewer:**  
"If I filter an audio signal with `filter(b, a, x)`, listen to it, and compare it with `filtfilt(b, a, x)`, what differences will I hear? Why does `filtfilt` fail in a live streaming system?"

#### Model Answer:
1. **Auditory & Waveform Difference:**
   * `filter(b, a, x)` introduces frequency-dependent phase distortion and a time delay. Transients (like drum beats) will be slightly smeared or delayed.
   * `filtfilt(b, a, x)` has exactly zero phase delay ($\angle H(\omega) = 0$). All frequency components remain perfectly aligned in time.
   * However, `filtfilt` squares the magnitude response: $|H_{\text{eff}}(e^{j\omega})| = |H(e^{j\omega})|^2$. So a filter with $-3\text{ dB}$ attenuation at cutoff will produce $-6\text{ dB}$ attenuation when passed through `filtfilt`.
2. **Why it fails in live streaming:**
   * `filtfilt` requires processing the signal forward, reversing the entire time sequence, filtering in reverse, and reversing again.
   * Reversing time requires access to future samples up to the end of the signal (non-causal). In a live microphone or radar stream, future samples do not yet exist! Therefore, `filtfilt` can only run on finite, pre-recorded buffers (offline processing).

---

### Question 3: Matrix Vectorization Challenge
**Interviewer:**  
"Given an $M \times N$ matrix $A$, replace all elements that are strictly less than the mean of their respective column with $0$. Do this in one vectorized line without `for` loops."

#### Model Answer:
```matlab
% Column-wise mean using implicit expansion (MATLAB R2016b+):
col_means = mean(A, 1);     % 1 x N row vector of column means
A(A < col_means) = 0;       % Implicitly expands col_means across rows of A!
```
* *MathWorks Note:* Interviewers look for knowledge of **implicit expansion** (introduced in MATLAB R2016b) which replaced `bsxfun(@lt, A, mean(A, 1))`. Mentioning both shows mastery across MATLAB versions!

---

### Question 4: FFT Leakage & Windowing
**Interviewer:**  
"I take the 1024-point FFT of a pure sine wave, but instead of seeing a single sharp spike, I see energy smeared across multiple neighboring bins. What is this phenomenon called, why does it occur, and how do you mitigate it?"

#### Model Answer:
1. **Name:** **Spectral Leakage**.
2. **Underlying Cause:**
   * Computing an $N$-point DFT is mathematically equivalent to taking the continuous DTFT of an infinite signal multiplied by a **rectangular window** of length $N$.
   * Multiplication in time equals convolution in frequency: the true line spectrum $\delta(f - f_0)$ is convolved with the frequency response of the rectangular window, which is a $\operatorname{sinc}$ function with high sidelobes ($-13\text{ dB}$).
   * If the sine wave's frequency $f_0$ does not fall *exactly* on an integer FFT bin ($f_0 \neq k \frac{f_s}{N}$), the non-zero sidelobes of the sinc function sample across all neighboring bins.
3. **Mitigation:**
   * Apply a smooth tapering window (e.g., **Hamming, Hann, Blackman, or Kaiser**) before computing the FFT:
     `X = fft(x .* hann(length(x)).');`
   * Windows smoothly taper the signal to zero at boundaries, dramatically suppressing sidelobes (e.g., Hann achieves $-31\text{ dB}$, Blackman achieves $-58\text{ dB}$), at the cost of a slightly wider mainlobe.
