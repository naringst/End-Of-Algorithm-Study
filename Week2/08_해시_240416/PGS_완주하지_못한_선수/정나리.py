# 아이디어
## 어떻게 풀어도 시간초과가 났다.
## 처음에는 배열을 deque로 만들고 해당하는 사람을 지우는 식으로 구현했는데 시간초과.
## for문만 돌아서 풀려고 했지만 동명이인이 존재한다는 조건 때문에 잘 안돼서 dict 활용
## 모두 참가자를 dictionary에 넣고 1로 초기화 => completion에 있으면 -1 그렇게 해서 1로남은 사람을 출력했다. 

# 예상 시간복잡도
## O(len(participant))

# 풀이시간 
## 20분

# 실행시간 
## 0.01ms~ 0.42ms

def solution(participant, completion):
    dict = {}

    for i in range(len(participant)) :
        if participant[i] in dict :
            dict[participant[i]] += 1
        else :
            dict[participant[i]] = 1

    
    for j in range(len(completion)) :
        dict[completion[j]] -= 1
    
    for key, value in dict.items() :
        if value == 1 :
            return key
