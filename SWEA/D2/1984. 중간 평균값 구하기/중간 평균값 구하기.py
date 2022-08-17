
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1,  T + 1) :
    x = list(map(int, input().split()))
    x.remove(max(x))
    x.remove(min(x))
    print('#'+str(test_case), int(round(sum(x) / 8, 0)))