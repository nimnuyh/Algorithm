import sys
input = sys.stdin.readline
n, m = map(int, input().split())
ans_dict = {}
for _ in range(n) :
    x = input().rstrip()
    ans_dict[x] = 1
for _ in range(m) :
    x = input().rstrip()
    if ans_dict.get(x) != None :
        ans_dict[x] += 1
ans_list = []
for k, v in ans_dict.items() :
    if v > 1 :
        ans_list.append(k)
print(len(ans_list))
ans_list.sort()
for ans in ans_list :
    print(ans)