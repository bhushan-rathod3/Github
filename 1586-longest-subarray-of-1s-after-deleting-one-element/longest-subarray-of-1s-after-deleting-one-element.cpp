class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int left = 0 , right = 0 , maxOnes = 0 , zeros = 0 , curr = 0;

        for(right ; right < nums.size() ; right++){
            if(nums[right] == 0) zeros++;

            while(zeros > 1){
                if(nums[left] == 0) zeros--;
                left++;
            }

            curr = right - left;
            maxOnes = max(maxOnes , curr);

        } 

        return maxOnes;
    }
};