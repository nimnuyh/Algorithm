
T = int(input())

a = T // 1000
T = T % 1000
b = T // 100
T = T % 100
c = T // 10
T = T % 10

print(a+b+c+T)