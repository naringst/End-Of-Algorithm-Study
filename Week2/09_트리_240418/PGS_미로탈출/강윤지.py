# 아이디어
## S -> L + L -> E 각각 구해서 더해주었다.
## 최소 경로 문제이기에 BFS로 작성하였다. (DFS는 시간초과 발생)
## visited를 먼저 추가해주고(40번째 줄), for문 안의 if 문에서 방문했는지 확인해주었더니 시간초과가 발생했다
## 먼저 방문했는지 확인하고, 나중에 추가해주는 로직으로 수정하니 시간초과가 발생하지 않았다

# 예상 시간복잡도
##

# 풀이시간 
## 100분

# 실행시간 
## 0.06ms~ 5833.36ms

from collections import deque

def bfs(board, start, end):
    # 세로 길이
    len_r = len(board)
    # 가로 길이
    len_c = len(board[0])  
    
    start_r, start_c = start
    end_r, end_c = end
    queue = deque([(start_r, start_c, 0)])
    dr = [0, 0, -1, 1]
    dc = [1, -1, 0, 0]
    visited = []
    
    while queue:
        # queue에서 정보 가져오기
        r, c, count = queue.popleft()
        
        # 종료 조건 확인
        if r == end_r and c == end_c:
            return count
        
        # 방문을 하고, 다음 갈 곳을 방문 확인하는거 -> 시간초과
        # 먼저 체크 후, 방문하는 걸로 하자!
        # 일단 갔던 곳 visited에 넣기
        # visited.append((r, c))
        if (r, c) in visited:
            continue
        
        # 여기서 갈 수 있는 곳 다 넣기
        for i in range(4):
            visited.append((r, c))
            nr = r + dr[i]
            nc = c + dc[i]

            # 방문했는지 확인            
            # 나가는지 확인 & 갈 수 있는지 확인
            if 0<=nr<len_r and 0<=nc<len_c and (nr, nc) and board[nr][nc] != 'X':
                queue.append((nr, nc, count+1))

def solution(maps):
    # 통로로만 이동
    # 통로들 중 하나에 레버 존재
    # 레버 당긴 후, 미로를 빠져나가는 칸으로 이동
    # 레버 당기지 않았더라도 출구 칸 지나가기 가능
    
    # S -> L 먼저 구하기
    # L -> E 구하기
    
    # 일단 board 만들기
    # 레버, 입구, 출구 찾기
    labor = ()
    start = ()
    exit = ()
    board = []
    for idx, string in enumerate(maps):
        temp = list(string)
        # 여기서 레버, 입구, 출구 찾기
        if 'L' in temp:
            labor += (idx, temp.index('L'))
        if 'S' in temp:
            start += (idx, temp.index('S'))
        if 'E' in temp:
            exit += (idx, temp.index('E'))
        board.append(temp)
    
    temp = bfs(board, start, labor)
    if temp is None:
        return -1
    temp2 = bfs(board, labor, exit)
    if temp2 is None:
        return -1

    return temp + temp2
