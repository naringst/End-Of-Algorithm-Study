# 아이디어
## 토너먼트로 진행되기에, 게임이 진행될 때 마다 참가자의 번호를 a/2의 올림으로 맞춰준다.
## 만약 두 참가자의 번호가 연속되고, 뒷 순서가 짝수라면 해당 라운드에서 만나게 된다
## 만약 올림한 번호가 같다면 이전 라운드에서 이미 만난것으로 간주한다.

# 예상 시간복잡도
## O(N) N = N/2

# 풀이시간 
## 15분

# 실행시간 
## 0.01ms~ 0.03ms

import math

def solution(n,a,b):
    answer = 1
    a, b = min(a, b), max(a, b)

    while True:
        b = math.ceil(b / 2)
        a = math.ceil(a / 2)
        answer += 1
        
        # 처음에 한 조에 들어있으면 리턴
        if a == b:
            return 1
        
        if b-a == 1 and b % 2 == 0:
            return answer