class Solution {
public:
    int pivotIndex(vector<int>& nums) {
       int rightSum = 0 , leftSum = 0 , totalSum = 0;

       for(auto num : nums){
        totalSum += num;
       }

       for(int i = 0 ; i < nums.size() ; i++){
        rightSum = totalSum - leftSum - nums[i];

        if(leftSum == rightSum){
            return i;
        }

        leftSum += nums[i];
       }

       return -1;
    }
};