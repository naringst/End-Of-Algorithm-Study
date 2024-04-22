# 아이디어
## 백트래킹 + DFS

# 예상 시간복잡도
## ??

# 풀이시간 
## 1시간 30분

# 실행시간 
## 0.01ms ~ 23.67ms

from collections import defaultdict
def solution(info, edges):
    ans = 0
    graph = defaultdict(list)
    # 그래프 초기화
    for s, e in edges:
        graph[s].append(e)
    
    st = [[1,0,[0]]]

    while st:
        sheep, wolf, visit = st.pop()
        ans = max(ans, sheep)
        # 그래프 돌면서 방문하지 않은 노드에 한해서 dfs
        for parent in visit:
            for next_node in graph[parent]:
                if next_node not in visit:
                    n_sheep = sheep
                    n_wolf = wolf
                    if info[next_node]:
                        n_wolf += 1
                    else:
                        n_sheep += 1
                    if n_sheep <= n_wolf:
                        continue
                    st.append([n_sheep, n_wolf, visit+[next_node]])
    return ans
