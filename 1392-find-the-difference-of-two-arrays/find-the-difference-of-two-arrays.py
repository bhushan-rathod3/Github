class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:

        a1 = set()
        a2 = set()
        for num in nums1:
            if num not in nums2:
                a1.add(num)
        
        for num in nums2:
            if num not in nums1:
                a2.add(num)

        ans = list(a1)
        ans2 = list(a2)

        return [ans,ans2]