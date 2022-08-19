import sys
input = sys.stdin.readline
n, m = map(int, input().split())
p_dict = {}
for i in range(n):
    p = input().rstrip()
    p_dict[i + 1] = p
    p_dict[p] = i + 1

for i in range(m):
    q = input().rstrip()
    if q.isdigit():
        print(p_dict[int(q)])
    else:
        print(p_dict[q])