"""You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself."""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Adds two non-empty linked lists representing two non-negative integers.
        Digits are stored in reverse order, and each node contains a single digit.
        
        Args:
            l1 (ListNode): The head of the first linked list.
            l2 (ListNode): The head of the second linked list.
        
        Returns:
            ListNode: The head of the linked list representing the sum of the two numbers.
        """
        # Create a dummy node to simplify edge cases and initialize pointers
        dummy = ListNode(0)
        current = dummy  # Pointer to build the result list
        carry = 0  # Carry to handle sums >= 10
        
        # Loop until both lists are exhausted and no carry remains
        while l1 or l2 or carry:
            # Extract the current values from the nodes, or use 0 if the node is None
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum of the two digits plus any carry from the previous step
            total = val1 + val2 + carry
            carry = total // 10  # Update the carry for the next digit
            current.next = ListNode(total % 10)  # Create a node for the current digit
            
            # Move to the next nodes in both lists, if available
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Return the head of the resulting linked list (skip the dummy node)
        return dummy.next
