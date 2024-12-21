n = int(input())
arr = [[0] * 2 for _ in range(n)]
for i in range(n) :
    arr[i][0], arr[i][1] = map(int, input().split())

min_dis = 100
for k in range(n) :
    min_x = 100
    max_x = 1

    for i in range(n) :
        for j in range(2) :
            if k == i :
                continue
        
            min_x = min(arr[i][j], min_x)
            max_x = max(arr[i][j], max_x)

    dis = max_x - min_x
    min_dis = min(dis, min_dis)

print(min_dis)