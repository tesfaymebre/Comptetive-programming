import math

len_AB = int(input())
len_BC = int(input())
degree_sign = u"\N{DEGREE SIGN}"
len_MC = math.sqrt(len_AB**2 + len_BC**2)/2
angC = math.atan(len_AB/len_BC)
len_BM = math.sqrt(len_BC**2 + len_MC**2 -(2*len_BC*len_MC * math.cos(angC)))
theta = math.degrees(math.asin((len_MC/len_BM)*math.sin(angC)))
print(str(round(theta)) + degree_sign)
