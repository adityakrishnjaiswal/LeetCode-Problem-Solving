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
