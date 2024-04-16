# 아이디어
## queue에 먼저 각 progress에 대한 작업 완료까지 필요한 일수를 구한 다음, 
## while문을 돌면서 이전 작업에 대한 완료 날짜를 확인

# 예상 시간복잡도
## progresses의 최대 길이인 100으로 예상

# 풀이시간 
## 40분

# 실행시간 
## 0.01ms~ 0.04ms

from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    queue = deque()
    
    for i in range(len(progresses)):
        queue.append(math.ceil((100-progresses[i])/speeds[i]))
        
    count = 1
    prev = queue.popleft()

    while(queue):
        if prev >= queue[0]:
            queue.popleft()
            count += 1
        else:
            answer.append(count)
            prev = queue.popleft()
            count = 1
    answer.append(count)
    return answer