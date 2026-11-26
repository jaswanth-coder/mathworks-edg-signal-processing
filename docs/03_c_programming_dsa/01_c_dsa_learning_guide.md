# C Programming & Data Structures Mastery Guide
### Tailored for MathWorks EDG (Signal Processing & Embedded Software Track)

---

## 1. C Memory Architecture, Pointers & System Fundamentals

### 1.1 Memory Segments in a C Program
Understanding memory layout is fundamental to answering MathWorks systems questions:
* **Text Segment:** Compiled machine instructions (read-only).
* **Data Segment:** Initialized global and static variables.
* **BSS Segment (Block Started by Symbol):** Uninitialized global and static variables (zero-initialized by kernel before `main`).
* **Heap:** Dynamically allocated memory (`malloc`, `calloc`, `realloc`), grows upward toward high addresses.
* **Stack:** Function call frames, local variables, return addresses, grows downward toward low addresses.

### 1.2 Pointers, Double Pointers & Function Pointers
```c
#include <stdio.h>
#include <stdlib.h>

// 1. Pointer Arithmetic
int arr[5] = {10, 20, 30, 40, 50};
int *p = arr;
int val = *(p + 2); // 30 (increments address by 2 * sizeof(int))

// 2. Modifying a pointer inside a function requires a double pointer (or returning the pointer):
void allocate_signal_buffer(float **buf, size_t size) {
    *buf = (float *)malloc(size * sizeof(float));
    if (*buf == NULL) {
        // Handle allocation failure! Always check in interviews!
        fprintf(stderr, "Out of memory!\n");
        exit(EXIT_FAILURE);
    }
}

// 3. Function Pointers (Used for callback architectures & DSP pipelines):
typedef float (*sample_processor_fn)(float);

float apply_gain(float in) { return in * 2.5f; }

void process_stream(float *buffer, size_t len, sample_processor_fn func) {
    for (size_t i = 0; i < len; ++i) {
        buffer[i] = func(buffer[i]);
    }
}
```

### 1.3 `volatile`, `const`, `static`, and Struct Padding
* **`volatile`:** Tells the compiler NOT to optimize away reads/writes to this variable, because its value can change outside program flow (e.g., hardware ADC register, DMA transfer buffer, or ISR interrupt flag).
* **`static`:**
  * Inside function: Preserves value between function calls (allocated in Data/BSS segment, not stack).
  * Global file scope: Restricts symbol linkage to the current translation unit (.c file).
* **Structure Padding & Memory Alignment:**
  ```c
  struct SampleBad {
      char status;     // 1 byte
      // 3 padding bytes inserted here to align double on 4/8-byte boundary!
      int timestamp;   // 4 bytes
      char channel;    // 1 byte
      // 3 padding bytes
  }; // sizeof = 12 bytes!

  struct SampleGood {
      int timestamp;   // 4 bytes
      char status;     // 1 byte
      char channel;    // 1 byte
      // 2 padding bytes
  }; // sizeof = 8 bytes! (Save memory by ordering largest members first)
  ```

### 1.4 Bit Manipulation (High-Yield MathWorks Questions)
```c
#include <stdbool.h>

// Check if integer is power of 2 (crucial for FFT size check!):
bool is_power_of_two(unsigned int n) {
    return (n > 0) && ((n & (n - 1)) == 0);
}

// Bit reversal for Radix-2 FFT (32-bit):
unsigned int reverse_bits(unsigned int n, unsigned int num_bits) {
    unsigned int rev = 0;
    for (unsigned int i = 0; i < num_bits; ++i) {
        if (n & (1 << i)) {
            rev |= (1 << (num_bits - 1 - i));
        }
    }
    return rev;
}

// Endianness Check:
bool is_little_endian(void) {
    unsigned short x = 0x0001;
    return *((unsigned char *)&x) == 0x01;
}
```

---

## 2. Low-Level DSP Algorithms in C

### 2.1 1D Linear Convolution in C
```c
#include <stdlib.h>

/**
 * Linear convolution: y = x * h
 * len_y = len_x + len_h - 1
 */
float* convolve_1d(const float *x, size_t len_x, const float *h, size_t len_h, size_t *len_y) {
    if (!x || !h || len_x == 0 || len_h == 0) return NULL;
    
    *len_y = len_x + len_h - 1;
    float *y = (float *)calloc(*len_y, sizeof(float));
    if (!y) return NULL;

    for (size_t n = 0; n < *len_y; ++n) {
        float sum = 0.0f;
        size_t k_min = (n >= len_h - 1) ? n - (len_h - 1) : 0;
        size_t k_max = (n < len_x - 1) ? n : len_x - 1;

        for (size_t k = k_min; k <= k_max; ++k) {
            sum += x[k] * h[n - k];
        }
        y[n] = sum;
    }
    return y;
}
```

### 2.2 Circular Buffer (Ring Buffer) for O(1) Moving Average Filter
A classic MathWorks live-coding favorite: implement a moving average filter on streaming data without re-summing $N$ items each time.
```c
#include <stdlib.h>

typedef struct {
    float *buffer;
    size_t capacity;
    size_t head;
    size_t count;
    double running_sum;
} MovingAverageFilter;

MovingAverageFilter* movavg_create(size_t window_size) {
    MovingAverageFilter *filter = (MovingAverageFilter *)malloc(sizeof(MovingAverageFilter));
    if (!filter) return NULL;
    filter->buffer = (float *)calloc(window_size, sizeof(float));
    if (!filter->buffer) {
        free(filter);
        return NULL;
    }
    filter->capacity = window_size;
    filter->head = 0;
    filter->count = 0;
    filter->running_sum = 0.0;
    return filter;
}

float movavg_update(MovingAverageFilter *f, float new_sample) {
    // Subtract oldest sample that will be overwritten
    f->running_sum -= f->buffer[f->head];
    
    // Insert new sample
    f->buffer[f->head] = new_sample;
    f->running_sum += new_sample;
    
    // Advance circular pointer
    f->head = (f->head + 1) % f->capacity;
    if (f->count < f->capacity) {
        f->count++;
    }
    
    return (float)(f->running_sum / f->count);
}

void movavg_destroy(MovingAverageFilter *f) {
    if (f) {
        free(f->buffer);
        free(f);
    }
}
```

### 2.3 Direct Form II Transposed IIR/FIR Filter Engine
```c
#include <stdlib.h>

/**
 * y[n] = b0*x[n] + d1[n-1]
 * d1[n] = b1*x[n] - a1*y[n] + d2[n-1]
 * ...
 */
typedef struct {
    const float *b;  // Numerator coefficients [M+1]
    const float *a;  // Denominator coefficients [N+1] (a[0] normalized to 1.0)
    size_t num_order;
    size_t den_order;
    size_t num_states; // max(num_order, den_order)
    float *state;      // Delay registers
} DF2T_Filter;

DF2T_Filter* df2t_create(const float *b, size_t num_order, const float *a, size_t den_order) {
    DF2T_Filter *f = (DF2T_Filter *)malloc(sizeof(DF2T_Filter));
    f->b = b;
    f->a = a;
    f->num_order = num_order;
    f->den_order = den_order;
    f->num_states = (num_order > den_order) ? num_order : den_order;
    f->state = (float *)calloc(f->num_states, sizeof(float));
    return f;
}

float df2t_step(DF2T_Filter *f, float x) {
    float y = f->b[0] * x + (f->num_states > 0 ? f->state[0] : 0.0f);
    
    for (size_t i = 0; i < f->num_states; ++i) {
        float bi = (i + 1 <= f->num_order) ? f->b[i + 1] : 0.0f;
        float ai = (i + 1 <= f->den_order) ? f->a[i + 1] : 0.0f;
        float next_state = (i + 1 < f->num_states) ? f->state[i + 1] : 0.0f;
        
        f->state[i] = bi * x - ai * y + next_state;
    }
    return y;
}
```

### 2.4 1D Peak Detection (Local Maxima with Plateau Handling)
```c
#include <stdio.h>
#include <stdlib.h>

/**
 * Finds indices of local peaks where signal[i] > signal[i-1] and signal[i] >= signal[i+1]
 * with plateau resolution and minimum threshold.
 */
int* find_peaks_1d(const float *sig, size_t n, float min_height, size_t *num_peaks) {
    if (!sig || n < 3) {
        *num_peaks = 0;
        return NULL;
    }

    int *peaks = (int *)malloc(n * sizeof(int));
    size_t count = 0;

    size_t i = 1;
    while (i < n - 1) {
        if (sig[i] > sig[i - 1] && sig[i] >= min_height) {
            size_t j = i;
            // Handle flat plateaus
            while (j < n - 1 && sig[j] == sig[j + 1]) {
                j++;
            }
            if (j < n - 1 && sig[j] > sig[j + 1]) {
                // Peak is midpoint of plateau
                peaks[count++] = (int)((i + j) / 2);
            }
            i = j + 1;
        } else {
            i++;
        }
    }

    *num_peaks = count;
    return peaks;
}
```

### 2.5 Numerical Integration (Trapezoidal Rule) in C
```c
/**
 * Integral of y over x using Trapezoidal rule
 */
double trapezoidal_integral(const double *x, const double *y, size_t n) {
    if (!x || !y || n < 2) return 0.0;
    double area = 0.0;
    for (size_t i = 0; i < n - 1; ++i) {
        double dx = x[i + 1] - x[i];
        double avg_h = (y[i] + y[i + 1]) / 2.0;
        area += dx * avg_h;
    }
    return area;
}
```

### 2.6 Fixed-Point Arithmetic & Saturation (Q15 Format)
In digital signal processors, overflow causes disastrous negative wrap-around (loud pop in audio). Saturation clamps to min/max.
```c
#include <stdint.h>

// Q15 fixed point format: 1 sign bit, 15 fractional bits. Range [-1.0, 1.0 - 2^-15]
typedef int16_t q15_t;

// Saturating Addition:
q15_t q15_add_sat(q15_t a, q15_t b) {
    int32_t sum = (int32_t)a + (int32_t)b;
    if (sum > 32767) return 32767;
    if (sum < -32768) return -32768;
    return (q15_t)sum;
}

// Q15 Multiplication:
q15_t q15_mul(q15_t a, q15_t b) {
    int32_t prod = ((int32_t)a * (int32_t)b) >> 15;
    if (prod > 32767) return 32767;
    if (prod < -32768) return -32768;
    return (q15_t)prod;
}
```

---

## 3. High-Yield Data Structures & Algorithms for MathWorks EDG

### 3.1 Matrix In-Place 90-Degree Rotation (LeetCode 48)
```c
void rotate_matrix_90_clockwise(int **matrix, int n) {
    // Step 1: Transpose matrix in-place
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            int tmp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = tmp;
        }
    }
    // Step 2: Reverse each row
    for (int i = 0; i < n; ++i) {
        int left = 0, right = n - 1;
        while (left < right) {
            int tmp = matrix[i][left];
            matrix[i][left] = matrix[i][right];
            matrix[i][right] = tmp;
            left++;
            right--;
        }
    }
}
```

### 3.2 Find Peak Element in $O(\log N)$ Time (LeetCode 162)
```c
int findPeakElement(int* nums, int numsSize) {
    int left = 0, right = numsSize - 1;
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (nums[mid] > nums[mid + 1]) {
            // Downward slope: peak must be to the left (including mid)
            right = mid;
        } else {
            // Upward slope: peak must be to the right
            left = mid + 1;
        }
    }
    return left;
}
```

### 3.3 Reverse Singly Linked List In-Place (Classic Interview Screening)
```c
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* reverseList(struct ListNode* head) {
    struct ListNode *prev = NULL;
    struct ListNode *curr = head;
    while (curr != NULL) {
        struct ListNode *next_node = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next_node;
    }
    return prev;
}
```
