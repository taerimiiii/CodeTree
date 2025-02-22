def in_range(x, y) :
    global n
    if x >= 0 and x < n and y >= 0 and y < n :
        return 1
    return 0


def get_bomb_block(n, arr, r, c) :
    r, c = r - 1, c - 1
    bomb = arr[r][c]
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    for direct in range(4) :
        x, y = r, c
        for count in range(bomb) :
            arr[x][y] = 0
            nx, ny = x + dxs[direct], y + dys[direct]
            if not in_range(nx, ny) :
                break
            x, y = x + dxs[direct], y + dys[direct]


def get_down_block(n, arr) :
    for j in range(n) :
        temp = [0] * n
        end_of_temp_arr = 0
        for i in range(n - 1, -1, -1) :
            if arr[i][j] != 0 :
                temp[end_of_temp_arr] = arr[i][j]
                end_of_temp_arr += 1
        copy(j, temp)


def copy(j, temp) :
    for i in range(len(temp)) :
        arr[i][j] = temp[n - i - 1]


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

get_bomb_block(n, arr, r, c)
get_down_block(n, arr)

for i in range(n) :
    for j in range(n) :
        print(arr[i][j], end = ' ')
    print()