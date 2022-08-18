score = []
for _ in range(5) :
    s = sum(map(int, input().split()))
    score.append(s)
print(f'{score.index(max(score)) + 1} {max(score)}')