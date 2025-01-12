"""A parentheses string is a non-empty string consisting only of '(' and ')'. It is valid if any of the following conditions is true:
It is ().
It can be written as AB (A concatenated with B), where A and B are valid parentheses strings.
It can be written as (A), where A is a valid parentheses string.
You are given a parentheses string s and a string locked, both of length n. locked is a binary string consisting only of '0's and '1's. For each index i of locked,
If locked[i] is '1', you cannot change s[i].
But if locked[i] is '0', you can change s[i] to either '(' or ')'.
Return true if you can make s a valid parentheses string. Otherwise, return false."""

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        n = len(s)
        
        # First pass: Left to right
        open_balance = 0
        for i in range(n):
            if locked[i] == '0' or s[i] == '(':
                open_balance += 1
            else:
                open_balance -= 1
            
            # If open_balance is negative, too many unmatched ')'
            if open_balance < 0:
                return False
        
        # Second pass: Right to left
        close_balance = 0
        for i in range(n - 1, -1, -1):
            if locked[i] == '0' or s[i] == ')':
                close_balance += 1
            else:
                close_balance -= 1
            
            # If close_balance is negative, too many unmatched '('
            if close_balance < 0:
                return False
        
        # If both passes are valid, the string can be valid
        return True