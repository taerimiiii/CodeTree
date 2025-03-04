# 말이 가는 순서를 정하는 함수

# answer에 추가조건 -> 인덱스가 이미 있으면 추가하지 않는다. 인덱스가 없으면 추가한다.
def choose(curr_index) :
    global max_score, k

    if curr_index == n :
        # 말 이동시키고 점수 계산해서 점수 최댓값 갱신시키기
        score = get_score()
        max_score = max(score, max_score)
        return
    
    # 리스트 n개에 k번까지 수를 넣기
    for i in range(1, k + 1) :
        #if curr_index == 0 :
        answer.append(i)
            #index_list.append(i)
        choose(curr_index + 1)
        answer.pop()
            #index_list.pop()
        
        #elif i not in index_list :
        #   answer.append(i)
        #    index_list.append(i)
        #    choose(curr_index + 1)
        #    answer.pop()
        #    index_list.pop()
        
    
    return

def get_score() :
    global n

    #print(answer)
    curr_num_by_bot = [1] * k
    for i in range(n) :
        curr_num_by_bot[answer[i] - 1] += n_list[i]
    
    score = 0
    for elem in curr_num_by_bot :
        if elem >= m :
            score += 1
    
    #print(answer)
    #print(curr_num_by_bot)
    return score

n, m, k = map(int, input().split())
n_list = list(map(int, input().split()))


# 말의 현재 칸 (말 k개)
curr_num_by_bot = [1] * k

# 말이 움직이는 순서(k)
answer = []

max_score = 0

choose(0)

print(max_score)