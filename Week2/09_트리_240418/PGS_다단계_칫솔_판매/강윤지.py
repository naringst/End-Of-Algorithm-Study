# 아이디어
## 판매원과 추천인을 dictionary로 연결하고, answer 또한 각 판매원에 맞게 dictionary로 선언한다
## 현재 판매에 대해 사람과 금액을 구하고, 그 다음 사람과 금액을 계산하여 맞도록 answer에 추가한다
## 만약 분배금이 없다면 바로 종료하도록 한다(시간 초과 예방)
## 만약 추천인이 없다면 종료한다.
## answer는 dictionary이기에 value들만 뽑아서 list로 반환하였다

# 예상 시간복잡도
## 100000 * 10000 = 대략 O(N^2)

# 풀이시간 
## 37분

# 실행시간 
## 0.02ms~ 125.51ms

def solution(enroll, referral, seller, amount):
    # 판매원과 추천인 연결
    users = dict(zip(enroll, referral))
    answer = dict(zip(enroll, [0] * len(enroll)))
    
    # 현재 판매에 대해
    for i in range(len(seller)):
        person = seller[i]
        money = amount[i] * 100
        
        # 타고 올라간다
        while True:
            # 10% 금액 구하기
            profit = money // 10

            # money를 제외한 금액을 당사자가 갖는다
            answer[person] += money - profit
            
            # 만약 분배금이 없다면 종료
            if profit == 0:
                break
                
            # 만약 추천인이 없다면 종료
            if users[person] == '-':
                break
            
            # 그 다음 당사자 구하기
            person = users[person]
            money = profit
        
    return list(answer.values())