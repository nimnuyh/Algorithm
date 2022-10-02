def solution(absolutes, signs):
    answer = 0
    for n, b in zip(absolutes, signs) :
        if b == True :
            answer += n
        else :
            answer -= n
    return answer