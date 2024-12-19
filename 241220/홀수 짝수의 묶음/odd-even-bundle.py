def max_groups(n, numbers):
    # 짝수와 홀수 분리
    evens = [num for num in numbers if num % 2 == 0]
    odds = [num for num in numbers if num % 2 == 1]
    
    # 짝수와 홀수의 개수
    even_count = len(evens)
    odd_count = len(odds)
    
    # 묶음 계산
    groups = 0
    current_even = True  # 첫 번째 묶음은 짝수
    
    while even_count > 0 or odd_count > 0:
        if current_even:  # 짝수 묶음 구성
            if even_count > 0:  # 짝수 하나 사용
                even_count -= 1
                groups += 1
            elif odd_count >= 2:  # 홀수 2개로 짝수 합 만들기
                odd_count -= 2
                groups += 1
            else:  # 더 이상 짝수를 만들 수 없음
                break
        else:  # 홀수 묶음 구성
            if odd_count >= 1:  # 홀수 하나 사용
                odd_count -= 1
                groups += 1
            else:  # 더 이상 홀수를 만들 수 없음
                break
        
    if even_count < 0 or odd_count < 0 :
        # 묶음 계산
        groups = 0
        current_even = True  # 첫 번째 묶음은 짝수
    
        while even_count > 0 or odd_count > 0:
            if current_even:  # 짝수 묶음 구성
                if even_count > 0:  # 짝수 하나 사용
                    even_count -= 1
                    groups += 1
                elif odd_count >= 2:  # 홀수 2개로 짝수 합 만들기
                    odd_count -= 2
                    groups += 1
                else:  # 더 이상 짝수를 만들 수 없음
                    break
            else:  # 홀수 묶음 구성
                if odd_count >= 3:  # 홀수 셋 사용
                    odd_count -= 3
                    groups += 1
                elif odd_count >= 1 :   # 홀수 하나 사용
                    odd_count -= 1
                    groups += 1
                else:  # 더 이상 홀수를 만들 수 없음
                    break

    if even_count < 0 or odd_count < 0 :
        # 묶음 계산
        groups = 0
        current_even = True  # 첫 번째 묶음은 짝수
    
        while even_count > 0 or odd_count > 0:
            if current_even:  # 짝수 묶음 구성
                if even_count > 0:  # 짝수 하나 사용
                    even_count -= 1
                    groups += 1
                elif odd_count >= 4:  # 홀수 4개로 짝수 합 만들기
                    odd_count -= 4
                    groups += 1
                elif odd_count >= 2:  # 홀수 2개로 짝수 합 만들기
                    odd_count -= 2
                    groups += 1
                else:  # 더 이상 짝수를 만들 수 없음
                    break
            else:  # 홀수 묶음 구성
                if odd_count >= 1:  # 홀수 하나 사용
                    odd_count -= 1
                    groups += 1
                elif odd_count >= 3:  # 홀수 셋 사용
                    odd_count -= 3
                    groups += 1
                else:  # 더 이상 홀수를 만들 수 없음
                    break

        
        # 다음 묶음은 반대 (짝수 → 홀수 → 짝수 → ...)
        current_even = not current_even
    
    return groups

# 입력 처리
n = int(input())
numbers = list(map(int, input().split()))

# 결과 출력
print(max_groups(n, numbers))
