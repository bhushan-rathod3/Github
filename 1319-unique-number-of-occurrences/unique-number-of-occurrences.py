class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        nums = {}

        for num in arr:
            if num in nums:
                nums[num] += 1
            else:
                nums[num] = 1

        val_cnt = len(nums.values())
        set_cnt = len(set(nums.values()))

        return val_cnt == set_cnt