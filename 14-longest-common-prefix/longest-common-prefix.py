class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        min_len = float('inf')
        min_word = ""
        for word in strs:
            if len(word) < min_len:
                min_len = len(word)
                min_word += word

        lcs = ""
        for i in range(min_len):
            curr_word = min_word[i]

            for word in strs:
                if curr_word != word[i]:
                    curr_word = ""
                    break
            if curr_word == "":
                break
            lcs += curr_word

        return lcs 