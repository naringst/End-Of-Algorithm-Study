# 아이디어
## 처음엔 progress와 speeds를 각각 하루마다 게산해서 pop 해주는 형태로 풀려고 했지만 로직 구성이 어려워 다른 방법으로 풀이.
## 먼저 각 기능이 개발완료될 때가지 껄리는 시간을 days 배열에 넣고, 이를 pop하면서 count 하는 형식으로 구현.
## 가장 먼저 꺼내지는 기능을 before로 기준으로 두고, 이것보다 작은 날짜수를 갖는 값들만 count 해주면서 pop
## 만약 더 큰 값을 만나면 count를 1로 초기화 하고 다시 개수 세기 시작

# 예상 시간복잡도
## progress길이 * 100 씩 처음에 순회 => 10000
## 이후 while 문에서는 days만큼 순회 => 100 

# 풀이시간 
## 40분

# 실행시간 
## 0.01ms~ 0.14ms

from collections import deque

def solution(progresses, speeds):     
    days = deque([])
    answer = [] 
    for i in range(len(progresses)) :
        for j in range(1,101):
            if progresses[i] +  j * speeds[i] < 100 :
                continue
            else :
                days.append(j)
                break 

    count = 1
    before = days.popleft()

    while days :
        if before < days[0] :
            answer.append(count)
            count = 1
            before = days.popleft()
        else :
            days.popleft()
            count += 1
    
    answer.append(count)

    return answer 