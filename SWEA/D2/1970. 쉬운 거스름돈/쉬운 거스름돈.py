
T = int(input())
for test_case in range(1, 1 + T) :
    N = int(input())
    print('#' + str(test_case))
    print(N // 50000, end = ' ')
    print(N % 50000 // 10000, end = ' ')
    print(N % 50000 % 10000 // 5000, end = ' ')
    print(N % 50000 % 10000 % 5000 // 1000, end = ' ')
    print(N % 50000 % 10000 % 5000 % 1000 // 500, end = ' ')
    print(N % 50000 % 10000 % 5000 % 1000 % 500 // 100, end = ' ')
    print(N % 50000 % 10000 % 5000 % 1000 % 500 % 100 // 50, end = ' ')
    print(N % 50000 % 10000 % 5000 % 1000 % 500 % 100 % 50 // 10)