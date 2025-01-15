"""Given two positive integers num1 and num2, find the positive integer x such that:
x has the same number of set bits as num2, and
The value x XOR num1 is minimal.
Note that XOR is the bitwise XOR operation.
Return the integer x. The test cases are generated such that x is uniquely determined.
The number of set bits of an integer is the number of 1's in its binary representation."""

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Count the number of set bits in num2
        count_num2 = bin(num2).count('1')
        
        # We will construct the number x
        x = 0
        set_bits = 0
        
        # Try to set bits at positions where num1 has 1s
        for i in range(31, -1, -1):
            if (num1 >> i) & 1:  # If bit i is set in num1
                if set_bits < count_num2:
                    x |= (1 << i)  # Set bit i in x
                    set_bits += 1
        
        # If there are remaining set bits to be set, set them in the lowest positions
        i = 0
        while set_bits < count_num2:
            if (x >> i) & 1 == 0:  # Only set if the bit is not already set
                x |= (1 << i)
                set_bits += 1
            i += 1
        
        return x
