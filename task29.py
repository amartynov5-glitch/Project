import math
a = float(input())
b = float(input())
c = float(input())
alpha = math.degrees(math.acos((b**2 + c**2 - a**2)/(2*b*c)))
beta = math.degrees(math.acos((a**2 + c**2 - b**2)/(2*a*c)))
gamma = math.degrees(math.acos((b**2 + a**2 - c**2)/(2*b*a)))
print(alpha)
print(beta)
print(gamma)

