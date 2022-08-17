n = int(input())

for x in range(1, n + 1) : 
    s = 0
    if x >= 100 :
        if x // 100 % 3 == 0 : # 100의 자리
            s = s + 1
            if x % 100 // 10 % 3 == 0 and x % 100 // 10 != 0 : # 10의 자리
                s = s + 1
                if x % 100 % 10 % 3 == 0 and x % 100 % 10 != 0 : # 1의 자리
                    s = s + 1
                    print('-' * s, end = ' ')
                else :
                    print('-' * s, end = ' ')
            else :
                if x % 100 % 10 % 3 == 0 and x % 100 % 10 != 0 : # 1의 자리
                    s = s + 1
                    print('-' * s, end = ' ')
                else :
                    print('-' * s, end = ' ')
        else :
            if x % 100 // 10 % 3 == 0 and x % 100 // 10 != 0 : # 10의 자리
                s = s + 1
                if x % 100 % 10 % 3 == 0 and x % 100 % 10 != 0 : # 1의 자리
                    s = s + 1
                    print('-' * s, end = ' ')
            else :
                if x % 100 % 10 % 3 == 0 and x % 100 % 10 != 0 : # 1의 자리
                    s = s + 1
                    print('-' * s, end = ' ')
                else :
                    print(x, end = ' ')
    elif x > 10 :
        if x % 100 // 10 % 3 == 0 and x % 100 // 10 != 0 : # 10의 자리
            s = s + 1
            if x % 100 % 10 % 3 == 0 and x % 100 % 10 != 0 : # 1의 자리
                s = s + 1
                print('-' * s, end = ' ')
            else :
                print('-' * s, end = ' ')
        else :
            if x % 100 % 10 % 3 == 0 and x % 100 % 10 != 0 : # 1의 자리
                s = s + 1
                print('-' * s, end = ' ')
            else :
                print(x, end = ' ')
    elif x <= 10 and x % 3 == 0 :
        print('-', end = ' ')
    else :
        print(x, end = ' ')