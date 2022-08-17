
N = int(input())
x = map(int, input().split())

x = list(x)

x = sorted(x)

print(x[int((N - 1) / 2)])