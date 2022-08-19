def solution(s):
    num_dict = {}
    num_eng = 'zero one two three four five six seven eight nine'
    num_eng = list(num_eng.split())
    for i, v in zip(range(10), num_eng) :
        num_dict[v] = i
    for k, v in num_dict.items() :
        s = s.replace(k, str(v))
    
    return int(s)