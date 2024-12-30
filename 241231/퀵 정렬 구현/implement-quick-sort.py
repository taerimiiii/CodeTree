def partition(arr, low, high) :
    pivot, arr = select_pivot(arr, low, high)

    i = low - 1
    for j in range(low, high) :
        if arr[j] < pivot :
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i+1

def quick_sort(arr, low, high) :
    if low < high :
        pos = partition(arr, low, high)

        quick_sort(arr, low, pos-1)
        quick_sort(arr, pos+1, high)

def select_pivot(arr, low, high) :
    if high-low+1 <= 3 :
        pivot = arr[high]
    else :
        mid = (low + high) // 2
        min_val = min(arr[low], arr[mid], arr[high])
        max_val = max(arr[low], arr[mid], arr[high])
        if arr[low] != min_val and arr[low] != max_val :
            pivot = arr[low]
            arr[low], arr[high] = arr[high], arr[low]
        elif arr[mid] != min_val and arr[mid] != max_val :
            pivot = arr[mid]
            arr[mid], arr[high] = arr[high], arr[mid]
        else :
            pivot = arr[high]

    return pivot, arr


n = int(input())
arr = list(map(int, input().split()))

quick_sort(arr, 0, n-1)

for elem in arr :
    print(elem, end = ' ')