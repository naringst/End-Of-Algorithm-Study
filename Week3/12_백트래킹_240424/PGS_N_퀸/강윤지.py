# 아이디어
## 먼저 wires를 행렬로 만들어 주고, 각 wire를 돌면서 하나씩 끊어준다.
## 이때 (x, y) 이라면 x와 y를 각각 시작 노드로 하여 dfs를 돌아 각각 연결된 노드들의 개수를 구해준다
## 이 노드들의 차이가 최소가 되도록 구해준다.

# 예상 시간복잡도
## O(N^2) N=wires의 길이

# 풀이시간 
## 50분

# 실행시간 
## 0.02ms~ 856.92ms

def solution(n, wires):    
    board = [[0] * n for _ in range(n)]
    min_diff = n
    visited = []
    
    # 행렬 만들기
    for i in range(len(wires)):
        x, y = wires[i]
        board[x-1][y-1] = 1
        board[y-1][x-1] = 1
    
    def dfs(start):
        visited.append(start)
        # 연결된 노드 확인
        for i in range(n):
            if i == start:
                continue
            if i not in visited and board[i][start] or board[start][i]:
                # 연결된 노드다! 그럼 다시 돌아야지
                # 방문 처리도 필수
                board[i][start] = 0
                board[start][i] = 0
                dfs(i)
                board[i][start] = 1
                board[start][i] = 1
        # 지금까지의 노드 수 리턴
        return len(visited)
    
    
    # 각 전선을 하나씩 끝어서 그 이전, 이후의 노드 개수 구하기
    for i in range(len(wires)):
        # 전선 하나 끊기
        x, y = wires[i]
        board[x-1][y-1] = 0
        board[y-1][x-1] = 0
        
        # dfs 돌기
        # x를 끝으로 하는 전력망, y를 시작으로 하는 전력망
        visited = []
        num1 = dfs(x-1)
        
        visited = []
        num2 = dfs(y-1)
        board[x-1][y-1] = 1
        board[y-1][x-1] = 1
        
        # 노드 개수 차이 최소 구하기
        if min_diff > abs(num1-num2):
            min_diff = abs(num1-num2)
        
    return min_diff