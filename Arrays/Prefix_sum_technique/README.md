# Prefix sum techniques

```markdown

# Prefix Sum

## Overview

The **Prefix Sum** technique involves preprocessing an array to create a new array where each element at index `i` represents the sum of the array from the start up to `i`. This enables efficient queries for the sum of elements in a specific range of the array.

## When to Use

Use Prefix Sum when:
- You need to perform multiple queries to find the sum of subarrays.
- You need cumulative sums for calculations or comparisons.

## How It Works

1. **Preprocessing**:
   Create a prefix sum array `P` such that:
   \[
   P[i] = \text{nums}[0] + \text{nums}[1] + \ldots + \text{nums}[i]
   \]

2. **Range Sum Query**:
   To find the sum of elements from index `i` to `j` in the original array:
   \[
   \text{Sum}[i:j] = P[j] - P[i-1]
   \]
   For \(i = 0\), simply use \(P[j]\) since \(P[-1]\) is undefined.

---

## Example

### Problem

Given an array `nums`, find the sum of elements in a subarray defined by indices `i` and `j`.

#### Input:
```plaintext
nums = [1, 2, 3, 4, 5, 6]
i = 1
j = 3
```

## Solution

1. Preprocess `nums` to compute the prefix sum array `P`:
   \[
   P = [1, 3, 6, 10, 15, 21]
   \]

2. Use the formula:
   \[
   \text{Sum}[i:j] = P[j] - P[i-1]
   \]
   For \(i = 1, j = 3\):
   \[
   \text{Sum}[1:3] = P[3] - P[0] = 10 - 1 = 9
   \]

### Output

```plaintext
9
```

---

## Applications

Prefix Sum is commonly used in problems requiring:

- Subarray sums
- Cumulative frequency counts
- Range-based queries

### Example Problems

1. **Range Sum Query - Immutable** ([LeetCode #303](https://leetcode.com/problems/range-sum-query-immutable))  
   Precompute a prefix sum array for efficient sum queries.

2. **Contiguous Array** ([LeetCode #525](https://leetcode.com/problems/contiguous-array))  
   Use prefix sums to track differences in counts for binary arrays.

3. **Subarray Sum Equals K** ([LeetCode #560](https://leetcode.com/problems/subarray-sum-equals-k))  
   Leverage prefix sums and a hash map to find subarrays that sum to a given value \(k\).

---

## Advantages

- **Efficient Range Queries**: Once the prefix sum array is built, range sum queries are \(O(1)\).
- **Simple to Implement**: Minimal preprocessing logic is required.

---

## Code Example

Here's an implementation of the Prefix Sum technique in Python:

```python
class NumArray:
    def __init__(self, nums):
        # Precompute prefix sums
        self.prefix_sums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix_sums[i + 1] = self.prefix_sums[i] + nums[i]

    def sumRange(self, left, right):
        # Calculate the sum using the prefix sum array
        return self.prefix_sums[right + 1] - self.prefix_sums[left]


# Example Usage
nums = [1, 2, 3, 4, 5, 6]
numArray = NumArray(nums)
print(numArray.sumRange(1, 3))  # Output: 9
```

---

## Resources

- [Introduction to Prefix Sum on GeeksforGeeks](https://www.geeksforgeeks.org/prefix-sum-array-implementation-applications-competitive-programming/)
- [LeetCode Discuss: Prefix Sum Techniques](https://blog.algomaster.io/p/15-leetcode-patterns)
