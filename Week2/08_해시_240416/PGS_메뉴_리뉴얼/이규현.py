# 아이디어
## 조합을 통해 가능한 모든 경우를 딕셔너리에 저장 후 카운트

# 예상 시간복잡도
## O(n^) -> course 수 * 가능한 조합 수

# 풀이시간 
## 45분

# 실행시간 
## 0.03ms~ 3.28ms

from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    
    answer = []
    
    for num in course:
        food = defaultdict(int)
        arr = []
        for order in map(list, orders):
            #정렬
            order.sort()
            # 조합 사용
            c = [''.join(x) for x in combinations(order, num)]
            arr.extend(c)
            
        for val in arr:
            food[val] += 1
        #정렬
        food = sorted(food.items(), key=lambda x : x[1], reverse=True)
        
        # 일치하는 조합이 없을 수도 있음
        if food:
            max_val = food[0][1]

            if max_val < 2:
                continue
            for key, val in food:
                if val == max_val:
                    answer.append(key)
                else:
                    break
    answer.sort()
    return answer
