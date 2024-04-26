# 아이디어
## n을 키로 정렬한후, 값이 같다면 자체로 장렬

# 예상 시간복잡도
## O(nlogn)

# 풀이시간 
## 5분

# 실행시간 
## 0.00ms~ 0.04ms

def solution(strings, n):
    strings = sorted(strings, key = lambda x : (x[n], x))
    return strings
