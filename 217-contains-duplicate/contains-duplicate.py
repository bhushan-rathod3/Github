class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        new = set(nums)
        return len(nums) != len(new)
        