# 아이디어
## 주석 참고

# 예상 시간복잡도
## 100000*10

# 풀이시간 
## 35분

# 실행시간 
## 0.04ms~ 271.86ms

def solution(want, number, discount):
    answer = 0

    dict = {}    
    for i in range(len(want)):
        dict[want[i]] = number[i]

    buy_dict = dict.copy()
    
    # 해당 날짜부터 10일간 원하는게 다 들어있는가
    for i in range(len(discount)):
        # 10개씩 자른다
        new_discount = discount[i:i+10]
        # 거기에 내가 원하는거 다 들어있는지 확인

        for j in range(len(new_discount)):
            # 만약 그날에 할인하는게 내가 원하는거에 있다면
            if new_discount[j] in buy_dict:
                buy_dict[new_discount[j]] -= 1
                if buy_dict[new_discount[j]] == 0:
                    del buy_dict[new_discount[j]]
                
        # 만약 10일동안 원하는거 다 못 샀다면
        if len(list(buy_dict.keys())) == 0:
            answer += 1
        buy_dict = dict.copy()
    return answer

