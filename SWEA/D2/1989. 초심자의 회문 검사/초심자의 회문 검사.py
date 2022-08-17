
T = int(input())
for test_case in range(1, T + 1) :
    a = str(input())
    b = ''.join(reversed(a))
    if a == b :
        print('#'+str(test_case),1)
    else :
        print('#'+str(test_case),0)