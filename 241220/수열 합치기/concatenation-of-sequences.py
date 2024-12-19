n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr = [0] * (n + m)

for i in range(n) :
    arr[i] = arr1[i]

for i in range(m) :
    arr[n + i] = arr2[i]

arr.sort()

for elem in arr :
    print(elem, end = ' ')