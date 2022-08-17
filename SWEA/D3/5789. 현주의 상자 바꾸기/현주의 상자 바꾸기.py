
T = int(input())
for TC in range(1, T + 1) :
    N, Q = map(int, input().split())
    box = [0 for n in range(N)]
    for i in range(1, Q + 1) :
        L, R = map(int, input().split())
        plus_list = [i for x in range(R - L + 1)]
        box[L - 1 : R] = plus_list
    print('#' + str(TC), end = ' ')
    for p in range(N) :
        if p != N - 1 :
            print(box[p], end = ' ')
        else :
            print(box[p])