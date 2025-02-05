# 올바르지 않은 기울어진 직사각형의 정보가 주어지는 경우는 없다.
# 만약 있다면 in_range를 적절히 활용할 것.

def move(meter, x, y, temp, move_direct) :
    x, y = x+dxs[move_direct]*meter, y+dys[move_direct]*meter
    return_temp = arr[x][y]

    list_direct = (move_direct + 2) % 4

    for i in range(meter) :
        if i == meter - 1 :
            arr[x][y] = temp
        else :
            nx, ny = x + dxs[list_direct], y + dys[list_direct]
            arr[x][y] = arr[nx][ny]
        x, y = x + dxs[list_direct], y + dys[list_direct]
    
    x, y = x+dxs[move_direct]*meter, y+dys[move_direct]*meter
    move_direct = (move_direct + 1) % 4
    return x, y, return_temp, move_direct

def get_dxdy(direct) :
    if direct :
        dxs, dys = [-1, -1, 1, 1], [-1, 1, 1, -1]
    else :
        dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
    return dxs, dys

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
row, col, m1, m2, m3, m4, direct = map(int, input().split())

x, y = row-1, col-1
dxs, dys = get_dxdy(direct)
move_direct = 0
temp = arr[x][y]

order = [m4, m3, m2, m1] if direct else [m1, m2, m3, m4]

for m in order:
    x, y, temp, move_direct = move(m, x, y, temp, move_direct)

for i in range(n) :
    for j in range(n) :
        print(arr[i][j], end = ' ')
    print()