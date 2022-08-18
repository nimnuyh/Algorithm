input_list = list(map(int, input().split()))
while input_list != sorted(input_list) :
    for i in range(len(input_list) - 1) :
        a = input_list[i]
        b = input_list[i + 1]
        if input_list[i] > input_list[i + 1] :
            input_list[i] = b
            input_list[i + 1] = a
            print(f'{input_list[0]} {input_list[1]} {input_list[2]} {input_list[3]} {input_list[4]}')