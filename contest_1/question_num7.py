symbol_val = {'I':1, 'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
S = input()
numVal = 0
for i in range(len(S)):
    numVal = numVal + int(symbol_val[S[i]])
print(numVal)
