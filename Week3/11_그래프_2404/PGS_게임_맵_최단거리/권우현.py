# 아이디어
## 

# 예상 시간복잡도
##

# 풀이시간 
## 분

# 실행시간 
## ms~ ms


from collections import deque


def solution(maps):
    m, n = len(maps), len(maps[0])
    start = (0, 0)
    end = (m - 1, n - 1)
    cnt = bfs(maps, start, end)
    if cnt is None:
        return -1
    return cnt


def bfs(maps, start, end):
    m, n = len(maps), len(maps[0])
    visited = set()
    next_ = deque([(start[0], start[1], 1)])
    directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
    while next_:
        nx, ny, cnt = next_.popleft()
        if (nx, ny) in visited:
            continue
        else:
            visited.add((nx, ny))
            if (nx, ny) == end:
                return cnt
            else:
                for dr, dc in directions:
                    next_x, next_y = nx + dr, ny + dc
                    if 0 <= next_x < m and 0 <= next_y < n and maps[next_x][next_y] == 1:
                        next_.append((next_x, next_y, cnt + 1))