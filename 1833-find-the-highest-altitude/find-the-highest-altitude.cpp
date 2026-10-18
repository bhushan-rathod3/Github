class Solution {
public:
    int largestAltitude(vector<int>& gain) {
        int maxx = 0 , curr = 0;
        for(int i = 0 ; i < gain.size() ; i++){
            curr += gain[i];
            if(curr > maxx) maxx = curr;
        }
        return maxx;
    }
};