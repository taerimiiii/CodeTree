def choose(curr_cnt) :
    global n

    if curr_cnt == n + 1 :
        printing()
        return
    
    for select in range(1, k + 1) :
        if (curr_cnt == 1 or curr_cnt == 2) or (curr_cnt >= 3 and answer[-1] != select) or (curr_cnt >= 3 and answer[-2] != select) :
            answer.append(select)
            choose(curr_cnt + 1)
            answer.pop()

    return

def printing() :
    global n
    for i in range(n) : 
        print(answer[i], end = ' ')
    print()



k, n = map(int, input().split())
answer = []
choose(1)