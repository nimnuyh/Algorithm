area = [[0 for _ in range(100)] for _ in range(100)]

for _ in range(4) :
    a, b, c, d = map(int, input().split())
    for x in range(a, c) :
        for y in range(b, d) :
            area[x][y] = 1
ans = 0
for i in area :
    ans += sum(i)
print(ans)