# 아이디어
## 

# 예상 시간복잡도
## O(NlogN)

# 풀이시간 
## 6분

# 실행시간 
## 0.00ms~ 0.03ms

def solution(strings, n):
    strings.sort()
    strings.sort(key = lambda x: x[n])
    return strings