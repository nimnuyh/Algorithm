num = list(input())

num_dict = {}

alphabet = list('ABCDEFGHIJKLMNOPQRSTUWVXYZ')
for a in alphabet :
    if a in list('ABC') :
        num_dict[a] = 3
    elif a in list('DEF') :
        num_dict[a] = 4
    elif a in list('GHI') :
        num_dict[a] = 5
    elif a in list('JKL') :
        num_dict[a] = 6
    elif a in list('MNO') :
        num_dict[a] = 7
    elif a in list('PQRS') :
        num_dict[a] = 8
    elif a in list('TUV') :
        num_dict[a] = 9
    else :
        num_dict[a] = 10

ans = 0
for i in num :
    ans += num_dict[i]
print(ans)