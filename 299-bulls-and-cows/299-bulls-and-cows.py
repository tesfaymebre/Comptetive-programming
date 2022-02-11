class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        item = Counter(secret)
        bull = 0
        cow = 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull+=1
                item[secret[i]]-=1
        for j in range(len(secret)):
            if secret[j] != guess[j] and item[guess[j]] > 0:
                cow+=1
                item[guess[j]]-=1
                
        return (str(bull)+"A"+str(cow)+"B")
                
            