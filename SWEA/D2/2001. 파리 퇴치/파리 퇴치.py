
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1) :
    N, M = map(int, input().split())

    square = [list(map(int, input().split())) for _ in range(N)]

    maxi = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            current = 0
            for k in range(M):
                for l in range(M):
                    current += square[j+l][i+k]
            if current > maxi:
                maxi = current
    print('#{} {}'.format(test_case, maxi))