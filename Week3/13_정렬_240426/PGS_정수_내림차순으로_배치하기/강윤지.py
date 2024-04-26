# 아이디어
## 주석 참고

# 예상 시간복잡도
## O(NlogN)

# 풀이시간 
## 2분

# 실행시간 
## 0.02ms~ 0.05ms

def solution(n):
    # 각 자릿수의 숫자를 따로따로 저장해서, 내림차순으로 정렬
    temp = list(str(n))
    temp2 = "".join(sorted(temp, reverse=True))

    return int(temp2)