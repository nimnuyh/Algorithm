
T = int(input())
for test_case in range(1, T + 1) :
    t = map(int, input().split())
    time = list(t)
    if time[0] + time[2] > 12 :
        if time[1] + time[3] > 60 :
            print('#' + str(test_case), time[0] + time[2] + 1 - 12, end = ' ')
            print(time[1] + time[3] - 60)
        else :
            print('#' + str(test_case), time[0] + time[2] - 12, end = ' ')
            print(time[1] + time[3])
    else : 
        if time[1] + time[3] > 60 :
            print('#' + str(test_case), time[0] + time[2] + 1, end = ' ')
            print(time[1] + time[3] - 60)
        else :
            print('#' + str(test_case), time[0] + time[2], end = ' ')
            print(time[1] + time[3])