# 아이디어
## # 반복
## 모든 0 제거 -> 1의 개수 카운트
## 그 수를 2진수로 표현
## 1인지 확인

# 예상 시간복잡도
## O(N)

# 풀이시간 
## 12분

# 실행시간 
## 0.01ms~ 0.49ms

def solution(s):    
    # 반복 횟수 카운트
    count = 0
    # 제거한 0 수
    remove_zero = 0

    while s != "1":
        s_len = s.count("1")
        remove_zero += len(s) - s_len
        count += 1
        s = bin(s_len)[2:]
    return [count, remove_zero]