# 아이디어
## 던전의 길이가 최대 8이기 때문에 8!을 해도 40320밖에 안된다. 따라서 모든 가능한 순열을 모두 구해 각 경우 중 최대 값을 구한다.

# 예상 시간복잡도
## n = len(dungeons)
## O(n! * n)

# 풀이시간 
## 15분

# 실행시간 
## 0.02ms~ 55.63ms

import itertools
def solution(k, dungeons):
    
    total_answer = 0
    all = list(itertools.permutations(dungeons,len(dungeons)))
    
    for one in all :
        answer = 0
        hp = k
        for a,b in one :
            if hp >= a :
                answer += 1
                hp -= b
        total_answer = max(total_answer,answer)
    
    return total_answer