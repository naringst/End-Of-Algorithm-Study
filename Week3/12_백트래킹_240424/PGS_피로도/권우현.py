# 아이디어
## 

# 예상 시간복잡도
##

# 풀이시간 
## 분

# 실행시간 
## ms~ ms


answer = 0

def dfs(visited, dungeons, k, cnt):
    global answer
    if cnt>answer:
        answer = cnt

    for i in range(len(dungeons)):
        if not visited[i] and k>=dungeons[i][0]:
            visited[i] = True
            dfs(visited, dungeons, k-dungeons[i][1], cnt + 1)
            visited[i] = False



def solution(k, dungeons):

    visited = [False] * len(dungeons)


    dfs(visited, dungeons, k,0)

    return answer




print(solution(80, [[80, 20], [50, 40], [30, 10]]))
