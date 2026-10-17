class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left = 0
        right = 0
        maxx = 0
        curr = 0
        zeros = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            
            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            curr = right - left
            maxx = max(curr , maxx)
        
        return maxx