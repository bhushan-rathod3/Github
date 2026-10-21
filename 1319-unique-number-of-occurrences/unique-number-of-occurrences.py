class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        nums = {}

        for num in arr:
            if num not in nums:
                nums[num] = 1
            if num in nums:
                nums[num] += 1

        if (len(set(nums.values())) == len(nums.values())):
            return True
        
        return False