t = int(input())
for i in range(t) :
    n, s = input().split()
    n = int(n)
    s = list(s)
    a = ''
    for d in s :
        a = a + d * n
    print(a)