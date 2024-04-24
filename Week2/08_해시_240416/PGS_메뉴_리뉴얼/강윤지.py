# 아이디어
## 각 메뉴를 코스의 수대로 조합하여, 가장 많이 나온 메뉴의 조합을 answer에 추가한다

# 예상 시간복잡도
## O(N*2^M)

# 풀이시간 
## 47분

# 실행시간 
## 0.06ms~ 95.69ms

from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    # 각 메뉴를 course 의 수 대로 잘라서 저장, 개수 구하고, 제일 많은거 뽑기
    for c in course:
        menu = []
        for order in orders:
            comb = list(combinations(sorted(order), int(c)))
            menu+=(comb)

        counter = Counter(menu)
                
        # 해당 course에서 가장 많이 주문한 조합 구하기
        if (len(counter) != 0 and max(counter.values()) != 1):
            for key, value in counter.items():
                if value == max(counter.values()):
                    answer.append("".join(key))
                    
    return sorted(answer)