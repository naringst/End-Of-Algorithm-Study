# 아이디어
## 딕셔너리로 부모 이름 저장 후 순회

# 예상 시간복잡도
## O(seller 수  * 트리 최대 depth)

# 풀이시간 
## 60분

# 실행시간 
## 0.02ms~ 125.92ms

def solution(enroll, referral, seller, amount):
    tree = dict(zip(enroll, referral))
    ans = dict(zip(enroll, [0] * len(enroll)))
    
    for name, num in zip(seller, amount):
        money = num * 100
        while True:
            profit = money // 10 
            ans[name] += money - profit 

            if profit < 1:
                break
            
            if tree[name] != '-':
                name = tree[name]
                money = profit 
            else:
                break
                
    return list(ans.values())
    
