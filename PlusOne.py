class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strDigits = ""
        for i in range(len(digits)):
            strDigits += str(digits[i])
        
        num = int(strDigits)+1
        strDigits = str(num)

        digits.clear()
        for j in range(len(strDigits)):
            digits.append(int(strDigits[j]))

        return digits
    