# 아이디어
## 신고당한 사람은 키로, 신고 한 사람을 값으로 set()에 담아서 카운트

# 예상 시간복잡도
## O(N)

# 풀이시간 
## 20분

# 실행시간 
## 0.01ms~ 133.38ms

from collections import defaultdict
def solution(id_list, report, k):

    # 이름 별 정지문자 받는 횟수 저장
    name_d = dict(zip(id_list, [0 for _ in range(len(id_list))]))
    d = defaultdict(set)
        
    for val in report:
        s, e = val.split()
        d[e].add(s)

    for val in d.values():
        if len(val) >= k:
            for name in val:
                name_d[name] += 1
                
    return list(name_d.values())
