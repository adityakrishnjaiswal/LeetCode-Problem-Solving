"""Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only."""

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.split()
        arrlen=len(s)
        wordlen=len(s[arrlen-1])
        return wordlen