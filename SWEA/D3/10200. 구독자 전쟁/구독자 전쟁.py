T = int(input())

for TC in range(T):
    n,a,b = map(int,input().split())

    if a+b <= n:
        max_n = min(a,b)
        min_n = 0
    elif a+b > n:
        max_n = min(a, b)
        min_n = a+b-n
    if a==b and b==n:
        max_n = n
        min_n = n
    print('#{} {} {}'.format(TC+1,max_n,min_n))