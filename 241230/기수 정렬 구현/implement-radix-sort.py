def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n  # 정렬된 결과를 저장할 배열
    count = [0] * 10  # 0~9까지 숫자의 빈도를 저장할 배열

    # 해당 자리수의 숫자 개수를 카운트
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # 누적 합 계산
    for i in range(1, 10):
        count[i] += count[i - 1]

    # 결과 배열 생성 (안정 정렬 유지)
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # 원본 배열에 정렬된 결과 복사
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    # 배열에서 최대값을 찾아 자릿수 결정
    max_val = max(arr)
    exp = 1  # 1의 자리부터 시작

    # 최대 자릿수까지 반복
    while max_val // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

n = int(input())
arr = list(map(int, input().split()))
radix_sort(arr)


for i in range(n) :
    print(arr[i], end = ' ')