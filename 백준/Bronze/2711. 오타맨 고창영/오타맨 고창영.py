t = int(input())
for i in range(t) :
    e, s = input().split()
    e = int(e) - 1
    print(s[:e] + s[e+1:])