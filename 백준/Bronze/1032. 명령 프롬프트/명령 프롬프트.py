w_list = []
for _ in range(int(input())) :
    w_list.append(input())
ans = ''
for i in range(len(w_list[0])) :
    c = 0
    for w in w_list :
        if w_list[0][i] == w[i] :
            c += 1
    if c == len(w_list) :
        ans = ans + w_list[0][i]
    else :
        ans = ans + '?'
print(ans)