w_list = []
for i in range(5) :
    w_list.append(list(input()))
ans = ''
for _ in range(len(max(w_list, key = len))) :
    for w in w_list :
        try :
            ans = ans + w.pop(0)
        except :
            continue
print(ans)