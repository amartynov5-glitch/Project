import math
from math import *
r1 = int(input())
r2 = int(input())
if r1 > r2:
    s = math.pi * (r1**2 - r2**2)
else:
    s = math.pi * (r2**2 - r1**2)
print(s)
