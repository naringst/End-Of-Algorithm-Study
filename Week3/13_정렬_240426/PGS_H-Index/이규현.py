## 아이디어
# 경우의 수를 잘 구분해야함

## 시간 복잡도
# O(n)

## 시간
# 0.01ms - 0.55ms

## 푼 시간
# 40분

def solution(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    
    for i in range(n):
        if citations[i] >= (n-i): # 999횟수 이상 논문이 3편인 경우
            answer = max(answer,n-i)
        else:
            answer = max(answer, citations[i]) # 4횟수 이상 논문이 5편인 경우
    
    return answer
