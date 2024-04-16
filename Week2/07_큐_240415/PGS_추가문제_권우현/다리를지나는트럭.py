# 아이디어
## [초기 아이디어]
## 다리를 리스트로 만들어서 1초 지날때마다 한칸씩 옮겨주고 트럭 빠져나가고, 새로 들어오고
## 한칸씩 옮겨주는 과정이 너무 오래걸릴거같음.
## [수정 아이디어]
## 다리를 덱으로 만들어서 끝에서 한칸 빼주고, 처음에서 추가하는 방식으로 한칸씩 옮겨주는 것과 동일하게 구현

# 예상 시간복잡도
##

# 풀이시간
## 30분

# 실행시간
## 0.01ms~ 56.35ms



from collections import deque

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

bridge = deque([0] * bridge_length)
truck_weights = deque(truck_weights)

time = 0
now_weight = 0

while truck_weights:
    # print(" time = ", time, "bridge = ", bridge)
    time += 1
    #한칸씩 땡기기
    out = bridge.pop()
    #다리 끝에 있는 트럭 나가
    if out != 0:
        now_weight -= out
    #올라올수있으면 올라와
    if now_weight+truck_weights[0] <= weight:
        bridge.appendleft(truck_weights.popleft())
        now_weight += bridge[0]

    #못올라왔으면 빈칸 추가
    else:
        bridge.appendleft(0)

# print(" time = ", time, "bridge = ", bridge)
#마지막 트럭이 첫번째칸에 올라가면 while문 끝!
time += bridge_length

print(time)