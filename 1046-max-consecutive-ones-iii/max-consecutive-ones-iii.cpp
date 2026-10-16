class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int maxx = 0 , curr = 0 , left = 0 , right = 0 , zeroCnt = 0;

        for(right ; right < nums.size() ; right++){
            if(nums[right] == 0) zeroCnt++;

            while(zeroCnt > k){
                if(nums[left] == 0) zeroCnt--;
                left++;
            }

            curr = right - left + 1;
            maxx = max(curr , maxx);
        }

        return maxx;
    }
};