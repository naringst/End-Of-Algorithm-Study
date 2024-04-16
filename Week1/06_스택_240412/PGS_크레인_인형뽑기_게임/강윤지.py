# 아이디어
## 

# 예상 시간복잡도
##

# 풀이시간 
## 분

# 실행시간 
## ms~ ms

def solution(board, moves):
    answer = 0
    depth = len(board)
    stack = [0]

    for move in moves:
        for i in range(depth):
            if board[i][move-1] == 0:
                continue
            if stack[-1] == board[i][move-1]:
                stack.pop()
                answer+=2
            else:
                stack.append(board[i][move-1])
            board[i][move-1] = 0
            break
    return answer
