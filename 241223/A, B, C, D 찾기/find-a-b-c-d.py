arr = list(map(int, input().split()))

a = min(arr)
arr.remove(a)

b = min(arr)
arr.remove(b)

c = min(arr)
arr.remove(c)

abcd = max(arr)

d = abcd - a - b - c

print(a, b, c, d)