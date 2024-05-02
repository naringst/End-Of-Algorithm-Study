# 아이디어
## 

# 예상 시간복잡도
##

# 풀이시간 
## 15분

# 실행시간 
## 0.01ms~ 4425.58ms

def solution(k, tangerine):
    answer = 0
    # 크기별로 dictionary를 이용하여 개수 카운팅
    max_size = max(tangerine)
    size_dict = dict(zip(range(1, max_size+1), [0]*max_size))
    
    # 카운팅
    for size in tangerine:
        size_dict[size] += 1
    
    # value 내림차순으로 정렬
    size_dict = dict(sorted(size_dict.items(), key=lambda x: x[1], reverse=True))
    
    # 앞에서부터 순서대로 사용
    for value in size_dict.values():
        k -= value
        answer += 1
        if k <= 0:
            return answer

    return answer