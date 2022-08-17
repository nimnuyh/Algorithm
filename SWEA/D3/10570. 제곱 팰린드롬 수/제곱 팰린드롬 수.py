import math

T = int(input())

for TC in range(T):
    a,b = map(int,input().split())
    cnt = 0
    for i in range(a,b+1):
        s = math.sqrt(i)
        if s % 1 > 0:
            continue
        s = str(int(s))
        i = str(i)
        if i==i[::-1] and s==s[::-1]:
            cnt+=1

    print('#{} {}'.format(TC+1,cnt))