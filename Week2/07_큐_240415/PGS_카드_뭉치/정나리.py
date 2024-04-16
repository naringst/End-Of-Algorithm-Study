# 아이디어
## goal의 단어들을 순회하며 card1에 있으면 1것, 2에 있으면 2것을 가져온다. 
## 만약 어디에도 없다면 No를 return한다.
## 이때 배열 인덱스 범위를 넘어가지 않도록 주의한다.

# 예상 시간복잡도
## O(n) => 20

# 풀이시간 
## 15분

# 실행시간 
## 0ms~ 0.1ms

def solution(cards1, cards2, goal):
    answer = 'Yes'
    card1_idx = 0
    card2_idx = 0
    for i in range(len(goal)) :
        if cards1[card1_idx] == goal[i] :
            if card1_idx < len(cards1) -1 :
                card1_idx += 1
        else :
            if cards2[card2_idx] == goal[i] :
                if card2_idx < len(cards2) -1 :
                    card2_idx += 1     
            else :
                return 'No'
            
    return answer