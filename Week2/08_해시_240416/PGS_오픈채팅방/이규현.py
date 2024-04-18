# 아이디어
## 아이디 별로 닉네임 저장

# 예상 시간복잡도
## O(record길이)

# 풀이시간 
## 25분

# 실행시간 
## 0.01ms~ 149.52ms

def solution(record):
    names = {}
    answer = []
    
    for val in record:
        #들어오는 경우
        if val[0] == 'E':
            uid, nick_name = val[6::].split(' ')
            names[uid] = nick_name
            answer.append([uid, '님이 들어왔습니다.'])
            
        #나가는 경우
        elif val[0] == 'L':
            uid = val[6::]
            answer.append([uid,'님이 나갔습니다.'])
            
        # 이름 바꾸는 경우
        else:
            uid, nick_name = val[7::].split(' ')
            names[uid] = nick_name

    for idx, val in enumerate(answer):
        answer[idx] = names[val[0]]+val[1]
    
    return answer
