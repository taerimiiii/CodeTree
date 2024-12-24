def in_range(x, y) :
    if 0 <= x < n and 0 <= y < n :
        return 1
    return 0

n = int(input())
arr = [[0] * n for _ in range(n)]

dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

x, y = n-1, n-1
direct = 2
arr[y][x] = n*n
for i in range(n*n - 1, 0, -1) :
    nx = x + dxs[direct]
    ny = y + dys[direct]
    if not in_range(nx, ny) or arr[ny][nx] != 0:
        direct = (direct + 1) % 4
    
    x = x + dxs[direct]
    y = y + dys[direct]
    arr[y][x] = i


for i in range(n) :
    for j in range(n) :
        print(arr[i][j], end = ' ')
    print()