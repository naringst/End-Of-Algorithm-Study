# 아이디어
## 인형 뽑으면서 제일 최근에 스택에 저장했던 값 꺼내서 비교,
## 같으면 answer+2하고 둘다 안넣음
## 다르면 꺼낸값 -> 뽑은 인형 순으로 다시 넣어줌.

# 예상 시간복잡도
## 30000번 연산

# 풀이시간 
## 30분

# 실행시간 
## 0.02ms~ 1.50ms


def solution(board, moves):
    n = len(board)
    figures = [0]
    answer = 0
    for i in moves:
        for j in range(n):
            if (board[j][i-1]==0): continue
            pick = board[j][i-1]
            board[j][i-1] = 0
            last = figures.pop()
            if(last==pick):
                answer += 2
            else :
                figures.append(last)
                figures.append(pick)
            break
    return answer