# 말이 가는 순서를 정하는 함수
def choose(curr_index) :
    global max_score, k

    if curr_index == n :
        # 말 이동시키고 점수 계산해서 점수 최댓값 갱신시키기
        score = get_score()
        max_score = max(score, max_score)
        return
    
    # answer리스트 n개에 k번까지 수를 넣기 (중복O)
    for i in range(1, k + 1) :
        answer.append(i)
        choose(curr_index + 1)
        answer.pop()        
    return

def get_score() :
    global n

    curr_num_by_bot = [1] * k
    for i in range(n) :
        curr_num_by_bot[answer[i] - 1] += n_list[i]
    
    score = 0
    for elem in curr_num_by_bot :
        if elem >= m :
            score += 1
    
    return score

n, m, k = map(int, input().split())
n_list = list(map(int, input().split()))

curr_num_by_bot = [1] * k # 말의 현재 칸 (말 k개)
answer = [] # 말이 움직이는 순서(말 k개)
max_score = 0
choose(0)
print(max_score)