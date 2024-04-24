# 아이디어
## 간선이 아니라 노드에 대한 방문 여부를 검사하고, 노드와 이어진 노드를 탐색한다

# 예상 시간복잡도
## O(N^2) N = 200

# 풀이시간 
## 7분

# 실행시간 
## 0.01ms~ 0.90ms

def solution(n, computers):
    answer = 0
    visited = []
    
    def dfs(node):
        visited.append(node)
        
        for i in range(n):
            # 해당 노드와 연결된 곳 검사
            if computers[node][i] and i not in visited:
                dfs(i)
            
    
    for i in range(n):
        if i not in visited:
            dfs(i)  
            answer+=1
    
    return answer