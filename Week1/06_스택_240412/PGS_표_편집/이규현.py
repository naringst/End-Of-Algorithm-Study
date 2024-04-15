# 아이디어
## 링크드리스트 자료구조를 활용하면 좋지만 파이썬에서 구현이 익숙하지 않아서 딕셔너리를 사용했습니다!
## 인덱스 번호를 키로 두고 전,후 인덱스를 값으로 저장하면 됩니다

# 예상 시간복잡도
## O(N)

# 풀이시간 
## 2시간

# 실행시간 
## 0.02ms~ 7.81ms


def solution(n, k, cmd):

    ans = ['O'] * n
    
    table = {i :[i-1, i+1] for i in range(n)}
    delete = []
    table[0] = [None, 1]
    table[n-1] = [n-2, None]
    
    for move in cmd:
              
        if move == 'C':
            #삭제
            ans[k] = 'X'
            front, end = table[k]
            delete.append([front, k, end])
            
            # 앞 뒤 수정
            if front == None:
                k = end
                table[end][0] = None
            elif end == None:
                k = front
                table[front][1] = None
            else:
                k = end
                table[front][1] = end
                table[end][0] = front

        elif move == 'Z':
            front, back_num , end = delete.pop()
            ans[back_num] = 'O'
            if front == None:
                table[end][0] = back_num
            elif end == None:
                table[front][1] = back_num
            else:
                table[front][1] = back_num
                table[end][0] = back_num
                
        else:
            c1, c2 = move.split(" ")
            c2 = int(c2)
            if c1 == 'U':
                for _ in range(c2):
                    k = table[k][0]
            else:
                for _ in range(c2):
                    k = table[k][1]

    return ''.join(ans)
