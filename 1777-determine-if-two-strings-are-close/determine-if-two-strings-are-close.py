class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        
        if len(word1) != len(word2):
            return False

        w1 = {}
        w2 = {}

        for char in word1:
            if char not in w1:
                w1[char] = 1
            else:
                w1[char] += 1
        
        for char in word2:
            if char not in w2:
                w2[char] = 1
            else:
                w2[char] += 1

        s1 = set(w1.keys())
        s2 = set(w2.keys())

        if (s1 - s2):
            return False

        ans1 = sorted(w1.values())
        ans2 = sorted(w2.values())

        if ans1 != ans2:
            return False
        
        return True
        