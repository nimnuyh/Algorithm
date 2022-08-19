n, m = map(int, input().split())
g_dict = {}
for _ in range(n) :
    name = input()
    members = []
    for i in range(int(input())) :
        member = input()
        members.append(member)
    members.sort()
    g_dict[name] = members

for _ in range(m) :
    q = input()
    k = int(input())
    if k == 1 :
        g_name = list(g_dict.keys())[(list(g_dict.values()).index([x for x in list(g_dict.values()) if q in x][0]))]
        print(g_name)
    else :
        g_member = g_dict[q]
        for member in g_member :
            print(member)