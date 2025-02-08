def pop_block(s, e, arr) :
    for i in range(s-1, e) :
        arr[i] = 0
    
    end_of_arr = len(arr)
    end_of_temp_arr = 0
    temp = []
    for elem in arr :
        if elem != 0 :
            temp.append(elem)

    return temp

n = int(input())
arr = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

arr = pop_block(s1, e1, arr)
arr = pop_block(s2, e2, arr)

print(len(arr))
for elem in arr :
    print(elem)