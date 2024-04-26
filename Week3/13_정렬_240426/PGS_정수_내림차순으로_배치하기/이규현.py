# 아이디어
## 문자열 변환 정렬 후 다시 정수로 변환

# 예상 시간복잡도
## O(nlogn)

# 풀이시간 
## 5분

# 실행시간 
## 0.02ms~ 0.05ms

def solution(n):
    return int(''.join(sorted(str(n), reverse=True)))
