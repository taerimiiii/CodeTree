def move(n, r, c) :
    dxs, dys = [1, -1, 0, 0], [0, 0, -1, 1]
    x, y = r, c

    for dx, dy in zip(dxs, dys) :
        if in_range(x+dx, y+dy) and arr[x+dx][y+dy] > arr[x][y] :
            print(arr[x][y], end = ' ')
            x, y = x+dx, y+dy
            return 1, x, y
    return 0, x, y

def in_range(x, y) :
    global n
    if x >= 0 and x < n and y >= 0 and y < n :
        return 1
    return 0

n, r, c = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
success = 1
r -= 1
c -= 1

while success :
    success, r, c = move(n, r, c)

print(arr[r][c])