class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        j = len(nums) - 1

        while i <= j:
            if nums[i] == val:
                if nums[j] != val:
                    nums[i] , nums[j] = nums[j] , nums[i]
                    i += 1
                    j -= 1
                else:
                    j -= 1
            if nums[i] != val:
                i += 1

        j = len(nums) - 1

        while j >= 0:
            if nums[j] == val:
                nums.pop(j)
            j -= 1

        return len(nums)
            
                
            