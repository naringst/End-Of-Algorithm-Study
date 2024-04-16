# 아이디어
##남은날짜 계산후 speed로 나누고,
##앞에서부터 확인, 바로 앞보다 짧게 걸리면 앞에 날로 변경해줌.

# 예상 시간복잡도
## 10000번 연산

# 풀이시간
## 15분

# 실행시간
## 0.01ms~ 0.05ms

import time
progresses = [1, 95, 95, 95]
speeds = [99, 1, 1, 1]

start = time.time()

days = []

for i in range(len(progresses)):
    tmp = 100-progresses[i]
    if tmp%speeds[i] !=0:
        days.append(int(tmp//speeds[i])+1)
    else :
        days.append(tmp//speeds[i])

prev = 0
distribution = []
answer = []

for day in days:
    if day > prev:
        distribution.append(day)
        prev = day
    else :
        distribution.append(prev)

prev = distribution[0]
tmp = 0
for i in range(1,len(distribution)):
    if(prev == distribution[i]):
        tmp+=1
    else :
        prev = distribution[i]
        answer.append(tmp+1)
        tmp = 0

answer.append(tmp+1)

end = time.time()

print(end - start)