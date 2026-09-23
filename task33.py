n = int(input())
c = int(input())
k = int(input())
a = n*c
p = (k-1) // a + 1
pos = (k-1) % a+1
s = (pos - 1) // n + 1
strok = (pos - 1) % n + 1
print('страница', p, 'столбец', s, 'строка', strok)
