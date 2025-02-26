def get_blockstop_row(n, m, k) :
    for row in range(n-1) :
        for col in range(k-1, k+m-1) :
            if arr[row+1][col] == 1 :
                return row
    return row+1 

def block_on(row, m, k) :
    for col in range(k-1, k+m-1) :
        arr[row][col] = 1

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 아래에 1이 있다면 그 행을 리턴
row = get_blockstop_row(n, m, k)

# [구한 행][열 m만큼 반복] 하면서 1로 채우기
block_on(row, m, k)

for i in range(n) :
    for j in range(n) :
        print(arr[i][j], end = ' ')
    print()