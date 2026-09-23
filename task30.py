ATT = int(input())
COMP = int(input())
YDS = int(input())
TD = int(input())
INT = int(input())
A = ((COMP/ATT)-0.3)*5
B = ((YDS / ATT) - 3) * 0.25
C = (TD / ATT) * 20
D = 2.375 - ((INT / ATT)*25)
rat = ((A+B+C+D)/6)*100
print(rat)