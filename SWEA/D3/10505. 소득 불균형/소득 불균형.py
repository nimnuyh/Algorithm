T = int(input())

for TC in range(T):
    n = int(input())
    s = list(map(int,input().split()))
    sum = 0
    for i in s:
        sum+=int(i)
    average = sum/n
    cnt = 0
    for i in s:
        if int(i) <= average:
            cnt+=1
    print('#{} {}'.format(TC+1,cnt))