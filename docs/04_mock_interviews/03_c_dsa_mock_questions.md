# MathWorks EDG Mock Interview Questions: C Programming & DSA

---

### Question 1: Circular Streaming Buffer for DSP Data Stream
**Interviewer:**  
"In a real-time DSP audio processing system, incoming samples arrive one by one from an ADC interrupt. Design and implement a C data structure for a Circular Ring Buffer of fixed capacity $K$. Provide functions to `push` a sample, `get_latest`, and handle buffer wrap-around without copying elements. What is the time complexity of push and read?"

#### Model Answer:
```c
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    float *data;
    size_t capacity;
    size_t head;    // Points to next insertion slot
    size_t count;   // Current number of elements stored (up to capacity)
} RingBuffer;

RingBuffer* ring_buffer_init(size_t capacity) {
    if (capacity == 0) return NULL;
    RingBuffer *rb = (RingBuffer *)malloc(sizeof(RingBuffer));
    if (!rb) return NULL;

    rb->data = (float *)malloc(capacity * sizeof(float));
    if (!rb->data) {
        free(rb);
        return NULL;
    }
    rb->capacity = capacity;
    rb->head = 0;
    rb->count = 0;
    return rb;
}

// Push new sample: O(1) time
void ring_buffer_push(RingBuffer *rb, float sample) {
    rb->data[rb->head] = sample;
    rb->head = (rb->head + 1) % rb->capacity;
    if (rb->count < rb->capacity) {
        rb->count++;
    }
}

// Get sample at offset from newest (0 = newest, 1 = second newest): O(1) time
bool ring_buffer_get_latest(const RingBuffer *rb, size_t offset, float *out_val) {
    if (!rb || offset >= rb->count) return false;
    
    // Calculate physical index backwards from head
    // head points to next write slot, so (head - 1) is the newest sample
    size_t index = (rb->head + rb->capacity - 1 - offset) % rb->capacity;
    *out_val = rb->data[index];
    return true;
}

void ring_buffer_free(RingBuffer *rb) {
    if (rb) {
        free(rb->data);
        free(rb);
    }
}
```
* **Follow-Up (MathWorks Optimization):** "How can you eliminate the expensive modulo `%` operator inside an inner interrupt loop if $K$ is a power of 2?"
* *Answer:* If $K = 2^M$, `index % K` can be replaced with the bitwise AND: `index & (K - 1)`. This is a single-cycle CPU operation!

---

### Question 2: Memory Leak & Pointer Debugging
**Interviewer:**  
"Find all bugs, memory leaks, and undefined behaviors in the following C code snippet:"
```c
void process_signals() {
    int *buffer = (int *)malloc(10 * sizeof(int));
    for (int i = 0; i <= 10; i++) {
        buffer[i] = i * 2;
    }
    int *copy = buffer;
    free(buffer);
    printf("First element: %d\n", *copy);
}
```

#### Model Answer:
1. **Off-by-One Buffer Overflow (Heap Corruption):**
   * The loop condition `i <= 10` executes 11 iterations ($i = 0, \dots, 10$).
   * Array size is only 10 elements (valid indices $0$ to $9$). Writing to `buffer[10]` writes past allocated heap boundaries, causing undefined behavior / memory corruption.
2. **Missing `NULL` Check on `malloc`:**
   * If `malloc` fails and returns `NULL`, accessing `buffer[i]` triggers a segmentation fault (Null pointer dereference).
3. **Use-After-Free (Dangling Pointer):**
   * `copy` points to the same heap block as `buffer`.
   * `free(buffer)` deallocates the block back to the operating system / runtime.
   * Accessing `*copy` on the very next line is a classic **Use-After-Free** undefined behavior. The memory might be recycled or cause a crash.

---

### Question 3: 2D Matrix Rotation In-Place (Clockwise 90°)
**Interviewer:**  
"Given an $N \times N$ 2D matrix representing an image or 2D FIR filter mask, rotate it 90 degrees clockwise in-place with $O(1)$ extra space."

#### Model Answer:
```c
void rotate_in_place(int n, int matrix[n][n]) {
    // Step 1: Transpose matrix along main diagonal
    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            int temp = matrix[i][j];
            matrix[i][j] = matrix[j][i];
            matrix[j][i] = temp;
        }
    }

    // Step 2: Reverse each row horizontally
    for (int i = 0; i < n; ++i) {
        int left = 0;
        int right = n - 1;
        while (left < right) {
            int temp = matrix[i][left];
            matrix[i][left] = matrix[i][right];
            matrix[i][right] = temp;
            left++;
            right--;
        }
    }
}
```
* **Complexity:** Time complexity is $O(N^2)$ to visit all elements. Auxiliary space is $O(1)$ since all swaps occur in-place.
