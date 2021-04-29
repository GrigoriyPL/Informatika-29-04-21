fil  = open("27-14a.txt")
num = int(fil.readline())
mas = [0] * 12
c = 0
for i in range(num):
    x = int(fil.readline())
    c += mas[(12 - x % 12) % 12]
    mas[x % 12] += 1
    print(mas)
print(c)