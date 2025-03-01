# 폭발 칸을 찾는 함수
def get_block(col) :
    global n
    for row in range(n) :
        if arr[row][col] != 0 :
            return row
    return n

# 폭발 동작 함수
def pop_block(row, col) :
    x, y = row, col
    pop_num = arr[x][y]
    arr[x][y] = 0
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    for dx, dy in zip(dxs, dys) :
        x, y = row, col
        for count in range(pop_num-1) :
            x, y = x+dx, y+dy
            if in_range(x, y) :
                arr[x][y] = 0
            else :
                break

def in_range(x, y) :
    global n
    if x >= 0 and x < n and y >= 0 and y < n :
        return 1
    return 0

# 중력이 작용하는 함수
def gravity(n) :
    for col in range(n) :
        temp = [0] * n
        end_of_temp_arr = 0
        for row in range(n-1, -1, -1) :
            if arr[row][col] != 0 :
                temp[end_of_temp_arr] = arr[row][col]
                end_of_temp_arr += 1
        copy(temp, col)

def copy(temp, col) :
    for i in range(n) :
        arr[i][col] = temp[n-i-1]

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cols = [int(input()) for _ in range(m)]

for i in range(m) :
    col = cols[i] - 1
    row = get_block(col)
    if row != n :
        pop_block(row, col)
        gravity(n)


for i in range(n) :
    for j in range(n) :
        print(arr[i][j], end = ' ')
    print()