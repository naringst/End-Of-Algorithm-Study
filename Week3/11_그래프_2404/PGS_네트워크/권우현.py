# 아이디어
## 

# 예상 시간복잡도
##

# 풀이시간 
## 분

# 실행시간 
## ms~ ms
n, computers = 5, [[1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 0, 1, 0, 1], [1, 0, 0, 1, 1], [0, 0, 1, 1, 1]]

answer = 0

def dfs(computers, i, visit):
    visited[i] = True
    for j in range(len(computers)):
        if i != j and computers[i][j] == 1 and not visit[j]:
            dfs(computers, j, visit)


visited = [False for _ in range(n)]

for i in range(n):
    if not visited[i]:
        dfs(computers, i, visited)
        answer += 1

print(answer)