n = int(input())
for i in range(n) :
    if i % 2 == 0 :
        star = '*' + ' *' * (n - 1)
        print(star)
    else :
        star = ' *' * n
        print(star)