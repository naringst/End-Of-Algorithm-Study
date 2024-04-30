# 아이디어
## 

# 예상 시간복잡도
##

# 풀이시간 
## 8분

# 실행시간 
## 0.01ms~ 50.73ms

def solution(triangle):
    dp = triangle.copy()
    depth = len(triangle)-1
    # 아래에서부터 올라가면서 가장 큰 합으로 골라 올라가기
    for i in range(1, len(triangle)):
        # dp[x][y] 는 triangle[x][y] + max(dp[x+1][y], dp[x+1][y+1])
        for j in range(len(triangle[depth-i])):
            dp[depth-i][j] = triangle[depth-i][j] + max(dp[depth-i+1][j], dp[depth-i+1][j+1])
    return dp[0][0]

