# 아이디어
## 연결된 노드 정보를 담은후 DFS를 해서 연결된 네트워크 카운트

# 예상 시간복잡도
##O(n^2)

# 풀이시간 
## 35분

# 실행시간 
## 0.01ms~ 0.44ms

def solution(n, computers):
    answer = 0
    visit = [0] * n
    graph = [[] for _ in range(n)]

    # 연결된 노드 추가 / 절반만 돌기 / 양방향
    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)
                
    st = []
    #DFS
    for i in range(n):
        if visit[i] == 0:
            st.append(i)
            visit[i] = 1
            answer += 1
            while st:
                now = st.pop()
                
                for val in graph[now]:
                    if visit[val] == 0:
                        st.append(val)
                        visit[val] = 1
    
    return answer
