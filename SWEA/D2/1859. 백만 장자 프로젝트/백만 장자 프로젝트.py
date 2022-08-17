T = int(input())

for i in range(T):
    N = int(input())
    x = list(map(int, input().split(' ')))[::-1]  # 뒤에서부터 탐색
    answer = 0
    now = x[0]  # 현재 가장 큰 값

    for j in range(1, N):
        if now > x[j]:
            answer += now - x[j]
        else:
            now = x[j]

    print('#{} {}'.format(i+1, answer))
