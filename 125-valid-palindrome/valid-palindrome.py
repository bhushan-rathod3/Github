class Solution:
    def isPalindrome(self, s: str) -> bool:
        raw = re.sub("[^A-Za-z0-9]" , "" , s).lower()
        return raw == raw[::-1]