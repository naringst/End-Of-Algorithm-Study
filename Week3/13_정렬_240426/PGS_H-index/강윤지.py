# 아이디어
## 주석 참고

# 예상 시간복잡도
##

# 풀이시간 
## 30분

# 실행시간 
## 0.00ms~ 0.11ms

def solution(citations):
    citations.sort()    
    n = len(citations)
    # 나머지 논문이 h번 이하 인용되었다면 -> 정렬로 해결

    for h in range(n, 0, -1):        
        # h번 이상 인용된 논문이 h편 이상인지 구하기
        # = h편 이상 인용된 논문 = citations[x]>=h
        if citations[n-h] >= h:
            return h
    return 0