class Solution {
public:
    int reverse(int x) {
        int rev = 0, digit = 0 , temp = x;

        while( temp != 0){
            
            digit = temp % 10;

            if((rev > INT_MAX/10) || (rev < INT_MIN / 10)) return 0;

            rev = rev * 10 + digit;
            temp /= 10;
        }

        return rev;
        
    }
};