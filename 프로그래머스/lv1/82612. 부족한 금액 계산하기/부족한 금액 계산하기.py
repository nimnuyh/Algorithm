def solution(price, money, count):
    need = price * sum(range(1, count + 1))
    a = need - money
    if a <= 0 :
        answer = 0
    else :
        answer = a
    return answer