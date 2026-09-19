weight = int(input())
hight = int(input())
h1 = 0.0254*hight
w1 = 0.45359237*weight
print(f'{w1/(h1**2):.2f}')
