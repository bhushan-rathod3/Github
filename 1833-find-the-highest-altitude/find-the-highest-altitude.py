class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        maxx = 0
        curr = 0

        for num in gain:
            curr += num
            maxx = max(curr,maxx)

        return maxx