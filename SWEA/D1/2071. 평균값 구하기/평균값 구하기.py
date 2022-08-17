T = int(input())
for test_case in range(1, T + 1) :
    a0, a1, a2, a3, a4, a5, a6, a7, a8, a9 = map(int, input().split())
    print('#'+str(test_case),int(round((sum((a0, a1, a2, a3, a4, a5, a6, a7, a8, a9))/10), 0)))