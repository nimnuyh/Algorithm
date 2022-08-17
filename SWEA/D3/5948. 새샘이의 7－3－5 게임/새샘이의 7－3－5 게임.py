T = int(input())

for TC in range(1, 1 + T) :
    num = list(map(int, input().split()))
    ans = []
    for x in num :
        for y in num :
            for z in num :
                if x != y and y != z and z != x :
                    a = x + y + z
                    ans.append(a)
    ans = set(ans)
    ans = list(ans)
    ans.sort()
    print('#' + str(TC), ans[-5])