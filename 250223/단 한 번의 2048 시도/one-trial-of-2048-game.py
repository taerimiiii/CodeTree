# 합쳐지는 함수
def add_block(direct) :
    if direct == 'R' :
        for i in range(4) :
            for j in range(3, 0, -1) :
                if arr[i][j] == arr[i][j - 1] :
                    arr[i][j] = arr[i][j] * 2
                    arr[i][j - 1] = 0
    
    elif direct == 'L' :
        for i in range(4) :
            for j in range(0, 3, 1) :
                if arr[i][j] == arr[i][j + 1] :
                    arr[i][j] = arr[i][j] * 2
                    arr[i][j + 1] = 0
    
    elif direct == 'U' :
        for j in range(4) :
            for i in range(0, 3, 1) :
                if arr[i][j] == arr[i + 1][j] :
                    arr[i][j] = arr[i][j] * 2
                    arr[i + 1][j] = 0
    
    else :
        for j in range(4) :
            for i in range(3, 0, -1) :
                if arr[i][j] == arr[i - 1][j] :
                    arr[i][j] = arr[i][j] * 2
                    arr[i - 1][j] = 0


# 중력이 작용하는 함수
def get_gravity(direct) :
    if direct == 'R' :
        for i in range(4) :
            temp = [0] * 4
            end_of_temp_arr = 0
            for j in range(3, -1, -1) :
                if arr[i][j] != 0 :
                    temp[end_of_temp_arr] = arr[i][j]
                    end_of_temp_arr += 1
            for k in range(4) :
                arr[i][k] = temp[4 - k - 1]
    
    elif direct == 'L' :
        for i in range(4) :
            temp = [0] * 4
            end_of_temp_arr = 0
            for j in range(0, 4, 1) :
                if arr[i][j] != 0 :
                    temp[end_of_temp_arr] = arr[i][j]
                    end_of_temp_arr += 1
            for k in range(4) :
                arr[i][k] = temp[k]
    
    elif direct == 'U' :
        for j in range(4) :
            temp = [0] * 4
            end_of_temp_arr = 0
            for i in range(0, 4, 1) :
                if arr[i][j] != 0 :
                    temp[end_of_temp_arr] = arr[i][j]
                    end_of_temp_arr += 1
            for k in range(4) :
                arr[k][j] = temp[k]
    
    else :
        for j in range(4) :
            temp = [0] * 4
            end_of_temp_arr = 0
            for i in range(3, -1, -1) :
                if arr[i][j] != 0 :
                    temp[end_of_temp_arr] = arr[i][j]
                    end_of_temp_arr += 1
            for k in range(4) :
                arr[k][j] = temp[4 - k - 1]


arr = [list(map(int, input().split())) for _ in range(4)]
direct = input()

get_gravity(direct)
add_block(direct)
get_gravity(direct)

for i in range(4) :
    for j in range(4) :
        print(arr[i][j], end = ' ')
    print()