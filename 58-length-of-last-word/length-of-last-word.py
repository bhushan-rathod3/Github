class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        last = len(words[-1])

        return last