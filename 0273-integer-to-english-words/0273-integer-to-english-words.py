class Solution:
    def numberToWords(self, num: int) -> str:
        if(num == 0): 
            return "Zero"
        
        one_digit = {1: 'One', 2: 'Two', 3: 'Three',4: 'Four',5: 'Five',
                     6: 'Six',7: 'Seven', 8: 'Eight',9: 'Nine'}

        two_digit = {10: 'Ten',11: 'Eleven',12: 'Twelve',13: 'Thirteen',14: 'Fourteen', 
                     15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 
                     19: 'Nineteen'}
        
        tens = {2: 'Twenty', 3: 'Thirty',4: 'Forty', 5: 'Fifty',
                6: 'Sixty', 7: 'Seventy',8: 'Eighty',9: 'Ninety'}
        
        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand = (num - billion * 1000000000 - million * 1000000) // 1000
        last_three = num - billion * 1000000000 - million * 1000000 - thousand * 1000
        
        def get_three_digit(num):
            if not num:
                return ""
            if not num// 100: 
                return get_two_digit(num)
            
            temp = one_digit[ num // 100 ] + " Hundred"
            if num % 100:
                return temp + " " + get_two_digit( num % 100 )
            else:
                return temp 
            
        def get_two_digit(num):
            if not num:
                return ''
            elif num < 10:
                return one_digit[ num ]
            elif num < 20:
                return two_digit[ num ]
                   
            if num % 10:
                return tens[num//10] + " " + one_digit[ num % 10 ]
            else:
                return tens[num//10]
        
        result = ''
        
        if billion:        
            result = get_three_digit(billion) + ' Billion'
            
        if million:
            result += ' ' if result else ''    
            result += get_three_digit(million) + ' Million'
            
        if thousand:
            result += ' ' if result else ''
            result += get_three_digit(thousand) + ' Thousand'
            
        if last_three:
            result += ' ' if result else ''
            result += get_three_digit(last_three)
            
        return result