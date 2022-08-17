s = input()
al = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
ans = 0
for a in al :
    ans += s.count(a)
    s = s.replace(a, ' ')
s = s.replace(' ', '')
ans += len(s)
print(ans)