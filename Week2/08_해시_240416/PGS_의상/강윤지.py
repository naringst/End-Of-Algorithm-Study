# 아이디어
## dictionary를 활용하여 각 의상의 종류에 의상의 수를 증가시켜주었고, 
## 각각의 조합을 구하기 위해 의상의 종류에 대한 수를 곱해주었다
## 각 의상의 종류는 입지 않아도 되기에 의상의 종류마다 1을 더해주었고
## 아무것도 입지 않았을 경우를 빼주기 위해 1을 마지막에 뺐다

# 예상 시간복잡도
## O(n)

# 풀이시간 
## 10분

# 실행시간 
## 0.01ms~ 0.03ms

from collections import defaultdict

def solution(clothes):
    answer = 1
    
    # 종류 : [이름]
    dict = defaultdict(lambda: 1)
    
    for i in range(len(clothes)):
        dict[clothes[i][1]] += 1
    
    for value in dict.values():
        answer *= value
    
    
    return answer-1