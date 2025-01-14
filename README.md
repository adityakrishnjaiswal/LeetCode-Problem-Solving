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

## Problem: Maximum Score After Splitting a String

**Description:**

Given a string `s` of zeros and ones, *return the maximum score after splitting the string into two **non-empty** substrings* (i.e. **left** substring and **right** substring).

The score after splitting a string is the number of **zeros** in the **left** substring plus the number of **ones** in the **right** substring.

### Approach:

We iterate through the string and evaluate each **valid split point** to calculate the score:

1. **Initialize Counts:**
   * Count the **total number of '1's** in the string (`total_ones`).
   * Use a variable `left_zeros` to track **'0's** in the  **left substring** .
   * Use a variable `right_ones` initialized to `total_ones` to track **'1's** in the  **right substring** .
2. **Iterate Through the String:**
   * For every valid split point (`i` from `0` to `len(s) - 2`):
     * If the character is `'0'`, increment `left_zeros`.
     * If the character is `'1'`, decrement `right_ones`.
     * Calculate the  **current split score** :

current_score=left_zeros+right_ones\text{current\_score} = \text{left\_zeros} + \text{right\_ones}**current_score**=**left_zeros**+**right_ones*** Update the `max_score` if `current_score` is greater than the previous maximum.

3. **Return Maximum Score:**
   After evaluating all valid splits, return the maximum score.

### **Time Complexity:**

* **O(n)** → We iterate through the string once and calculate scores at each valid split.

### **Space Complexity:**

* **O(1)** → We use a few counters (`left_zeros`, `right_ones`, `max_score`) without additional data structures.

## **Problem: Best Time to Buy and Sell Stock II (Using Dynamic Programming)**

**Description:**

You are given an integer array `prices`, where `prices[i]` represents the  **price of a stock on the i-th day** .

* You can **buy and/or sell the stock** on any day.
* You can only **hold at most one share** of the stock at any given time.
* You are  **allowed to buy and sell on the same day** .

**Objective:**
Return the **maximum profit** you can achieve by choosing to buy and/or sell the stock on given days using  **Dynamic Programming (DP)** .

### **Approach:**

We use **Dynamic Programming (DP)** to track two states:

1. **Hold State (`dp[i][0]`)**
   * Either you **buy** the stock today, or you **keep holding** from yesterday.

dp[i][0]=max⁡(dp[i−1][0],dp[i−1][1]−prices[i])dp[i][0] = \max(dp[i-1][0], dp[i-1][1] - prices[i])

* Either you **sell** the stock today, or you **do nothing** and continue not holding a stock.

dp[i][1]=max⁡(dp[i−1][1],dp[i−1][0]+prices[i])dp[i][1] = \max(dp[i-1][1], dp[i-1][0] + prices[i])

* On  **Day 0** , if you're **holding** a stock: `dp[0][0] = -prices[0]`
* If you're **not holding** a stock: `dp[0][1] = 0`

3. The final answer will be in `dp[n-1][1]`, where `n` is the number of days.
4. The final answer will be in `dp[n-1][1]`, where `n` is the number of days.

### **Time Complexity:**

* **O(n)** → We loop through the prices array once.

### **Space Complexity:**

* **O(1)** (Optimized version) → Only two variables are used (`hold` and `no_hold`).

## **Problem: Jump Game**

**Description:**

You are given an integer array `nums`, where `nums[i]` represents the **maximum number of steps** you can jump forward from the `i-th` index.

* You start at  **index 0** .
* Your goal is to **reach the last index** of the array.

**Objective:**
Return `True` if you can reach the last index, otherwise return `False`.

### **Approach:**

**Intuition:**

The key is to track the **farthest index** you can reach as you iterate through the array. If at any point the current index exceeds the farthest reachable index, you cannot proceed further.

**Algorithm Steps:**

1. **Initialize** `farthest = 0` to track the farthest reachable index.
2. Loop through each index `i` in `nums`:
   * If `i > farthest`, return `False` (you cannot proceed).
   * Update `farthest = max(farthest, i + nums[i])`.
3. If the loop completes, return `True`.

**State Transition:**

* At each index `i`:

farthest=max⁡(farthest,i+nums[i])farthest = \max(farthest, i + nums[i])

 If `i > farthest`: return `False`

### **Time Complexity:**

* **O(n)** → The loop iterates through the array once.

### **Space Complexity:**

* **O(1)** → No additional space is used.

## Count Vowel Strings in Ranges

**Description:**

You are given a **0-indexed** array of strings `words` and a 2D array of integers `queries`.

Each query `queries[i] = [l<sub>i</sub>, r<sub>i</sub>]` asks us to find the number of strings present in the range `l<sub>i</sub>` to `r<sub>i</sub>` (both  **inclusive** ) of `words` that start and end with a vowel.

Return *an array *`ans`* of size *`queries.length`*, where *`ans[i]`* is the answer to the *`i`^th^ * query* .

**Note** that the vowel letters are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`.

### Approach:

**Intuition:**

Instead of checking the range `[li, ri]` repeatedly for each query, we can **precompute** the counts using a  **prefix sum array** .

* Each prefix sum will store the count of valid strings up to that index.
* For each query, we can quickly determine the count by subtracting prefix sums.

### **Time Complexity:**

* **O(n + q)** → `n` for building the prefix sum array and `q` for processing queries.

### **Space Complexity:**

* **O(n)** → For the prefix sum array.

## Problem: Number of Ways to Split Array

**Description:**

You are given a **0-indexed** integer array `nums` of length `n`.

`nums` contains a **valid split** at index `i` if the following are true:

* The sum of the first `i + 1` elements is **greater than or equal to** the sum of the last `n - i - 1` elements.
* There is **at least one** element to the right of `i`. That is, `0 <= i < n - 1`.

Return *the number of **valid splits** in* `nums`.

### Approach:

We can efficiently solve the problem using the  **Prefix Sum Technique** :

1. **Calculate the Total Sum:** Compute the total sum of the array.
2. **Iterate Through the Array:** Loop through the array (excluding the last element) while maintaining a  **prefix sum** .
3. **Calculate Right Sum:**
   Right Sum=Total Sum−Prefix Sum\text{Right Sum} = \text{Total Sum} - \text{Prefix Sum}**Right Sum**=**Total Sum**−**Prefix Sum**
4. **Check Validity:** Compare `Prefix Sum` and `Right Sum`. If:
   Prefix Sum≥Right Sum\text{Prefix Sum} \geq \text{Right Sum}**Prefix Sum**≥**Right Sum**
   Then increment the valid split counter.
5. **Return the Counter:** After the loop, return the total count of valid splits.

### **Time Complexity**

* **O(n)** — We iterate through the array once, performing constant-time calculations during each iteration.

### **Space Complexity**

* **O(1)** — Only a few integer variables (`prefix_sum`, `right_sum`, `valid_split_count`) are used, regardless of the input size.

## Problem: Jump Game II

**Description:**

You are given a **0-indexed** array of integers `nums` of length `n`. You are initially positioned at `nums[0]`.

Each element `nums[i]` represents the maximum length of a forward jump from index `i`. In other words, if you are at `nums[i]`, you can jump to any `nums[i + j]` where:

* `0 <= j <= nums[i]` and
* `i + j < n`

Return *the minimum number of jumps to reach *`nums[n - 1]`. The test cases are generated such that you can reach `nums[n - 1]`.

### Approach:

#### Dynamic Programming:

1. Start at index `0`.
2. For each index `i`:

   * Check all previous indices (`j`) where `j + nums[j] >= i`.
   * Update `dp[i]` as:

   dp[i]=min⁡(dp[i],dp[j]+1)dp[i] = \min(dp[i], dp[j] + 1)**d**p**[**i**]**=**min**(**d**p**[**i**]**,**d**p**[**j**]**+**1**)
3. The value at `dp[n-1]` will give the **minimum jumps** needed to reach the last index.

**Steps:**

1. **Initialize a DP array:**
   * Set `dp[0] = 0` (no jumps needed at the start).
   * Set all other indices to infinity (`float('inf')`).
2. **Iterate through the array:**
   * For each `i` (from `1` to `n-1`), check all previous indices (`j`) that can jump to `i`.
   * Update `dp[i]` with the minimum jumps.
3. **Return `dp[n-1]`:** The minimum jumps to reach the last index.

#### Greedy:

At every position:

1. **Maximize your reach:** Keep track of the **farthest index** you can jump to.
2. **Track your current range:** When you reach the  **end of the current jump range** , increment your jump count and extend your range to the  **farthest reachable index** .

**Steps:**

1. Start at index `0`.
2. Use two variables:
   * `current_reach`: The farthest point you can reach with the  **current jump** .
   * `next_reach`: The farthest point you can potentially reach with the  **next jump** .
3. Iterate through the array:
   * Update `next_reach` at every step.
   * If you reach the `current_reach`, increment the jump count and update `current_reach` to `next_reach`.
4. Stop when you reach or exceed the last index.

### Time Complexity:

#### Dynamic Programming:

* **O(n2**)**For each index `i`, we check all previous indices (`j`) to find the minimum jumps.

#### Greedy:

* **O**(**n**) We iterate through the array once, and each index is processed in constant time.

### Space Complexity:

#### Dynamic Programming:

* **O(1)**The `dp` array stores the minimum jumps for each index.

#### Greedy:

* **O**(**1**) Only a few integer variables are used (`jumps`, `current_reach`, `next_reach`).

## Problem: Unique Length-3 Palindromic Subsequences

Description:

Given a string `s`, return *the number of **unique palindromes of length three** that are a **subsequence** of *`s`.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted  **once** .

A **palindrome** is a string that reads the same forwards and backwards.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

### Approach:

To count the number of unique palindromic subsequences of length three in a string, we focus on identifying subsequences with the structure `aXa`, where the first and last characters are the same, and the middle character can be any character. The approach starts by iterating through each **unique character** in the string, treating it as the outer character (`a`) of the palindrome. For each character, we locate its **first** and **last occurrences** using string functions like `find()` and `rfind()`. If a valid range exists (i.e., the first index is less than the last index), we extract the **substring between these two positions** and collect all unique middle characters using a  **set** . The size of this set represents the number of unique palindromes that can be formed with the current character as the outer pair. We repeat this process for all unique characters and sum up the counts to get the final result. This approach efficiently avoids redundant checks by focusing only on unique characters and leverages set operations to ensure uniqueness, resulting in an optimized and clear solution.

### Time Complexity:

* There are at most **26 unique characters** (`a-z`).
* For each character, substring extraction and set creation are O(n)O(n)**O**(**n**).
* Overall: O(26⋅n)→O(n)O(26 \cdot n) → O(n)**O**(**26**⋅**n**)**→**O**(**n**)**

### Space Complexity:

* The set of middle characters uses up to O(n)O(n)**O**(**n**) space in the worst case.
* Overall: O(n)O(n)**O**(**n**)

## Problem: H-Index

**Description:**

Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their `i<sup>th</sup>` paper, return  *the researcher's h-index* .

According to the [definition of h-index on Wikipedia](https://en.wikipedia.org/wiki/H-index): The h-index is defined as the maximum value of `h` such that the given researcher has published at least `h` papers that have each been cited at least `h` times.

### Approach:

1. **Understand the Problem:**
   * We want the **maximum value of `h`** such that there are **at least `h` papers** with  **`h` or more citations** .
2. **Sort the Array:**
   * Sort the array in  **descending order** .
   * This makes it easier to count how many papers have at least `h` citations.
3. **Iterate and Compare:**
   * Iterate through the sorted array.
   * For each paper, check if its citation count is greater than or equal to its index (1-based).
   * Keep track of the maximum valid `h`.
4. **Stop When the Condition Fails:**
   * As soon as a paper’s citation count is less than its index, stop and return the last valid `h`.

### Time Complexity:

* **O**(**n**log**n**) → Sorting the array dominates the complexity.

### Space Complexity:

* **O**(**1**) → No extra space used apart from variables.

## Problem: Shifting Letters II

**Description:**

You are given a string `s` of lowercase English letters and a 2D integer array `shifts` where `shifts[i] = [start<sub>i</sub>, end<sub>i</sub>, direction<sub>i</sub>]`. For every `i`, **shift** the characters in `s` from the index `start<sub>i</sub>` to the index `end<sub>i</sub>` ( **inclusive** ) forward if `direction<sub>i</sub> = 1`, or shift the characters backward if `direction<sub>i</sub> = 0`.

Shifting a character **forward** means replacing it with the **next** letter in the alphabet (wrapping around so that `'z'` becomes `'a'`). Similarly, shifting a character **backward** means replacing it with the **previous** letter in the alphabet (wrapping around so that `'a'` becomes `'z'`).

Return *the final string after all such shifts to *`s` * are applied* .

### Approach:

**Naive Approach:**

* Directly process each shift, iterating over the substring `[starti, endi]` for each query.
* This leads to an inefficient `O(n * m)` time complexity (where `n` is the length of the string and `m` is the number of queries).

**Optimized Approach:**

* Use a **difference array** (prefix sum concept) to mark shifts at boundaries.
* Apply the difference array and then compute cumulative sums to get the final shift for each character in `O(n)` time.

**Steps:**

1. Create a `shift` array of length `n+1` (to handle boundaries cleanly).
2. For each query `[starti, endi, directioni]`:
   * If `directioni == 1`, increment `shift[starti]` and decrement `shift[endi+1]`.
   * If `directioni == 0`, decrement `shift[starti]` and increment `shift[endi+1]`.
3. Calculate the **prefix sum** of the `shift` array.
4. Apply the final `shift` values to the string.

### Time Complexity:

* `O(n + m)` (processing shifts + applying prefix sum)

### **Space Complexity:**

* `O(n)` (shift array)

## Problem: Minimum Number of Operations to Move All Balls to Each Box

**Description:**

You have `n` boxes. You are given a binary string `boxes` of length `n`, where `boxes[i]` is `'0'` if the `i<sup>th</sup>` box is  **empty** , and `'1'` if it contains **one** ball.

In one operation, you can move **one** ball from a box to an adjacent box. Box `i` is adjacent to box `j` if `abs(i - j) == 1`. Note that after doing so, there may be more than one ball in some boxes.

Return an array `answer` of size `n`, where `answer[i]` is the **minimum** number of operations needed to move all the balls to the `i<sup>th</sup>` box.

Each `answer[i]` is calculated considering the **initial** state of the boxes.

### Approach:

1. **Initialize:** Create an `answer` array of size `n` to store the result for each box.
2. **Left Pass:**

   * Move left to right, accumulating moves and ball count.
3. **Right Pass:**

   * Move right to left, accumulating moves and ball count.
4. Return the `answer` array.

### **Time Complexity:**

* O(n)O(n)**O**(**n**) Two passes (left-to-right and right-to-left).

### **Space Complexity:**

* O(n)O(n)**O**(**n**) Forhe `answer` array.

## Problem: String Matching in an Array

**Description:**

Given an array of string `words`, return all strings in *`words` that is a **substring** of another word* . You can return the answer in  **any order** .

A **substring** is a contiguous sequence of characters within a string.

### Approach:

* Initialize an empty list `result` to store the matching words.
* Iterate over each word `words[i]`.
* For each `words[i]`, iterate over the other words `words[j]`.
* If `words[i]` is a substring of `words[j]` and `i` is not equal to `j`, add `words[i]` to the `result` list and break the inner loop to avoid duplicate entries.
* Return the `result` list containing all words that are substrings of another word in the array.

### Time Complexity:

* **O**(**n**2**⋅**m**)***

### Space Complexity

* **O**(**n**⋅**m**)

## Problem: Insert Delete GetRandom O(1)

**Description:**

Implement the `RandomizedSet` class:

* `RandomizedSet()` Initializes the `RandomizedSet` object.
* `bool insert(int val)` Inserts an item `val` into the set if not present. Returns `true` if the item was not present, `false` otherwise.
* `bool remove(int val)` Removes an item `val` from the set if present. Returns `true` if the item was present, `false` otherwise.
* `int getRandom()` Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the **same probability** of being returned.

You must implement the functions of the class such that each function works in **average** `O(1)` time complexity.

### Approach:

* **Insert Operation:**
  * Checks if `val` exists in the set.
  * If not, adds it and returns `True`.
  * Otherwise, returns `False`.
* **Remove Operation:**
  * Checks if `val` exists in the set.
  * If present, removes it and returns `True`.
  * Otherwise, returns `False`.
* **getRandom Operation:**
  * Converts the set into a list and selects a random element using `random.choice`.

### **Time Complexity:**

* **Insert:** O(1)O(1)**O**(**1**) — Set insertion is average-case constant time.
* **Remove:** O(1)O(1)**O**(**1**) — Set removal is average-case constant time.
* **getRandom:** O(1)O(1)**O**(**1**) — `random.choice` on a list is constant time.

### **Space Complexity:**

* O(n)O(n)**O**(**n**) — Space is proportional to the number of elements in the set.

## Problem: Count Prefix and Suffix Pairs I

**Description:**

You are given a **0-indexed** string array `words`.

Let's define a **boolean** function `isPrefixAndSuffix` that takes two strings, `str1` and `str2`:

* `isPrefixAndSuffix(str1, str2)` returns `true` if `str1` is **both** a prefix

  and a suffix

  of `str2`, and `false` otherwise.

For example, `isPrefixAndSuffix("aba", "ababa")` is `true` because `"aba"` is a prefix of `"ababa"` and also a suffix, but `isPrefixAndSuffix("abc", "abcd")` is `false`.

Return  *an integer denoting the **number** of index pairs * `(i, j)`* such that *`i < j`*, and *`isPrefixAndSuffix(words[i], words[j])`* is *`true`*.*

### Approach:

1. Loop through all pairs of indices (i,j)(i, j)**(**i**,**j**)** where i<ji < j**i**<**j**.
2. For each pair, check if `words[i]` is a prefix and a suffix of `words[j]`.
   * Prefix: `words[j].startswith(words[i])`
   * Suffix: `words[j].endswith(words[i])`
3. Count pairs that satisfy both conditions.
4. Return the count.

### **Time Complexity:**

* O(n2)O(n^2)**O**(**n**2**)**Two nested loops run over the array.
* String comparisons (`startswith` and `endswith`) are efficient but still contribute.

### **Space Complexity:**

* O(1)O(1)**O**(**1**) No extra space is used apart from the count variable.

## Problem: Product of Array Except Self

**Description:**

Given an integer array `nums`, return *an array* `answer` *such that* `answer[i]` *is equal to the product of all the elements of* `nums` *except* `nums[i]`.

The product of any prefix or suffix of `nums` is **guaranteed** to fit in a **32-bit** integer.

You must write an algorithm that runs in `O(n)` time and without using the division operation.

### Approach:

* **Initialize Two Arrays:**
  * `prefix[]` → Store the cumulative product of elements *before* each index.
  * `suffix[]` → Store the cumulative product of elements *after* each index.
* **Calculate Prefix Products:**
  * Start from the left and calculate prefix products.
* **Calculate Suffix Products:**
  * Start from the right and calculate suffix products.
* **Calculate Final Answer:**
  * For each index `i`:
    answer[i]=prefix[i]×suffix[i]answer[i] = prefix[i] \times suffix[i]**an**s**w**er**[**i**]**=**p**re**f**i**x**[**i**]**×**s**u**ff**i**x**[**i**]**
* **Optimize Space:**
  * Instead of two extra arrays, we can use one result array and a temporary variable.

### Time Complexity:

* **O**(**n**)One pass for prefix, one pass for suffix.

### Space Complexity:

* **O**(**1**) (excluding the output array)
* No additional arrays, just a couple of scalar variables.

## Problem: Counting Words With a Given Prefix

**Description:**

Given an array of strings `words` and a string `pref`, the goal is to count the number of strings in the `words` array that contain `pref` as a prefix.

A prefix of a string `s` is any leading contiguous substring of `s`.

### Approach:

To solve this problem, we follow these steps:

1. **Initialize a Counter** : Start with a counter `a` set to `0` to keep track of strings with the given prefix.
2. **Iterate Through the Words** : Loop through each word in the `words` array.
3. **Check for Prefix** : For each word, check if `pref` matches the leading substring of the word. This can be done using slicing: `word[:len(pref)]`.
4. **Increment the Counter** : If the prefix matches, increment the counter.
5. **Return the Count** : After iterating through all words, return the counter.

### Time Complexity

* **Iterating Through the Array** : The loop iterates over all `n` words in the `words` array.
* **Prefix Comparison** : For each word, checking the prefix takes O(m)O(m)**O**(**m**), where mm**m** is the length of `pref`.

Overall, the time complexity is  **O(n * m)** , where:

* nn**n** is the number of words in the array.
* mm**m** is the length of the prefix.

### Space Complexity

The solution uses a constant amount of extra space, as no additional data structures are used. Thus, the space complexity is  **O(1)** .

## Problem: Gas Station

**Description:**

There are `n` gas stations along a circular route, where the amount of gas at the `i<sup>th</sup>` station is `gas[i]`.

You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from the `i<sup>th</sup>` station to its next `(i + 1)<sup>th</sup>` station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays `gas` and `cost`, return *the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return* `-1`. If there exists a solution, it is **guaranteed** to be  **unique** .

### Approach:

**Observation** :

* For a successful trip, the total gas in the circuit must be greater than or equal to the total cost:
  If ∑(gas)<∑(cost),no solution exists.\text{If } \sum(\text{gas}) < \sum(\text{cost}), \text{no solution exists.}**If **∑**(**gas**)**<**∑**(**cost**)**,**no solution exists.
* If a car runs out of gas at station ii**i**, any station between the previous start point and ii**i** cannot be the solution, so the search can restart from i+1i+1**i**+**1**.

**Algorithm** :

* Calculate the total gas and total cost.
* If the total gas is less than the total cost, return `-1`.
* Otherwise, iterate through the stations and track the remaining gas:
  * If the gas tank goes negative at station ii**i**, restart the journey from station i+1i+1**i**+**1**.
* Return the starting station.

### Time Complexity

* Iterating through the stations: O(n)O(n)**O**(**n**).
* Total complexity: O(n)O(n)**O**(**n**).

### Space Complexity

* The solution uses only constant extra space: O(1)O(1)**O**(**1**).

## Problem: Word Subsets

**Description:**

You are given two string arrays `words1` and `words2`.

A string `b` is a **subset** of string `a` if every letter in `b` occurs in `a` including multiplicity.

* For example, `"wrr"` is a subset of `"warrior"` but is not a subset of `"world"`.

A string `a` from `words1` is **universal** if for every string `b` in `words2`, `b` is a subset of `a`.

Return an array of all the **universal** strings in `words1`. You may return the answer in **any order**

### Approach:

The main goal is to check whether each word in `words1` contains all the characters needed by every word in `words2` with the correct frequency. Instead of checking for each word in `words2` within each word in `words1` repeatedly, we can approach the problem as follows:

1. **Character Frequency Count for `words2`:**
   First, we need to figure out the frequency of each character in `words2`. For each word in `words2`, we determine the maximum frequency of each character required.
2. **Checking Superset Condition:**
   For each word in `words1`, we check whether it contains the required characters from `words2` with the necessary frequency.

### Time Complexity:

 **O(N * M + P * K)** , where:

* `N` = number of words in `words2`,
* `M` = average length of words in `words2`,
* `P` = number of words in `words1`,
* `K` = average length of words in `words1`.

### Space Complexity:

* **O(P)** , where `P` is the number of words in `words1`.

## Problem: Candy

**Description:**

There are `n` children standing in a line. Each child is assigned a rating value given in the integer array `ratings`.

You are giving candies to these children subjected to the following requirements:

* Each child must have at least one candy.
* Children with a higher rating get more candies than their neighbors.

Return  *the minimum number of candies you need to have to distribute the candies to the children* .

### Approach:

We can solve this problem in a **greedy** manner using two passes over the ratings array:

1. **First Pass (Left to Right):**
   * Start by assigning 1 candy to each child.
   * Traverse the array from left to right, and for each child, if their rating is higher than the previous child's rating, they should receive one more candy than the previous child.
2. **Second Pass (Right to Left):**
   * Traverse the array from right to left.
   * For each child, if their rating is higher than the next child's rating, update the candy count to ensure the child receives more candies than the next child (but only if it's greater than the previously assigned candies to avoid overriding the first pass).

After both passes, the total number of candies will be the sum of the candies assigned to each child.

### **Time Complexity:**

* The solution involves two passes through the array, making the time complexity  **O(n)** , where `n` is the number of children.

### **Space Complexity:**

* We use an additional array `candies` to store the candy count for each child, so the space complexity is  **O(n)** .

## Construct K Palindrome Strings

**Description:**

Given a string `s` and an integer `k`, return `true` *if you can use all the characters in *`s`* to construct *`k`* palindrome strings or *`false` * otherwise* .

### Approach:

* **Count odd frequencies** directly while iterating through the string.
* **Early exit** : If at any point, the number of odd frequencies exceeds `k`, we can return `false` immediately.
* **Simplified logic** : No need to store the full frequency count of all characters; we only care about how many characters have an odd frequency.

### **Time Complexity**:

O(n)

### **Space Complexity**:

O(m), where `m` is the number of unique characters in the string

## Problem: Trapping Rain Water

**Description:**

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

### Approach:

**Key Observations:**

1. Water trapped above a bar depends on the **minimum** of the tallest bars to its **left** and  **right** :
   * `water[i] = min(max_left[i], max_right[i]) - height[i]`
2. The challenge is efficiently calculating `max_left` and `max_right` for every bar.

### Time Complexity:

* The array is traversed once using two pointers, so the time complexity is  **O(n)** .

### Space Complexity:

* We use a constant amount of extra space, so the space complexity is **O(1).**

## Problem: Check if a Parentheses String Can Be Valid

**Description:**

A parentheses string is a **non-empty** string consisting only of `'('` and `')'`. It is valid if **any** of the following conditions is  **true** :

* It is `()`.
* It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid parentheses strings.
* It can be written as `(A)`, where `A` is a valid parentheses string.

You are given a parentheses string `s` and a string `locked`, both of length `n`. `locked` is a binary string consisting only of `'0'`s and `'1'`s. For **each** index `i` of `locked`,

* If `locked[i]` is `'1'`, you **cannot** change `s[i]`.
* But if `locked[i]` is `'0'`, you **can** change `s[i]` to either `'('` or `')'`.

Return `true`  *if you can make `s` a valid parentheses string* . Otherwise, return `false`.

### Approach:

* **Track Imbalance from Left to Right:**

  * Simulate the parentheses validation from left to right.
  * Use a counter open\text{open}**open** to track the net number of open parentheses that need closing.
  * Increment open\text{open}**open** for '(' or when you treat a modifiable '0' as '('.
  * Decrement open\text{open}**open** for ')'.
  * If open\text{open}**open** ever goes negative, it means there's an unmatched ')' which cannot be resolved, so return `False`.
* **Track Imbalance from Right to Left:**

  * Perform a similar pass from right to left, but in reverse, treating unmatched '(' as invalid.
  * Use a counter close\text{close}**close** to track the number of ')' that are needed to balance the string.
  * If close\text{close}**close** goes negative during this pass, return `False`.
* **Final Check:**

  * If both passes are valid, return `True`, since it indicates that we can resolve all mismatched parentheses.

### Time Complexity:

* **O**(**n**) because we make two linear passes over the string.

### Space Complexity:

* **O**(**1**) since we use constant extra space.

## Problem: Roman to Integer

**Description:**

Roman numerals are represented by seven different symbols: `I`, `V`, `X`, `L`, `C`, `D` and `M`.

<pre><strong>Symbol</strong>       <strong>Value</strong>
I             1
V             5
X             10
L             50
C             100
D             500
M             1000</pre>

For example, `2` is written as `II` in Roman numeral, just two ones added together. `12` is written as `XII`, which is simply `X + II`. The number `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not `IIII`. Instead, the number four is written as `IV`. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as `IX`. There are six instances where subtraction is used:

* `I` can be placed before `V` (5) and `X` (10) to make 4 and 9.
* `X` can be placed before `L` (50) and `C` (100) to make 40 and 90.
* `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

### Approach:

1. **Understand the Symbol Values:**
   * Create a mapping of Roman numerals to their respective integer values:
     roman_to_int = {
     'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
     }
2. **Traverse the String:**
   * Iterate through the string from left to right.
   * If the current numeral is smaller than the next numeral, subtract its value (e.g., II**I** before VV**V** is subtracted to make IV=4IV = 4**I**V**=**4).
   * Otherwise, add its value.
3. **Return the Total:**
   * The total computed will be the integer representation of the Roman numeral.

Here’s the Python implementation:

### Time Complexity:

* **O**(**n**), where nn**n** is the length of the Roman numeral string.

### Space Complexity:

* O(1)O(1)**O**(**1**), as we use a fixed dictionary for mappings and a few variables for computation.

## Problem: Minimum Length of String After Operations

**Description:**

You are given a string `s`.

You can perform the following process on `s` **any** number of times:

* Choose an index `i` in the string such that there is **at least** one character to the left of index `i` that is equal to `s[i]`, and **at least** one character to the right that is also equal to `s[i]`.
* Delete the **closest** character to the **left** of index `i` that is equal to `s[i]`.
* Delete the **closest** character to the **right** of index `i` that is equal to `s[i]`.

Return the **minimum** length of the final string `s` that you can achieve.

### Approach:

* **Count character frequencies:**
  First, count the frequency of each character in the given string using the `Counter` from Python's `collections` module. This will allow us to track how many times each character appears in the string.
* **Process each character frequency:**
  For each character in the string, we need to determine how many characters can be removed (pairs of characters). The condition for removing a character is that there must be one occurrence to the left and one occurrence to the right of any selected index.
  * If a character appears an even number of times, we can remove pairs of characters. This will effectively reduce its count to zero.
  * If a character appears an odd number of times, we will be left with one character after performing the operation, which can't be removed.
* **Return the final length of the string:**
  After removing all possible characters, the final length of the string will be the sum of the leftover characters (those that couldn't be removed in pairs). This can be computed by checking the parity (odd or even) of the frequency of each character.

### Time Complexity:

* The `Counter` object is built in **O(n)** time, where `n` is the length of the input string `s`.
* Iterating over the values of the `Counter` takes **O(k)** time, where `k` is the number of distinct characters in the string. In the worst case, `k` can be as large as `n` (when all characters are unique).

Thus, the overall time complexity is **O(n)**

### Space Complexity:

* The space complexity is determined by the storage required for the `Counter` object. The `Counter` stores the frequency of each distinct character, which requires **O(k)** space, where `k` is the number of distinct characters in the string. In the worst case, `k` can be equal to `n` (when all characters are unique).

Thus, the overall space complexity is  **O(k)** , where `k` is the number of distinct characters in the string.

## Problem: Integer to Roman

**Description:**

Seven different symbols represent Roman numerals with the following values:

| Symbol | Value |
| ------ | ----- |
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

* If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
* If the value starts with 4 or 9 use the **subtractive form** representing one symbol subtracted from the following symbol, for example, 4 is 1 (`I`) less than 5 (`V`): `IV` and 9 is 1 (`I`) less than 10 (`X`): `IX`. Only the following subtractive forms are used: 4 (`IV`), 9 (`IX`), 40 (`XL`), 90 (`XC`), 400 (`CD`) and 900 (`CM`).
* Only powers of 10 (`I`, `X`, `C`, `M`) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (`V`), 50 (`L`), or 500 (`D`) multiple times. If you need to append a symbol 4 times use the  **subtractive form** .

Given an integer, convert it to a Roman numeral.

### Approach:

* **Create a Mapping for Roman Numerals** :
  We need to have a list of tuples, where each tuple consists of a decimal value and its corresponding Roman numeral symbol. These tuples should be ordered from largest to smallest values.
* **Iterate Through the List** :
  We will iterate through the list of Roman numeral values and check which one is the largest that can be subtracted from the given integer (the input number). We subtract this value from the integer, and append the corresponding Roman numeral to the result string. This process continues until the integer becomes zero.
* **Handling Subtractive Notation** :
  The subtractive notation (e.g., IV for 4, IX for 9, XL for 40, etc.) should naturally be handled because we include these subtractive pairs in the Roman numeral mapping.

### Time Complexity:

* The loop iterates through the list of Roman numeral values, which has a fixed size (13 elements).
* In each iteration, we perform constant time operations (subtracting values and appending symbols to the result).

Thus, the overall time complexity is  **O(1)** , since the length of the list and the number of operations per iteration are constant.

### Space Complexity:

* The space complexity is **O(1)** for the algorithm itself, as the space used for storing the Roman numeral symbols is fixed and independent of the input size.
* The space for the result string is proportional to the number of Roman numeral symbols needed, but this is still considered **O(1)** in terms of space complexity because the input size is limited to a fixed range (typically up to 3999 for Roman numerals).

## Problem: Find the Prefix Common Array of Two Arrays

**Description:**

You are given two **0-indexed **integer permutations `A` and `B` of length `n`.

A **prefix common array** of `A` and `B` is an array `C` such that `C[i]` is equal to the count of numbers that are present at or before the index `i` in both `A` and `B`.

Return *the **prefix common array** of *`A`* and *`B`.

A sequence of `n` integers is called a **permutation** if it contains all integers from `1` to `n` exactly once.

### Approach:

* Use sets to keep track of elements seen so far in AA**A** and BB**B**.
* For each index ii**i**:
  * Add A[i]A[i]**A**[**i**] and B[i]B[i]**B**[**i**] to their respective sets.
  * Compute the intersection of the two sets to find common elements.
  * Update C[i]C[i]**C**[**i**] with the size of the intersection.

### Time Complexity:

**O**(**n**⋅**lo**g**(**n**))**

### Space Complexity:

**O**(**n**)**(for the output array **C**)**.

## Problem: Length of Last Word

**Description:**

Given a string `s` consisting of words and spaces, return the length of the last word in the string. A word is defined as a maximal substring consisting of non-space characters only.

### Approach:

* **Split the String** : Use Python's `split()` method to split the string into words by spaces. This removes extra spaces automatically.
* **Find Last Word** : Retrieve the last word from the resulting list of words using its index (`-1`).
* **Return Length** : Calculate the length of the last word using the `len()` function and return it.

### Time Complexity:

* **Splitting the String:**
  The `split()` function processes the entire string of length `n`.
  **Time Complexity = O(n)**
* **Accessing Last Word:**
  Accessing the last word is constant time.
  **Time Complexity = O(1)**
* **Calculating Length of the Last Word:**
  The length of the last word depends on the word size, which is negligible compared to the entire string.
  **Time Complexity = O(k)** (where `k` is the length of the last word).

**Overall Time Complexity = O(n)**

### Space Complexity:

* The `split()` function creates a list of words, consuming space proportional to the number of words.
  **Space Complexity = O(n)**

## Problem: Longest Common Prefix

---

**Description:**

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

### Approach:

* We compare characters column by column. For each column (i.e., each character position), we check if all strings have the same character at that position.
* If we find any mismatch, we return the prefix up to the previous column.
* If all strings are the same up to a certain column, we continue checking the next column.
* If one of the strings is exhausted (i.e., shorter than the others), the longest common prefix is the part of the strings we've compared up to that point.

### Time Complexity:

* `O(S)`, where `S` is the total number of characters across all strings. In the worst case, we may need to check every character in all strings.

### **Space Complexity:**

* `O(1)` since we are only using a constant amount of extra space aside from the input.

## Problem: Minimize XOR

---

**Description:**

Given two positive integers `num1` and `num2`, find the positive integer `x` such that:

* `x` has the same number of set bits as `num2`, and
* The value `x XOR num1` is  **minimal** .

Note that `XOR` is the bitwise XOR operation.

Return *the integer *`x`. The test cases are generated such that `x` is  **uniquely determined** .

The number of **set bits** of an integer is the number of `1`'s in its binary representation.

### Approach:

1. **Count Set Bits of `num2`:** Calculate how many set bits (1's) are in `num2`.
2. **Greedy Strategy:**
   * Initialize `x` to 0 and iterate over `num1`'s bits (from MSB to LSB).
   * Set bits in `x` where `num1` has 1s, if more set bits are needed.
3. **Fill Remaining Bits:** If more set bits are needed, set the lowest available bits in `x`.
4. **Return `x`:** After setting the required number of bits.

### Time Complexity:

* **O(32)** : We iterate over 32 bits, making the time complexity effectively constant (`O(1)`).

### Space Complexity:

* **O(1)** : We use only a fixed amount of space for variables like `x` and `set_bits`.
