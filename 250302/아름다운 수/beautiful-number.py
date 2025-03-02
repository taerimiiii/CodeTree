def choose(curr_len) :
    global n, cnt

    if curr_len == n :
        cnt += 1
        return
    
    elif curr_len > n :
        return
    
    for select in range(1, 5) : #(1, n+1)이면 숫자 제한 없을 때
        answer.append(select)
        choose(curr_len + select)
        answer.pop()
    
    return


n = int(input())
cnt = 0
answer = []

choose(0)

print(cnt)