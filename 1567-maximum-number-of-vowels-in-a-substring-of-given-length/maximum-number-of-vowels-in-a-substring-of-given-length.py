class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_v = 0
        cnt = 0
        vowels = "aeiou"

        for i in range(k):
            if s[i] in vowels:
                cnt += 1

        max_v = cnt
        for i in range(len(s) - k):
            if s[i] in vowels:
                cnt-=1
            if s[i+k] in vowels:
                cnt+=1
            max_v = max(max_v,cnt)

        return max_v