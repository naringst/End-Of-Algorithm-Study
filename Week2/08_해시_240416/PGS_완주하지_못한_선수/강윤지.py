# 아이디어
## 파이썬의 딕셔너리를 활용하여 참가자를 저장한다. 이때 동명이인이 있을 경우를 위해 정수로 카운트 하며,
## 완주한 참가자는 삭제한다. 한 명의 선수만 완주하지 못하기에 딕셔너리를 리스트로 변환 후, 0 번째 인덱스를 반환한다

# 예상 시간복잡도
## 최대 100000 + 99999

# 풀이시간 
## 4분

# 실행시간 
## 0.00ms~ 50.44ms

def solution(participant, completion):    
    dict = {}
    for i in participant:
        if i in dict:
            dict[i]+=1
        else:
            dict[i] = 1
            
    for i in completion:
        dict[i]-=1
        if dict[i] == 0:
            del dict[i]
            
    return list(dict.keys())[0]