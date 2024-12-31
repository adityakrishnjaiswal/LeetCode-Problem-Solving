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

### **Approach:**

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

### **Time Complexity:**

* **O(m + n)**
  * Each comparison and assignment is performed at most `m + n` times.

---

### **Space Complexity:**

* **O(1)**
  * The merging process is performed directly in `nums1` without requiring any extra space.

## Problem: Remove Element

**Description:**

Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in `nums` [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm). The order of the elements may be changed. Then return *the number of elements in *`nums`* which are not equal to *`val`.

Consider the number of elements in `nums` which are not equal to `val` be `k`, to get accepted, you need to do the following things:

* Change the array `nums` such that the first `k` elements of `nums` contain the elements which are not equal to `val`. The remaining elements of `nums` are not important as well as the size of `nums`.
* Return `k`.

### **Approach:**

To correctly solve the problem of removing all occurrences of a given value from the list `nums` in-place, you can use the following approach:

1. **Iterate through the list** with a pointer, keeping track of the elements that do not match the target value `val`.
2. **Shift non-matching elements** to the front of the array.
3. **Return the length** of the modified list that contains no occurrences of `val`.

### Time Complexity:

* **O(n)** : We iterate through the list once, where `n` is the length of the list `nums`.

### **Space Complexity** :

* **O(1)** : We are modifying the list in place and using a constant amount of extra space.

## Problem: Remove Duplicates from Sorted Array

**Description:**

Given an integer array `nums` sorted in  **non-decreasing order** , remove the duplicates [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm) such that each unique element appears only  **once** . The **relative order** of the elements should be kept the  **same** . Then return *the number of unique elements in *`nums`.

Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:

* Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially. The remaining elements of `nums` are not important as well as the size of `nums`.
* Return `k`.

### **Approach:**

We can solve this problem by modifying the list in-place using the two-pointer technique. Here's the optimized approach:

1. **Pointer `i`** to track the position of the last unique element.
2. **Pointer `j`** to iterate through the list and compare the current element with the last unique element.
3. If the element at `j` is different from the last unique element, move it to the next position in the list.

### **Time Complexity** :

* **O(n)** : We traverse the list once, where `n` is the length of the list `nums`.

### **Space Complexity** :

* **O(1)** : The solution modifies the list in-place and uses a constant amount of extra space.

## Problem: Remove Duplicates from Sorted Array II

**Description:**

Given an integer array `nums` sorted in  **non-decreasing order** , remove some duplicates [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm) such that each unique element appears  **at most twice** . The **relative order** of the elements should be kept the  **same** .

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the **first part** of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements.

Return `k`* after placing the final result in the first *`k`* slots of *`nums`.

### **Approach:**

* Use a pointer `i` to iterate through the array.
* Use another pointer `j` to keep track of the position where the next valid element should be placed.
* Allow each unique element to appear  **at most twice** .
* To enforce this, compare the current element `nums[i]` with the element `nums[j-2]` (ensuring it's valid) to check if we have already added it twice.
* If the condition holds, add the current element to the result and increment `j`.

### **Time Complexity:**

* O(n)O(n)**O**(**n**) — We iterate through the array once.

### **Space Complexity:**

* O(1)O(1)**O**(**1**) — We modify the array in place without using extra space.

## **Problem: Majority Element**

**Description:**

Given an array `nums` of size `n`, return the  **majority element** .
The **majority element** is the element that appears  **more than ⌊n / 2⌋ times** .
You can assume that the array always contains a majority element.

### Approach:

* **Candidate Selection:**
  * Use a `candidate` variable to store a potential majority element.
  * Use a `count` variable to track balance.
  * Increment `count` if the current number matches `candidate`, else decrement.
  * If `count` is `0`, select a new candidate.
* **Return Candidate:**
  * Since a majority element is guaranteed, return the final `candidate`.

### Time Complexity:

**O**(**n**) — Single pass through the array.

### Space Complexity:

**O**(**1**) — Only two variables are used.

## **Problem: Rotate Array**

**Description:**

Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.

### **Approach:**

* **Normalize `k`:**
  * Since rotating the array by its length `n` doesn't change the array, reduce `k` to `k % n` (i.e., `k = k % len(nums)`).
    This ensures that we handle cases where `k` is greater than `n` (the length of the array).
* **Reverse the Entire Array:**
  * Reverse the entire array first. This ensures that the elements at the end of the array are moved towards the front.
* **Reverse the First `k` Elements:**
  * After reversing the entire array, the last `k` elements are in the front. We reverse just the first `k` elements to restore their correct order.
* **Reverse the Remaining `n - k` Elements:**
  * Finally, reverse the remaining `n - k` elements to restore their correct order.

### **Time Complexity:**

* O(n)O(n)**O**(**n**) — Each element is reversed a constant number of times.

### **Space Complexity:**

* O(1)O(1)**O**(**1**) — In-place rotation with no extra space.

## Problem: Number of Ways to Form a Target String Given a Dictionary

**Description:**

You are given a list of strings of the **same length** `words` and a string `target`.

Your task is to form `target` using the given `words` under the following rules:

* `target` should be formed from left to right.
* To form the `i<sup>th</sup>` character ( **0-indexed** ) of `target`, you can choose the `k<sup>th</sup>` character of the `j<sup>th</sup>` string in `words` if `target[i] = words[j][k]`.
* Once you use the `k<sup>th</sup>` character of the `j<sup>th</sup>` string of `words`, you **can no longer** use the `x<sup>th</sup>` character of any string in `words` where `x <= k`. In other words, all characters to the left of or at index `k` become unusuable for every string.
* Repeat the process until you form the string `target`.

**Notice** that you can use **multiple characters** from the **same string** in `words` provided the conditions above are met.

Return  *the number of ways to form `target` from `words`* . Since the answer may be too large, return it **modulo** `10<sup>9</sup> + 7`.

### Approach:

* **Frequency Map Preprocessing:**
  * Build a **frequency table** (`freq`) to count how many times each character appears at each column across all strings in `words`.
  * This allows quick lookup for the number of ways a character in `target` can be formed from each column.
* **Dynamic Programming with Memoization:**
  * Use a **recursive DP function** (`dp(i, j)`) where:
    * `i`: The current index in the `target` string.
    * `j`: The current column in `words`.
  * The DP function considers two choices at every step:
    1. **Skip the current column (`j`)** and move to the next column (`j+1`).
    2. **Use the current column (`j`)** if it contains the required character (`target[i]`) and then move to the next character in `target` (`i+1`) and the next column (`j+1`).
* **Base Cases:**
  * If `i == len(target)`: Successfully formed the `target` → Return `1`.
  * If `j == len(words[0])`: Ran out of columns → Return `0`.
* **Recursive Transition:**
  * If `target[i]` exists in column `j`:
    dp(i,j)=dp(i,j+1)+freq[j][target[i]]×dp(i+1,j+1)dp(i, j) = dp(i, j+1) + freq[j][target[i]] \times dp(i+1, j+1)**d**p**(**i**,**j**)**=**d**p**(**i**,**j**+**1**)**+**f**re**q**[**j**]**[**t**a**r**g**e**t**[**i**]]**×**d**p**(**i**+**1**,**j**+**1**)
  * Use **Memoization** to avoid recalculating overlapping subproblems.
* **Modulo Operation:**
  * Since the result can be very large, take every intermediate result modulo 109+710^9 + 7**1**0**9**+**7**.
* **Final Answer:**
  * The answer is given by `dp(0, 0)`

### Time Complexity:

O(m×n+n×t)O(m \times n + n \times t)**O**(**m**×**n**+**n**×**t**)* `m × n`: Frequency table construction

* `n × t`: DP recursion with memoization

If `m` is much larger than `t`, the preprocessing step dominates.

**Final Time Complexity:** O(m×n+n×t)O(m \times n + n \times t)**O**(**m**×**n**+**n**×**t**)

### Space Complexity:

**O**(**n**×**26**+**t**×**n**+**t**+**n**)Simplified:

O(n×t+n+t)O(n \times t + n + t)**O**(**n**×**t**+**n**+**t**)For large inputs, the dominant term is O(n×t)O(n \times t)**O**(**n**×**t**).

**Final Space Complexity:** O(n×t)O(n \times t)**O**(**n**×**t**)

## **Problem: Best Time to Buy and Sell Stock**

**Description:**

You are given an array `prices` where `prices[i]` represents the price of a given stock on the `i-th` day.

You want to maximize your profit by choosing **a single day to buy one stock** and  **a different day in the future to sell that stock** .

Return **the maximum profit** you can achieve from this transaction. If you cannot achieve any profit, return `0`.

### **Approach**

We use a **single pass loop** to keep track of:

1. The **minimum price encountered so far** (`min_price`) to simulate the best buying opportunity.
2. The **maximum profit** (`max_profit`) we can achieve if we sell on the current day.

### **Time Complexity:**

* **O(n)**
  We iterate through the `prices` array once, where `n` is the number of days.

### **Space Complexity:**

* **O(1)**
  We only use two variables (`min_price` and `max_profit`) regardless of the input size.

## **Problem: Best Time to Buy and Sell Stock**

**Description:**

You are given an array `prices` where `prices[i]` represents the price of a given stock on the `i-th` day.

You want to maximize your profit by choosing **a single day to buy one stock** and  **a different day in the future to sell that stock** .

Return **the maximum profit** you can achieve from this transaction. If you cannot achieve any profit, return `0`.

### **Approach:**

We use a **single-pass loop** to keep track of:

1. The **minimum price encountered so far** (`min_price`) to simulate the best buying opportunity.
2. The **maximum profit** (`max_profit`) we can achieve if we sell on the current day.

At each step:

* Update `min_price` if the current price is lower.
* Calculate the profit if sold on the current day (`current_price - min_price`) and update `max_profit` if it's larger.

### **Time Complexity:**

* **O(n)** → We iterate through the array once.

### **Space Complexity:**

* **O(1)** → Only two variables (`min_price` and `max_profit`) are used.

## **Problem: Minimum Cost for Train Tickets**

**Description:**

You are given an integer array `days`, where each element represents a day of the year (from  **1 to 365** ) that you plan to travel. Train tickets are available in three options:

1. **1-day pass:** Costs `costs[0]` dollars and covers 1 day of travel.
2. **7-day pass:** Costs `costs[1]` dollars and covers 7 consecutive days of travel.
3. **30-day pass:** Costs `costs[2]` dollars and covers 30 consecutive days of travel.

The passes allow travel for the corresponding number of consecutive days starting from the day of purchase.

**Objective:**
Return the **minimum cost** required to travel on all the days given in the array `days`.

### **Approach:**

We use **Dynamic Programming (DP)** to solve this problem efficiently.

1. **Define a DP Array:**
   * `dp[i]` represents the **minimum cost** of traveling from day `i` to the end of the `days` array.
2. **Iterate Backward:**
   * Start from the last travel day and move backward.
   * For each day, consider purchasing each of the 1-day, 7-day, and 30-day passes.
   * Use a pointer `j` to find the next valid day after the current pass expires.
   * Update `dp[i]` with the **minimum cost** from the three options.
3. **Transition Formula:**
   dp[i]=min⁡(dp[j]+cost)dp[i] = \min(dp[j] + cost) **d**p**[**i**]**=**min**(**d**p**[**j**]**+**cos**t**)**where `j` represents the next index after the pass expires.
4. **Base Case:**
   * Beyond the last day of travel, the cost is `0`.

### **Time Complexity:**

* **O(n * 3)** → For each day, we evaluate three pass options (1-day, 7-day, and 30-day).

### **Space Complexity:**

* **O(n)** → We use a `dp` array of size `n+1` where `n` is the number of travel days.
