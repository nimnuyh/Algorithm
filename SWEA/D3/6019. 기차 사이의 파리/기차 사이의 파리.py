T = int(input())
for TC in range(1, T + 1) :
    D, A, B, F = map(int, input().split())
    t = D / (A + B)
    print('#'+str(TC), end=' ')
    print(format(F * t, ".10f"))