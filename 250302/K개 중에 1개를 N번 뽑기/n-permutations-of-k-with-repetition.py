def choose(curr_num) :
    global n
    if curr_num == n + 1 :
        print_answer()
        return
    
    for i in range(1, k+1) :
        answer.append(i)
        choose(curr_num + 1)
        answer.pop()
    
    return

def print_answer() :
    for elem in answer :
        print(elem, end = ' ')
    print()

k, n = map(int, input().split())
answer = []

choose(1)