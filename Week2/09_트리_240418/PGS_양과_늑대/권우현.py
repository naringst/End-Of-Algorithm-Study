# 아이디어
## 

# 예상 시간복잡도
##

# 풀이시간 
## 분

# 실행시간 
## ms~ ms


info = [0,0,1,1,1,0,1,0,1,0,1,1]
edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

child = {i: [] for i in range(len(info))}

for edge in edges:
    child[edge[0]].append(edge[1])

sheep = 1
wolf = 0
visitable = []
visitable.append(child[0][0])
visitable.append(child[0][1])

while True:
    flag = False
    for i in visitable:
        if info[i]==0:
            visitable.remove(i)
            flag = True
            if child[i][-1]:
                visitable.append(child[i][0])
            if child[i][-2]:
                visitable.append(child[i][1])
            break


    if flag: continue