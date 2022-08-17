for _ in range(int(input())) :
    w_list = [input() for _ in range(int(input()))]
    pointer = 0
    end = False
    while pointer < len(w_list) and end == False :
        for i in range(pointer + 1, len(w_list)) :
            w1 = w_list[pointer] + w_list[i]
            w2 = w_list[i] + w_list[pointer]
            if w1 == w1[::-1] :
                print(w1)
                end = True
                break
            elif w2 == w2[::-1] :
                print(w2)
                end = True
                break
        pointer += 1
    if end == False :
        print(0)