# 아이디어
## 주석 참고

# 예상 시간복잡도
## O(N^2logN)

# 풀이시간 
## 3분

# 실행시간 
## 0.00ms~ 0.01ms

def solution(array, commands):
    answer = []
    
    # i 번째 숫자부터 j 번쨰 숫자까지 자르고 정렬, k 번째 있는 수 구하기
    for command in commands:
        i, j, k = command
        
        # i~j 까지 자르기
        slice_list = array[i-1:j]
        
        # 정렬하기
        slice_list.sort()
        
        # k 번째 수 반환
        answer.append(slice_list[k-1])
    return answer