# 아이디어
## https://velog.io/@ju_h2/Python-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-level2-%EA%B0%80%EC%9E%A5-%ED%81%B0-%EC%A0%95%EC%82%AC%EA%B0%81%ED%98%95-%EC%B0%BE%EA%B8%B0-%EB%8F%99%EC%A0%81-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D-dp

# 예상 시간복잡도
##

# 풀이시간 
## 30분

# 실행시간 
## 0.01ms~ 417.60ms

def solution(board):
    dp = [[0] * len(board[0]) for _ in range(len(board))]
    
    dp[0] = board[0]
    
    for i in range(1, len(board)):
        dp[i][0] = board[i][0]
    
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
    
    # 가장 큰 값 찾기
    max_value = 0
    for i in range(len(board)):
        max_value = max(max_value, max(dp[i]))
    
    return max_value ** 2