# 아이디어
## 0,0의 위치에서부터 지나갈 수 있는 모든 경로를 지나가면서 현재까지의 경로 수를 센다
## 최단거리를 탐색하는 것이기 때문에 bfs를 활용한다

# 예상 시간복잡도
## 최대 O(n*m)?

# 풀이시간 
## 25분

# 실행시간 
## 0.01ms~ 8.94ms

from collections import deque
def bfs(visited, q,n,m,maps):
    while q :
        x,y = q.popleft()
        
        if x == n-1 and y == m-1 :
            return visited[n-1][m-1] 
            
        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)] :
            nx = x + dx
            ny = y + dy
            if 0<= nx < n and 0<= ny < m :
                if not visited[nx][ny] and maps[nx][ny] == 1 :
                    q.append([nx,ny])
                    visited[nx][ny] = visited[x][y] + 1 
    
def solution(maps):
    q = deque([[0,0]])
    visited = [[0]*len(maps[0]) for _ in range(len(maps))]
    visited[0][0] = 1
    n = (len(maps))
    m = len(maps[0])
    
    answer = bfs(visited,q,n,m,maps)
    
    if answer is None:
        answer = -1
    return answer