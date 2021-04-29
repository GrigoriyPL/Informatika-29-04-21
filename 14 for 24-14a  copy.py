fil = open("27-14a.txt")
num = int(fil.readline())
mas = []
for i in range(num):
    mas.append(int(fil.readline()))
c = 0
for i in range(num - 1):
    for j in range(i + 1, num):
        if (mas[i] + mas[j]) % 12 == 0:
            c += 1
print(c)