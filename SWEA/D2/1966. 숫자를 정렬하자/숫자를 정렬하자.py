
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, T + 1) :
    N = int(input())
    n = list(map(int, input().split()))
    n.sort()
    print('#' + str(test_case), end = ' ')
    for i in range(N) :
        if i < N - 1 :
            print(n[i], end = ' ')
        else :
            print(n[i])