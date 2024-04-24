# 아이디어
## set을 이용하여 폰켓몬의 종류를 파악하고, 그 수가 절반이 넘는다면 절반을 리턴,
## 그렇지 않다면 폰켓몬의 종류를 리턴한다

# 예상 시간복잡도
## set(...)의 시간복잡도가 O(len(...))
## len(s)의 시간복잡도가 O(1)
## 즉, 최종 시간복잡도는 
## O(n) n = 10000

# 풀이시간 
## 2분

# 실행시간 
## 0.00ms~ 0.80ms

def solution(nums):
    temp = set(nums)
    return len(temp) if len(temp) <= len(nums)/2 else len(nums)/2