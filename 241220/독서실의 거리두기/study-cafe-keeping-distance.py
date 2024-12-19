n = int(input())
string = input()

arr = ['0'] * n
for i in range(n) :
    arr[i] = string[i]

max_ans = 0
for i in range(n - 1) :
    if arr[i] == '1' :
        continue
    arr[i] = '1'

    for j in range(i + 1, n) :
        if arr[j] == '1' :
            continue
        arr[j] = '1'

        min_dis = 100000
        for k in range(n- 1) :
            if arr[k] == '1' :
                for l in range(k + 1, n) :
                    if arr[l] == '1' :
                        dis = l - k
                        break;
                min_dis = min(min_dis, dis)
        
        max_ans = max(min_dis, max_ans)

        #if i == 2 :
         #   print(arr, max_ans)
        arr[j] = '0'

    arr[i] = '0'

print(max_ans)