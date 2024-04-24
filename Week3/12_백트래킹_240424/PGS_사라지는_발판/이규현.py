# 아이디어
## BFS를 돌며 최솟값 갱산 -> BFS + DP

# 예상 시간복잡도
## ???

# 풀이시간 
## 120분

# 실행시간 
## 0.03ms~ 96.61ms

from collections import deque
def solution(board):
    
    def bfs(start):
        n = len(board)
        visit = [[10000000 for _ in range(n)] for _ in range(n)]
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        dq = deque([start])
        visit[0][0] = 0

        while dq:
            y, x, cost, cur_dir = dq.popleft()
            for i in range(4):
                nx = x + dx[i] 
                ny = y + dy[i]

                if 0 <= nx < n and 0<= ny < n and board[ny][nx] == 0:
                    if cur_dir != i: # 방향이 바뀌는 경우
                        ncost = cost + 600
                    else:
                        ncost = cost + 100
                    if visit[ny][nx] >= ncost:
                        visit[ny][nx] = ncost
                        dq.append([ny, nx, ncost, i])

        return visit[-1][-1]

    return min(bfs((0,0,0,0)), bfs((0,0,0,1)))
