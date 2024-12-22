n = int(input())
arr = list(map(int, input().split()))

arr.sort()

# 2 5 7 9 10 15
min_dis = 1000000000
for i in range(n) :
    dis = abs(arr[i] - arr[n + i])
    min_dis = min(dis, min_dis)

print(min_dis)