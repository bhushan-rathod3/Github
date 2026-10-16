class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        max_len = 0
        curr_len = 0
        zero_cnt = 0

        left = 0
        right = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_cnt += 1
            
            while zero_cnt > k:
                if nums[left] == 0:
                    zero_cnt -= 1
                left += 1

            curr_len = right - left + 1
            max_len = max(curr_len , max_len)

        return max_len
            
            
            

