# 아이디어
## dedaultdict을 이용하여 완주한 사람들 먼저 딕셔너리에 담고,
## 참여한 사함들 명단과 비교

# 예상 시간복잡도
## O(N)

# 풀이시간 
## 20분

# 실행시간 
## 0.00ms~ 0.57ms

from collections import defaultdict
def solution(participant, completion):
    dict_l= defaultdict(int)
    
    # 완주한 사람들 딕셔너리 담기
    for val in completion:
        dict_l[val] += 1
    
    for val in participant:
        # 완주 목록에 없는 경우 이름 반환
        if val not in dict_l:
            return val
        else:
            if dict_l[val] == 1:
                del dict_l[val]
            else:
                dict_l[val] -= 1

