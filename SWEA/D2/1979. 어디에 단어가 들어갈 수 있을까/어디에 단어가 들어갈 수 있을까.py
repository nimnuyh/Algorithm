def checkK(current):
    global cnt
    if Ks in current :
        check = ''
        for i in range(N):
            if check == '':
                if current[i] == '1':
                    check += '1'
            else:
                if current[i] == '1':
                    check += '1'
                    if i == N-1 and len(check) == K:
                        cnt += 1
                else:
                    if len(check) == K:
                        cnt += 1
                        check = ''
                    else:
                        check = ''

# T = 1
T = int(input())
for test_case in range(1, T+1):

    N, K = map(int, input().split())
    board = [''.join(input().split()) for _ in range(N)]

    Ks = '1'*K  
    cnt = 0     

    for i in range(N):
        checkK(board[i])

    for i in range(N):
        col = ''
        for j in range(N):
            col += board[j][i]
        checkK(col)


    print('#{} {}'.format(test_case, cnt))