# Leetcode question  - https://leetcode.com/problems/multiply-strings/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # ASCII code for 0 = 48
        number1 = 0
        number2 = 0
        place1  = 0
        for i in range(1, len(num1)+1):
            unit =  ord(num1[-i]) - 48
            number1 += unit * pow(10, place1)
            place1 += 1

        place2  = 0
        for j in range(1, len(num2)+1):
            unit =  ord(num2[-j]) - 48
            number2 += unit * pow(10, place2)
            place2 += 1

        return str(number1 * number2)
