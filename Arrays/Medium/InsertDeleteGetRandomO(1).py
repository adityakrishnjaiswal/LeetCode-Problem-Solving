"""Implement the RandomizedSet class:
RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity."""

import random

class RandomizedSet:

    def __init__(self):
        # Initialize an empty set
        self.myset = set()

    def insert(self, val: int) -> bool:
        # Insert if the value is not already present
        if val not in self.myset:
            self.myset.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        # Remove if the value exists
        if val in self.myset:
            self.myset.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        # Return a random value from the set
        if not self.myset:
            raise ValueError("The set is empty")
        return random.choice(list(self.myset))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()