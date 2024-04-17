# 아이디어
## 연속 10일동안 해당 조건을 만족하는지 확인한다.
## 이때 원하는 만큼의 항목과 가격을 dict로 넣어주고, 연속 10일의 항목을 해당 dict에서 개수를 뺀다.
## 그리고 나서 모든 값이 0 이면 answer += 1
## 그렇게 10개를 진행한 뒤, 10개 이후부터는 앞에 항목을 하나빼고, 뒤의 항목을 하나 추가하는 식으로 구현한다.
## dict를 사용했으니 해당 항목을 찾을 때에는 O(1)이고 for문 1회 순회하기 때문에 O(discount)

# 예상 시간복잡도
## O(discount - 10) == O(100000)

# 풀이시간 
## 20분

# 실행시간 
## 0.01ms~ 40.55ms

def solution(want, number, discount):
    answer = 0
    dict = {}
    
    for w in range(len(want)) :
        dict[want[w]] = number[w] 
    
    for i in range(10) :
        if discount[i] in dict :
            dict[discount[i]] -= 1
            
    # dict가 다 0인지 확인
    if not any(dict.values()):
        answer += 1
        
    
    for j in range(10,len(discount)) :
        # 앞에꺼 빼기 
        if discount[j-10] in dict :
            dict[discount[j-10]] += 1
        # 뒤에꺼 넣기
        if discount[j] in dict :
            dict[discount[j]] -= 1
        # dict가 다 0인지 확인
        if not any(dict.values()):
            answer += 1
    
    return answer
