class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = int("".join(str(d) for d in digits))
        num += 1
        digi = []
        while num > 0:
            digit = num % 10
            digi.append(digit)
            num //= 10
        
        return digi[::-1]



        