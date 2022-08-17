T =int(input())
for test_case in range(T):
    t = input()
    if int(t[5]) in [1,3,5,7,8] and int(t[6:]) < 32:
        year = t[0:4]
        month = t[4:6]
        day = t[6:]
        d = year + "/" + month + "/" + day
        print("#{} {}".format(test_case+1, d))
    elif int(t[4:6]) in [10,12] and int(t[6:]) < 32:
        year = t[0:4]
        month = t[4:6]
        day = t[6:]
        d = year + "/" + month + "/" + day
        print("#{} {}".format(test_case+1, d))
    elif int(t[5]) in [4,6,9] and int(t[6:]) < 31:
        year = t[0:4]
        month = t[4:6]
        day = t[6:]
        d = year + "/" + month + "/" + day
        print("#{} {}".format(test_case+1, d))
    elif int(t[4:6]) == 11 and int(t[6:]) < 31:
        year = t[0:4]
        month = t[4:6]
        day = t[6:]
        d = year + "/" + month + "/" + day
        print("#{} {}".format(test_case+1, d))
    elif int(t[5]) == 2 and int(t[6:]) < 29:
        year = t[0:4]
        month = t[4:6]
        day = t[6:]
        d = year + "/" + month + "/" + day
        print("#{} {}".format(test_case+1, d))
    else:
        d = -1
        print("#{} {}".format(test_case+1, d))