# 아이디어
## goal을 하나씩 확인하며 cards1, cards2에 있는 카드와 순서대로 비교한다
## goal 에 대해 for문을 사용하고 cards1, cards2를 pop해서 사용하면 조금 더 깔끔한 코드가 됐을 것 같다.

# 예상 시간복잡도
## goal의 길이만큼 while문을 돌기에 goal의 최대 길이인 20이 될 것으로 예상된다.

# 풀이시간 
## 9분

# 실행시간 
## 0.00ms~ 0.01ms

def solution(cards1, cards2, goal):
    card1_idx = 0
    card2_idx = 0
    check = False
    
    while len(goal):
        word = goal.pop(0)
        if card1_idx < len(cards1) and cards1[card1_idx] == word:
            card1_idx += 1
            check = True
        elif card2_idx < len(cards2) and cards2[card2_idx] == word:
            card2_idx += 1
            check = True

        if check == False:
            return "No"
        check = False

    return "Yes"