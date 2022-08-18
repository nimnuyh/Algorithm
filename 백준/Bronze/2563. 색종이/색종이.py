n = int(input())
area = [[0 for _ in range(100)] for _ in range(100)]
 
for _ in range(n):
    x, y = map(int, input().split())
    for a in range(x, x + 10):
        for b in range(y, y + 10):
            area[a][b] = 1
ans = 0
for i in area :
    ans += sum(i)
print(ans)