n, t = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr3 = list(map(int, input().split()))

for time in range(t) :
    temp1 = arr1[n-1]
    temp2 = arr2[n-1]
    temp3 = arr3[n-1]
    
    for i in range(n-1, 0, -1) :
        arr1[i] = arr1[i-1]
        arr2[i] = arr2[i-1]
        arr3[i] = arr3[i-1]
    
    arr1[0] = temp3
    arr2[0] = temp1
    arr3[0] = temp2

arr = [arr1, arr2, arr3]
for i in range(3) :
    for j in range(n) :
        print(arr[i][j], end = ' ')
    print()
