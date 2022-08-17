T = int(input())

for test_case in range(1, T + 1) :
    N = int(input())
    m = 0
    for i in range(N) :
        p, x = map(float, input().split())
        m = m + (p * x)
    print('#'+str(test_case), end = ' ')
    print(format(m, ".6f"))
