# C Programming & DSA Cheatsheet for MathWorks EDG

---

## 1. Fast Pointer & Memory Syntax

```c
// Pointer declarations:
int *p;             // Pointer to int
int **pp;           // Pointer to pointer to int
int *arr[10];       // Array of 10 pointers to int
int (*parr)[10];    // Pointer to array of 10 ints
int (*fn)(int, int);// Pointer to function taking 2 ints and returning int

// Memory allocation best practice:
float *buf = (float *)malloc(n * sizeof(*buf));
if (!buf) { /* Error handling */ }
// Always free and set to NULL to prevent dangling pointers:
free(buf);
buf = NULL;
```

---

## 2. Essential Bit Manipulation Quick Reference

| Goal | Bitwise Expression | Explanation |
| :--- | :--- | :--- |
| **Check Power of 2** | `(n > 0) && !(n & (n - 1))` | Removes lowest set bit |
| **Get $k$-th bit** | `(n >> k) & 1` | Shifts target bit to LSB |
| **Set $k$-th bit** | `n \| (1U << k)` | Bitwise OR with mask |
| **Clear $k$-th bit** | `n & ~(1U << k)` | Bitwise AND with inverted mask |
| **Toggle $k$-th bit** | `n ^ (1U << k)` | Bitwise XOR with mask |
| **Extract lowest set bit** | `n & (-n)` | Two's complement property |
| **Multiply by $2^k$** | `n << k` | Left shift |
| **Divide by $2^k$** | `n >> k` | Right shift (unsigned/non-negative) |

---

## 3. Core DSA Complexity Matrix

| Data Structure / Algorithm | Access | Search | Insertion | Deletion | Space |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Array** | $O(1)$ | $O(N)$ | $O(N)$ | $O(N)$ | $O(N)$ |
| **Circular Buffer** | $O(1)$ | $O(N)$ | $O(1)$ | $O(1)$ | $O(K)$ |
| **Singly Linked List** | $O(N)$ | $O(N)$ | $O(1)$ (at head) | $O(1)$ (with node) | $O(N)$ |
| **Binary Search Tree (Balanced)** | $O(\log N)$ | $O(\log N)$ | $O(\log N)$ | $O(\log N)$ | $O(N)$ |
| **Hash Table** | - | $O(1)$ avg | $O(1)$ avg | $O(1)$ avg | $O(N)$ |
| **Binary Search** | - | $O(\log N)$ | - | - | $O(1)$ |
| **Merge Sort** | - | - | - | - | Time: $O(N \log N)$, Space: $O(N)$ |
| **Quick Sort (In-Place)** | - | - | - | - | Time: $O(N \log N)$ avg, Space: $O(\log N)$ |

---

## 4. Top C Interview Edge Cases MathWorks Checks

1. **Null Pointer Dereference:** Always check `if (ptr == NULL)` before accessing!
2. **Buffer Overflow & Off-By-One:** Loop conditions `<= N` vs `< N`, array indices $0$ to $N-1$.
3. **Memory Leaks:** Every `malloc` / `calloc` / `realloc` must have a corresponding `free`.
4. **Integer Overflow:** In convolution accumulations and sample index arithmetic, cast to `int64_t` or `double` to prevent wrap-around.
5. **Dangling Pointers:** Freeing a pointer without setting it to `NULL` leaves a pointer to deallocated memory.
