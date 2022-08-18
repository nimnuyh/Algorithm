for t in range(int(input())) :
    if t > 0 :
        input()
    sdk = []
    for _ in range(9) :
        sdk.append(list(map(int, input().split())))

    check = [1,2,3,4,5,6,7,8,9]
    ans = 'CORRECT'
    end = False
    while ans == 'CORRECT' and end == False :
        for h in sdk :
            if sorted(h) != check :
                ans = 'INCORRECT'

        for i in range(9) :
            v = []
            for l in sdk :
                v.append(l[i])
            if sorted(v) != check :
                ans = 'INCORRECT'

        for i in range(0, 9, 3) :
            for j in range(0, 9, 3) :
                l = sdk[i][j : j + 3] + sdk[i + 1][j : j + 3] + sdk[i + 2][j : j + 3]
                if sorted(l) != check : 
                    ans = 'INCORRECT'

        end = True
    print(f'Case {t + 1}: {ans}')