class Solution:
    def intToRoman(self, num: int) -> str:
        integers = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        roman_nums = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        
        result = ""
        for index,value in enumerate(integers):
            result += (num//value)*roman_nums[index]
            num = num%value
            
        return result
        
        