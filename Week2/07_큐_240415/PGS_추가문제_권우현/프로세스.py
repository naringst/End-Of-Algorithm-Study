# 아이디어
## pop으로 꺼내고 우선순위 체크해서 더 먼저 실행해야될거있으면
## 뒤로 보냄
## 없으면 목표인지 확인, 아니면 실행하고 순서++

# 예상 시간복잡도
##

# 풀이시간
## 5분

# 실행시간
## 0.01ms~ 0.53ms


from collections import deque

priorities = [1, 1, 9, 1, 1, 1]
location = 0

process = [i for i in range(len(priorities))]
process = deque(process)
priorities = deque(priorities)

order = 1
while process:
    #일단 꺼내
    now_priority = priorities.popleft()
    now_process = process.popleft()
    #우선순위 있는지 확인
    #있으면 뒤로 보냄
    if any(x > now_priority for x in priorities):
        priorities.append(now_priority)
        process.append(now_process)
    #없으면
    #target인지 확인
    elif(now_process==location):
        break
    #target아니면 실행
    else : order += 1
print(order)