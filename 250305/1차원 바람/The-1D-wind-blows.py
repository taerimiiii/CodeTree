def get_wind(r, d) :
    if d == 'L' :
        temp = arr[r][m - 1]
        for i in range(m - 1, 0, -1) :
            arr[r][i] = arr[r][i - 1]
        arr[r][0] = temp
    else :
        temp = arr[r][0]
        for i in range(0, m - 1) :
            arr[r][i] = arr[r][i + 1]
        arr[r][m - 1] = temp

def up_extend(r, d) :
    while in_range(r - 1) :
        success = 0
        for i in range(m) :
            if arr[r][i] == arr[r - 1][i] :
                success = 1
                r, d = r - 1, get_direct(d)
                get_wind(r, d)
                break
        if not success :
            break

def down_extend(r, d) :
    while in_range(r + 1) :
        success = 0
        for i in range(m) :
            if arr[r][i] == arr[r + 1][i] :
                success = 1
                r, d = r + 1, get_direct(d)
                get_wind(r, d)
                break
        if not success :
            break
        

def in_range(row) :
    if row >= 0 and row < n :
        return 1
    return 0

def get_direct(d) :
    if d == 'R' :
        return 'L'
    else :
        return 'R'

n, m, q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
wind_list = [list(input().split()) for _ in range(q)]

for i in range(q) :
    r, d = wind_list[i]
    r = int(r) - 1
    get_wind(r, d)
    up_extend(r, d)
    down_extend(r, d)

for i in range(n) :
    for j in range(m) :
        print(arr[i][j], end = ' ')
    print()