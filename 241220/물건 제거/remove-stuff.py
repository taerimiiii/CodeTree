n = int(input())
arr_n = list(map(int, input().split()))
k = int(input())
arr_k = list(map(int, input().split()))

arr_n.sort(reverse=True)
arr_k.sort(reverse=True)

sec = 0
while len(arr_k) > 0 :
    sec += 1
    for i in range(n) :

        for j in range(len(arr_k)) :
            if arr_n[i] >= arr_k[j] :
                arr_k.pop(j)
                break

        #print(arr_k)


print(sec)