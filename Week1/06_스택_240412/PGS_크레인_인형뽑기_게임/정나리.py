# 아이디어
## moves 배열의 값대로 순회하면서 board에 해당하는 idx를 위에서부터 확인한다. 그리고 0이 아닌 값을 만나면 꺼내서 bucket으로 옮긴다.
## bucket으로 옮길 때 두 개 연속하면 바로 pop한다.
## 주의 : bucket에서 pop할 때에는 pop할 원소가 있는지 확인한 뒤 pop

# 예상 시간복잡도
## 1000 * 30 = 3만

# 풀이시간 
## 17분

# 실행시간 
## 0.02 ms~ 2.19ms

def solution(board, moves):
    answer = 0
    bucket = []
    for move in moves :
        idx = move -1
        for j in range(len(board)) :
            if board[j][idx] == 0 :
                continue
            else :
                if bucket and bucket[-1] == board[j][idx] :
                    bucket.pop()
                    answer +=2 
                else :
                    bucket.append(board[j][idx])
                board[j][idx] = 0
                break 
                

    return answer