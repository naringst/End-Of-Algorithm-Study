# 아이디어
## BFS로 탐색하면서 방문횟수 누적 -> 이미 방문한 경로로 오는 경우는 최솟값이 아니므로 제외

# 예상 시간복잡도
## O(n * m)

# 풀이시간 
## 60분

# 실행시간 
## 0.01ms~ 0.06ms

from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dq = deque()
    
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    dq.append([0, 0])


    while dq:
        y, x= dq.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                dq.append([ny, nx])

    if maps[-1][-1] == 1:
        return -1
    return maps[-1][-1]
        
