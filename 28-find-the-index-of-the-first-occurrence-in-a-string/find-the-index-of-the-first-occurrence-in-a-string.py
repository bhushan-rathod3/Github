class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        end = len(needle)
        if needle in haystack:
            for i in range(len(haystack) - end + 1):
                if haystack[i:i + end] == needle:
                    return i
        else:
            return -1