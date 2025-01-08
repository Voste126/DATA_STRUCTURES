# DATA STRUCTURES

```markdown
# Array Problems - Learning Data Structures

Welcome to my journey of mastering data structures! This repository contains solutions and explanations for some classic array problems, categorized by difficulty level. Dive in, explore, and learn along with me!

---

## Simple Problem - Two Sum

**Problem:**  
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.  

**Constraints:**
- Each input has exactly one solution.
- You may not use the same element twice.
- The solution can be returned in any order.

### Example:
```plaintext
Input: nums = [2,7,11,15], target = 9  
Output: [0,1]  
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```

```plaintext
Input: nums = [3,2,4], target = 6  
Output: [1,2]

Input: nums = [3,3], target = 6  
Output: [0,1]
```

**Constraints:**

- `2 <= nums.length <= 10⁴`
- `-10⁹ <= nums[i] <= 10⁹`
- `-10⁹ <= target <= 10⁹`
- Only one valid answer exists.

---

## Intermediate Problem - Container with Most Water

**Problem:**  
You are given an integer array `height` of length `n`, representing the heights of vertical lines drawn on the x-axis. Find two lines that, together with the x-axis, form a container that holds the maximum amount of water.  

### Example

```plaintext
Input: height = [1,8,6,2,5,4,8,3,7]  
Output: 49  
Explanation: The lines at indices 1 and 8 form the container with the most water (49 units).
```

### Additional Test Cases 1

```plaintext
Input: height = [1,1]  
Output: 1
```

**Constraints:**

- `n == height.length`
- `2 <= n <= 10⁵`
- `0 <= height[i] <= 10⁴`

---

## Hard Problem - Trapping Rain Water

**Problem:**  
Given `n` non-negative integers representing an elevation map, where the width of each bar is 1, compute how much water it can trap after raining.

### Example 2

```plaintext
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]  
Output: 6  
Explanation: The elevation map can trap 6 units of rainwater between the bars.
```

### Additional Test Cases 2

```plaintext
Input: height = [4,2,0,3,2,5]  
Output: 9
```

**Constraints:**

- `n == height.length`
- `1 <= n <= 2 * 10⁴`
- `0 <= height[i] <= 10⁵`

---

## Why These Problems?

These problems are classic examples of array manipulation, testing your ability to think critically about space, time complexity, and edge cases. By solving these, you will strengthen your fundamentals in:

- Index-based operations
- Two-pointer techniques
- Efficient algorithm design

---

## How to Use This Repository

1. Clone the repository.
2. Solve the problems on your own first.
3. Compare your solutions with the ones provided.
4. Test the solutions with edge cases to deepen your understanding.

**Happy Learning! 🚀**:

```bash

Feel free to expand on this README.md as you continue your learning!

```
