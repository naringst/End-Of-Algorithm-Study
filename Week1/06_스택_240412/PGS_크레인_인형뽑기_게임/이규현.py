# 아이디어
## 배열로 뽑기 편하게 행과 열 뒤집어서 진행했습니다.

# 예상 시간복잡도
## O(N^2)

# 풀이시간 
## 25분

# 실행시간 
## 0.01ms~ 0.43ms


def solution(board, moves):
    n = len(board)
    answer = 0
    new_board = [[] for _ in range(n)]
    
    # 행 <-> 열 교체
    for i in range(n):
        for j in range(n-1, -1, -1):
            if board[j][i] == 0:
                break
            new_board[i].append(board[j][i])
    
    bowl = []
    
    for val in moves:
        # 인형 없는 경우 방지
        if new_board[val-1]:
            doll = new_board[val-1].pop()
            
            if not bowl:
                bowl.append(doll)
            else:
                if bowl[-1] == doll:
                    bowl.pop()
                    answer += 2
                else:
                    bowl.append(doll)
            
    return answer
