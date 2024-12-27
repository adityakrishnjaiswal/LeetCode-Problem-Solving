# LeetCode Solutions

This repository contains solutions to various LeetCode problems. The goal is to showcase optimized solutions with clear explanations and help others improve their problem-solving skills.

## Problem: Two Sum

**Description:**
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to the target.
You may assume that each input will have exactly one solution, and you may not use the same element twice.

### Approach:

The solution uses a HashMap (dictionary) to store previously seen numbers and their indices. For each number, we calculate its complement and check if it has been encountered before.

### Time Complexity:

O(n) - where n is the length of the `nums` list.

### Space Complexity:

O(n) - due to the HashMap storing indices.

## Problem: 3Sum

**Description:**

Given an array of integers `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that:

* `i != j`, `i != k`, and `j != k`
* `nums[i] + nums[j] + nums[k] == 0`

You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

### Approach:

The solution first sorts the array to simplify finding triplets. It then iterates through each element, using the two-pointer technique to find pairs that sum to the complement of the current element. Duplicate triplets are avoided by skipping duplicate values for the fixed element and the pointers.

### Time Complexity:

* **Sorting:** `O(n log n)`
* **Two-pointer approach:** For each element, we use the two-pointer technique to find other two elements, making the total time complexity for the two-pointer approach `O(n)`.
* **Overall Time Complexity:** `O(n^2)`, where `n` is the length of the `nums` array.

### Space Complexity:

* **Auxiliary Space:** `O(1)` for the two-pointer technique.
* **Result Storage:** `O(k)`, where `k` is the number of triplets found, which can be at most `O(n^2)`.

## **Problem: Add Two Numbers**

**Description:**
You are given two non-empty **linked lists** representing two non-negative integers. The digits are stored in  **reverse order** , and each of their nodes contains a  **single digit** . Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number `0` itself.

### **Approach:**

We use a **dummy node** to simplify handling edge cases and initialize a **pointer (`current`)** to build the result list. A **carry** variable is used to handle sums greater than or equal to `10`.
For each node in the two linked lists:

1. Sum the digits of the current nodes along with the carry.
2. Create a new node for the current digit (`total % 10`).
3. Update the carry (`total // 10`).
4. Move to the next nodes in both lists.

### **Time Complexity:**

* **O(max(m, n))** — where `m` and `n` are the lengths of the two linked lists.

### **Space Complexity:**

* **O(max(m, n))** — for storing the resulting linked list.

## Problem: Target Sum

**Description:**
You are given an integer array `nums` and an integer `target`. You want to assign each integer in the array either a `'+'` or `'-'` sign such that the sum of the resulting expression equals the target.

Return the **number of different expressions** that can be built to achieve the target sum.

### **Approach:**

The problem can be reduced to a  **Subset Sum Problem** :

* Calculate the total sum of the array.
* Check if dividing the array into two subsets (`subset1` and `subset2`) can satisfy the condition:
  (total_sum+target)/2=subset1(total\_sum + target) / 2 = subset1**(**t**o**t**a**l**_**s**u**m**+**t**a**r**g**e**t**)**/2**=**s**u**b**se**t**1
* Use a **Dynamic Programming** approach to count the subsets that sum up to `subset1`.

**Key Steps:**

1. Validate if the target is achievable.
2. Transform the problem into a subset sum problem.
3. Use a **1D Dynamic Programming array** to calculate the number of subsets with the target sum.

---

### **Time Complexity:**

* O(n×target_sum)O(n \times target\_sum)**O**(**n**×**t**a**r**g**e**t**_**s**u**m**)**
* Where `n` is the number of elements in `nums`.

### **Space Complexity:**

* O(target_sum)O(target\_sum)**O**(**t**a**r**g**e**t**_**s**u**m**)**
* Using a 1D DP array to store intermediate results.

## **Problem: Best Sightseeing Pair**

**Description:**

You are given an integer array `values` where `values[i]` represents the score of the `i-th` sightseeing spot. The score of a pair `(i, j)` is calculated as:

values[i]+values[j]+i−jvalues[i] + values[j] + i - j**v**a**l**u**es**[**i**]**+**v**a**l**u**es**[**j**]**+**i**−**j**Return the **maximum score** of a sightseeing pair.

**Constraints:**

* `2 <= values.length <= 50,000`
* `1 <= values[i] <= 1,000`

### **Approach:**

We can break down the formula:

values[i]+values[j]+i−jvalues[i] + values[j] + i - j**v**a**l**u**es**[**i**]**+**v**a**l**u**es**[**j**]**+**i**−**j**into two parts:

(values[i]+i)+(values[j]−j)(values[i] + i) + (values[j] - j)**(**v**a**l**u**es**[**i**]**+**i**)**+**(**v**a**l**u**es**[**j**]**−**j**)**1.  **Maximize `(values[i] + i)`** : Keep track of the maximum value of `values[i] + i` as we iterate.

1. For every `j`, calculate the total score using the previously tracked maximum `(values[i] + i)` and `(values[j] - j)`.
2. Update the maximum score during each iteration.

This approach eliminates the need for a nested loop, achieving linear time complexity.

### **Time Complexity:**

* **O(n)** — We iterate through the list once, and each iteration performs constant-time operations.

### **Space Complexity:**

* **O(1)** — Only two variables (`max_score` and `max_i`) are used, regardless of input size


## **Problem: Merge Sorted Array**

### **Description**

You are given two integer arrays `nums1` and `nums2`, sorted in  **non-decreasing order** , and two integers `m` and `n`:

* `nums1` has a length of `m + n`:
  * The first `m` elements are valid and sorted.
  * The remaining `n` elements are set to `0` and should be ignored.
* `nums2` has a length of `n` and contains `n` valid sorted integers.

The task is to  **merge `nums2` into `nums1` in-place** , ensuring that the resulting array remains  **sorted in non-decreasing order** .

---

### **Approach**

1. **Initialize Pointers:**
   * Start from the end of both arrays to avoid overwriting valid data in `nums1`.
   * Use three pointers: one for the last valid element in `nums1`, one for the last element in `nums2`, and one for the last position in the combined array.
2. **Merge from the End:**
   * Compare the elements from the end of `nums1` and `nums2`.
   * Place the larger element at the end of `nums1`.
   * Move the respective pointer and decrement the merge position.
3. **Handle Remaining Elements in `nums2`:**
   * If there are still elements left in `nums2`, copy them directly into `nums1`.
   * Remaining elements in `nums1` are already in the correct place.

---

### **Time Complexity**

* **O(m + n)**
  * Each comparison and assignment is performed at most `m + n` times.

---

### **Space Complexity**

* **O(1)**
  * The merging process is performed directly in `nums1` without requiring any extra space.
