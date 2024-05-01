# 아이디어
## https://velog.io/@imacoolgirlyo/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EB%8F%84%EB%91%91%EC%A7%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC

# 예상 시간복잡도
##

# 풀이시간 
## 50분

# 실행시간 
## 0.07ms~ 635.11ms

def solution(money):    
    # 이 문제가 선형이었을 때 정석 알고리즘에 다음 아래와 같은 규칙을 적용하면 풀립니다.
    # 경우1. 처음 집 포함, 마지막집 제외시 최적
    # 경우2. 처음 집 제외, 마지막집 포함시 최적
    # 정답 = 둘중 최대값
    
    dp = [0] * len(money)
    
    dp[0] = money[0]
    dp[1] = max(money[1], money[0]) # ?
    
    # 처음 집 포함, 마지막집 제외
    for i in range(2, len(money)-1):
        dp[i] = max(dp[i-1], dp[i-2] + money[i])
    # print(dp)
  
    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]
    # 처음 집 제외, 마지막집 포함
    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])
        
    # print(dp2)
    return max(max(dp), max(dp2))