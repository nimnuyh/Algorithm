a, b = input().split()
for i in list(a) :
    if i in list(b) :
        c = i
        break
for n in range(len(b)) :
    if n != b.find(c) :
        print('.'*a.find(c) + b[n] + '.'*(len(a)-1-a.find(c)))
    else :
        print(a)