# 아이디어
## 

# 예상 시간복잡도
##

# 풀이시간 
## 분

# 실행시간 
## ms~ ms

answer = 10
# n, weak, dist = 12, [1, 5, 6, 10], [1, 2, 3, 4]
# n, weak, dist = 12, [1, 3, 4, 9, 10],	[3, 5, 7]
n, weak, dist = 200, [0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30]
dist.sort(reverse=True)

def solution(n, weak, dist):
    visited = set()
    dfs(n, weak, dist, visited, 0)
    if answer==10:
        return -1
    return answer



def dfs(n, weak, dist, visited, i):
    global answer
    if i > answer:
        return
    if len(visited)==len(weak):
        answer = min(answer, i)
        return
    if i >= len(dist):
        return
    for j in range(len(weak)):
        if weak[j] in visited:
            continue
        #반시계
        #12시 안지남
        start = weak[j]
        if start-dist[i]>0:
            end = start-dist[i]
        #점검하기
            for k in range(len(weak)):
                if end <= weak[k] <= start and not weak[k] in visited:
                    visited.add(weak[k])
        #12시 지남
        else:
            end = n-dist[i]+start
            for k in range(len(weak)):
                if end <= weak[k] <n or 0<= weak[k]<=start and not weak[k] in visited:
                    visited.add(weak[k])
        dfs(n, weak, dist, visited, i+1)

        #점검 취소
        if start-dist[i]>0:
            end = start-dist[i]
            for k in range(len(weak)):
                if end <= weak[k] <= start and weak[k] in visited:
                    visited.remove(weak[k])
        #12시 지남
        else:
            end = n-dist[i]+start
            for k in range(len(weak)):
                if (end <= weak[k] <n or 0<= weak[k]<=start) and weak[k] in visited:
                    visited.remove(weak[k])

        #시계로 돌면
        #12시 안지남
        if start+dist[i]<n:
            end = start+dist[i]
            for k in range(len(weak)):
                if start <= weak[k] <= end:
                    visited.add(weak[k])
        else :
            end = dist[i]+start-n
            for k in range(len(weak)):
                if start<=weak[k] <n or 0<= weak[k]<=end:
                    visited.add(weak[k])
        dfs(n, weak, dist, visited, i+1)
        if start+dist[i]<n:
            end = start+dist[i]
            for k in range(len(weak)):
                if start <= weak[k] <= end and weak[k] in visited:
                    visited.remove(weak[k])
        else :
            end = dist[i]+start-n
            for k in range(len(weak)):
                if (start<=weak[k] <n or 0<= weak[k]<=end) and weak[k] in visited:
                    visited.remove(weak[k])


print(solution(n, weak, dist))