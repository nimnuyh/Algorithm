T = int(input())

for test_case in range(1, T + 1) :

    string = input()

    li = []
    for i in range(1, 11):
        li.append(string[:i])

    ans = 10
    for i in range(10):
        tmp = len(li[i])

        if string[:tmp] == string[tmp:2 * tmp]:
            if tmp < ans:
                ans = tmp
                break
    print('#{} {}'.format(test_case, ans))