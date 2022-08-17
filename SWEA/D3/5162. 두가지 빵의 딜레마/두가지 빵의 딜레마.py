
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for TC in range(1, 1 + T) :
    a, b, c = map(int, input().split())
    if a < b :
        ans1 = c // a
        ans2 = c % a // b
        print('#'+str(TC), int(ans1 + ans2))
    else :
        ans1 = c // b
        ans2 = c % b // a
        print('#'+str(TC), int(ans1 + ans2))