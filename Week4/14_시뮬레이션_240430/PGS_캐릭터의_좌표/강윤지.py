# 아이디어
## 

# 예상 시간복잡도
##

# 풀이시간 
## 15분

# 실행시간 
## 0.00ms~ 0.02ms

def solution(keyinput, board):
    width, height = 0, 0

    for command in keyinput:
        if command == 'left' and -(board[0]//2) < width:
            width -= 1
        elif command == 'right' and board[0]//2 > width:
            width +=1
        elif command == 'down' and -(board[1]//2) < height:
            height -= 1
        elif command == 'up' and board[1]//2 > height:
            height +=1 
            
    return [width, height]