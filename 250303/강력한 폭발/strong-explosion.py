# 터질 폭탄의 종류를 선택하는 함수
def choose(curr_cnt) :
    global max_pop_block_cnt, bomb_cnt

    if curr_cnt == bomb_cnt :
        #print(choose_list)
        #printing(n)
        pop_block_cnt = get_pop_block_cnt()
        max_pop_block_cnt = max(max_pop_block_cnt, pop_block_cnt)
        return
    
    for select in range(1, 4) :
        choose_list.append(select)
        #x, y = bomb_xy_list[curr_cnt]
        #pop_block(select, x, y)
        choose(curr_cnt + 1)
        #back_block(select, x, y)
        choose_list.pop()

    return

# 초토화 된 칸 개수를 구하는 함수
def get_pop_block_cnt() :

    for i in range(bomb_cnt) :
        x, y = bomb_xy_list[i]
        pop_block(choose_list[i], x, y)
    
    
    pop_block_cnt = 0
    for i in range(n) :
        for j in range(n) :
            if arr[i][j] != 0 :
                pop_block_cnt += 1
    
    for i in range(bomb_cnt) :
        x, y = bomb_xy_list[i]
        back_block(choose_list[i], x, y)
    
    return pop_block_cnt

# 선택한 폭탄에 따라 초토화 되는 칸
def pop_block(select, x, y) :
    if select == 1:
        for dx in [-2, -1, 1, 2]:
            if in_range(x + dx, y) and arr[x + dx][y] == 0:
                arr[x + dx][y] = 2
    elif select == 2 :
        for dx, dy in zip([-1, 0, 1, 0], [0, 1, 0, -1]) :
            if in_range(x + dx, y + dy) and arr[x + dx][y + dy] == 0:
                arr[x + dx][y + dy] = 2
    else :
        for dx, dy in zip([-1, 1, 1, -1], [1, 1, -1, -1]) :
            if in_range(x + dx, y + dy) and arr[x + dx][y + dy] == 0:
                arr[x + dx][y + dy] = 2
        
def in_range(x, y) :
    global n
    if x >= 0 and x < n and y >= 0 and y < n :
        return 1
    return 0

# 초토화 된 칸을 원래대로 되돌리는 함수
def back_block(select, x, y) :
    if select == 1:
        for dx in [-2, -1, 1, 2]:
            if in_range(x + dx, y) and arr[x + dx][y] == 2:
                arr[x + dx][y] = 0
    elif select == 2 :
        for dx, dy in zip([-1, 0, 1, 0], [0, 1, 0, -1]) :
            if in_range(x + dx, y + dy) and arr[x + dx][y + dy] == 2:
                arr[x + dx][y + dy] = 0
    else :
        for dx, dy in zip([-1, 1, 1, -1], [1, 1, -1, -1]) :
            if in_range(x + dx, y + dy) and arr[x + dx][y + dy] == 2:
                arr[x + dx][y + dy] = 0

# 폭탄의 개수를 구하는 함수
def get_bomb_cnt(n) :
    bomb_cnt = 0
    for i in range(n) :
        for j in range(n) :
            if arr[i][j] == 1 :
                bomb_cnt += 1
    return bomb_cnt

# 폭탄의 위치를 구하는 함수
def get_bomb_location(bomb_cnt, n) :
    bomb_xy_list = [[0, 0] for _ in range(bomb_cnt)]
    index = 0
    for i in range(n) :
        for j in range(n) :
            if arr[i][j] == 1 :
                bomb_xy_list[index][0], bomb_xy_list[index][1] = i, j
                index += 1
    return bomb_xy_list

def printing(n) :
    for i in range(n) :
        for j in range(n) :
            print(arr[i][j], end = ' ')
        print()
    print()

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

bomb_cnt = get_bomb_cnt(n)
bomb_xy_list = get_bomb_location(bomb_cnt, n)

max_pop_block_cnt = 0
choose_list = []
choose(0)

print(max_pop_block_cnt)