# 아이디어
## 

# 예상 시간복잡도
## O(n)

# 풀이시간 
## 25분

# 실행시간 
## 0.01ms~ 72.29ms

from collections import deque

def solution(bridge_length, weight, truck_weights):
    # 다리 길이 당 트럭 지나간 여부 저장
    # bridge = [0] * bridge_length
    bridge = deque([0] * bridge_length)
    time = 0
    sum_weights = 0
    
    while truck_weights:
        # 트럭 전진
        time += 1
        sum_weights -= bridge.popleft()
        bridge.append(0)

        # 트럭이 다리에 들어갈 수 있는지 구하기
        # 다리 무게 체크
        # if (sum(bridge) + truck_weights[0]) <= weight:
        # 이렇게 sum을 쓰면 시간초과 발생. 변수를 사용하여 가감하는 형식으로 사용!
        if sum_weights + truck_weights[0] <= weight:
            # 무게가 버틴다면, 다리에 진입
            sum_weights += truck_weights[0]
            bridge[-1] = truck_weights[0]
            truck_weights.pop(0)

    # 맨 마지막 트럭 지나갈 시간 구하기
    location = 0
    for i in range(len(bridge)):
        if bridge[i] != 0:
            location = i
    
    # location == 마지막 트럭의 위치
    # 트럭 빠져나가는 시간 구하기
    time += location + 1
            
    return time