class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        size_s = len(s)
        ans = 0
        
        for word in words:
            i = 0
            tmp = 0
            j = 0
            while i <len(word):
                
                ch = word[i]
                
                count = 0
                while i < len(word) and word[i]==ch:
                    count+=1
                    i+=1
                s_count = 0
                
                while j< size_s and s[j]==ch:
                    s_count+=1
                    j+=1
                
                if  ((s_count >=3 and count < s_count) or count==s_count):
                    tmp+=count 
                
            ans+=((tmp==len(word)) and j==size_s)
        return ans