class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        track = []
        length = []

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
                track.append(i+1)
            elif len(stack) >0:
                stack.pop()
                track.pop()
            else:
                track.append(i+1)

        if len(track)>0:
            temp1 = track.pop()
            length.append(len(s)-temp1)

            for j in range(len(track)):
                temp2 = track.pop()
                length.append(temp1-1-temp2)
                temp1 = temp2

            length.append(temp1-1)

            return max(length)

        else:
            return len(s)

        
