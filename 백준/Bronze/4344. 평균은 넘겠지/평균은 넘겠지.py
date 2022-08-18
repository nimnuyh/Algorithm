for _ in range(int(input())) :
    input_list = list(map(int, input().split()))
    n = input_list.pop(0)
    avg = sum(input_list) / n
    c = len([x for x in input_list if x > avg])
    ans = round(c / n * 100, 4)
    ans = format(ans, '.3f')
    print(f'{ans}%')