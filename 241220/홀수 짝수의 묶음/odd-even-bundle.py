# 입력
n = int(input())
numbers = list(map(int, input().split()))

# 짝수와 홀수 분리
evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 == 1]
    
# 짝수와 홀수의 개수
even_count = len(evens)
odd_count = len(odds)
    
# 묶음 계산
groups = 0
current_even = True  # 첫 번째 묶음은 짝수
    
# 최대갯수로 만들기 위해서는 짝수는 중요하지 않고 홀수가 중요함.
while odd_count > 0:
    if current_even:  # 짝수 묶음 구성
        if even_count > 0:  # 짝수 1개로 짝수 만들기
            even_count -= 1
            groups += 1
        else :  # 홀수 2개로 짝수 만들기
            odd_count -= 2
            groups += 1
    else:  # 홀수 묶음 구성
        odd_count -= 1 # 홀수 1개로 홀수 만들기. 홀수 1개 짝수 1개로 홀수 만들기는 짝수 갯수 여분은 능동적으로 처리 가능하므로 생략.
        groups += 1
                
    # 짝홀짝홀짝...
    current_even = not current_even
    #print(even_count, odd_count)
        
    
# 짝수가 하나라도 남는 경우는 홀수 그룹으로 while문 반복이 끝난 경우 뿐이다.
# 따라서 홀수 다음 짝수에 0(짝수)가 올 수 있으므로 그룹에 1을 추가한다.
if even_count > 0 :
    groups += 1

# 짝수 번째인데 홀수 하나만 남을 경우 = 짝홀짝 불가능
# 여분의 홀수 하나를 처리해 주기 위해선 짝홀 그룹이 각각 하나씩 필요함.
# 따라서 그룹에서 2를 빼준다.
if odd_count < 0 :
    groups -= 2


# 출력
print(groups)