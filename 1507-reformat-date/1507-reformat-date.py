class Solution:
    def reformatDate(self, date: str) -> str:
        months = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sep": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12",
        }
        
        DD,MM,YYYY = date.split()
        ans = YYYY + '-' + months[MM] + '-'
        
        if len(DD) < 4:
            ans += '0' + DD[:len(DD)-2]
        else:
            ans += DD[:2]
        
        return ans
        