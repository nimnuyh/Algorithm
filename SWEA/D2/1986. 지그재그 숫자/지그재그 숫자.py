
T = int(input())
for test_case in range(1,T + 1) :
    n = int(input())
    x = 0
    for i in range(1, n + 1) :
        if i % 2 == 1 :
            x = x + i
        else :
            x = x - i
    print('#'+str(test_case), x)