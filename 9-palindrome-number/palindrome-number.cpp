class Solution {
public:
    bool isPalindrome(int x) {
        int halfrev = 0;

        if(x < 0 || (x % 10 == 0 && x != 0)){
            return false;
        }

        while(halfrev < x){
            halfrev = halfrev * 10 + (x % 10);
            x /= 10;
        }

        return halfrev == x || halfrev/10 == x;
    }
};