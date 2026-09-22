s = int(input())
h = s // 60 // 60
m = (s // 60) % 60
sec = s % 60 % 60
print(h, 'часов', m, 'минут', sec, 'секунд')