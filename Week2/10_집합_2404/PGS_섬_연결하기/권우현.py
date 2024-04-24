# 아이디어
## 

# 예상 시간복잡도
##

# 풀이시간 
## 분

# 실행시간 
## ms~ ms
costs = [[0, 1, 5], [0, 3, 2], [0, 4, 3], [1, 4, 1], [3, 4, 10], [1, 2, 2], [2, 5, 3], [4, 5, 4]]
n = 6

answer = 0
costs.sort(key=lambda x : x[2])
isConnect = {costs[0][0]}

while len(isConnect) != n:
    print(isConnect)
    for cost in costs:
        if cost[0] in isConnect and cost[1] in isConnect:
            continue
        if cost[0] in isConnect or cost[1] in isConnect:
            isConnect.add(cost[0])
            isConnect.add(cost[1])
            answer += cost[2]
            break
print(answer)