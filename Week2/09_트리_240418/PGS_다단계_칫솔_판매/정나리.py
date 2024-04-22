# 아이디어
## 재귀함수를 사용해서 계속 나의 윗 노드로 값을 보내주도록 한다.
## 이때 주의할 점은 나의 10퍼센트를 주는 것 같지만, 사실 나의 윗 노드가 받는 금액은
## 내가 준 돈의 10퍼센트 중 1퍼센트를 제외한 금액이다.
## 따라서 int(money *0.1) - int(money*0.1*0.1) 다음과 같이 계산한다.


# 예상 시간복잡도
## seller = 100,000
## seller를 순회하면서 total, ref_connect에서 값 찾고 계산. 단 total, ref_connect는 dict이므로 O(1)
## 아마 O(len(seller))가 아닐까

# 풀이시간 
## 55분

# 실행시간 
## 0.11~264ms

ref_connect = {}
total = {}


def getMoney(person,money):
    global ref_connect, total
    
    if money * 0.1 >= 1 :
        total[ref_connect[person]] += int(money *0.1) - int(money*0.1*0.1)
    else : 
        return

    if ref_connect[person] == '-' :
        return 

    return getMoney(ref_connect[person], money*0.1)


def solution(enroll, referral, seller, amount):
    global ref_connect, total
    
    answer = []
    total['-'] = 0
    ref_connect = dict(zip(enroll, referral))
    
    for e in enroll :
        total[e] = 0
        
    for s in range(len(seller)) :
        add = amount[s] * 100
        total[seller[s]] += add * 0.9
        getMoney(seller[s],add)
        
    for name in enroll :
        answer.append(int(total[name]))
        
    return answer