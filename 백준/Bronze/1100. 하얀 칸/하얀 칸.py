chess = []
for _ in range(8) :
    chess.append(list(input()))
ans = 0
for i, l in enumerate(chess) :
    if i % 2 == 0 :
        for j, cell in enumerate(l) :
            if j % 2 == 0 and cell == 'F' :
                ans += 1
    else :
        for j, cell in enumerate(l) :
            if j % 2 == 1 and cell == 'F' :
                ans += 1
print(ans)