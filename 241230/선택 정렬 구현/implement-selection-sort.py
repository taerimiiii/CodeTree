def selection_sort(arr, n) :
    for i in range(0, n-1) :
        min_val = arr[i]
        idx = i
        for j in range(i+1, n) :
            if arr[j] < min_val :
                min_val = arr[j]
                idx = j
        temp = arr[idx]
        arr[idx] = arr[i]
        arr[i] = temp
        

n = int(input())
arr = list(map(int, input().split()))

selection_sort(arr, n)

for i in range(n) :
    print(arr[i], end = ' ')