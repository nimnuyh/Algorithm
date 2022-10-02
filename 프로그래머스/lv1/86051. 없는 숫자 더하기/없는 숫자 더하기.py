def solution(numbers):
    n_list = list(range(10))
    for i in numbers :
        n_list.remove(i)
    answer = sum(n_list)
    return answer