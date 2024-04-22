# 아이디어
## 홀수와 짝수를 각각 2로 나눠서 값이 같아지는 경우가 답

# 예상 시간복잡도
## O(logn)

# 풀이시간 
## 20분

# 실행시간 
## 0.00ms~ 0.01ms

def solution(n,a,b):
    round = 0
    
    while True:
        round += 1
        a = (a // 2) + (a % 2)
        b = (b // 2) + (b % 2)
        if a == b:
            break
    return round
