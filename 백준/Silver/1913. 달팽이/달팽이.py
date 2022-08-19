n = int(input())
f = int(input())
base = [[0 for _ in range(n)] for _ in range(n)]

m = [[0, 1],[1, 0],[0, -1],[-1, 0]]
d = 0
x, y, num = 0, 0, n ** 2

while num > 0 :
    base[y][x] = num
    if(x + m[d][0] < 0 
       or x + m[d][0] >= n 
       or y + m[d][1] < 0 
       or y + m[d][1] >= n 
       or base[y + m[d][1]][x + m[d][0]] != 0):
        d = (d + 1) % 4
    y += m[d][1]
    x += m[d][0]
    num -= 1

for l in base :
    for d in l :
        if l.index(d) == n - 1:
            if d == f :
                print(d)
                x, y = l.index(d), base.index(l)
            else :
                print(d)
        else :
            if d == f :
                print(d, end = ' ')
                x, y = l.index(d), base.index(l)
            else :
                print(d, end = ' ')
print(y + 1, x + 1)