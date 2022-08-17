
T = int(input())
for test_case in range(1, T + 1) :
    a0, a1 = map(int, input().split())
    if a0 > a1 :
        print('#'+str(test_case),'>')
    elif a0 == a1 :
        print('#'+str(test_case),'=')
    else : 
        print('#'+str(test_case),'<')