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
