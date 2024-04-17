# 아이디어
## 먼저 Enter, Leave면 answer에 id와 함께 담아주고, 
## Change면 id_nickname dict에 넣는다.
## answer를 순회하며 dict에 있는 닉네임 기준으로 출력해준다. 

# 예상 시간복잡도
## O(record) = O(10만)

# 풀이시간 
## 15분

# 실행시간 
## 0.02ms~ 196ms

def solution(record):
    answer = []
    id_nickname = {}
    result = []
    
    for line in record :
        if line.startswith('Enter') :
            cd, id, nickname = line.split()
            answer.append([cd,id])
            id_nickname[id] = nickname
        elif line.startswith('Leave') :
            cd, id = line.split()
            answer.append([cd,id])
        else :
            cd, id ,nickname = line.split()
            id_nickname[id] = nickname
            
    for a in range(len(answer)) :
        if answer[a][0] == 'Enter':
            result.append("{0}님이 들어왔습니다.".format(id_nickname[answer[a][1]]))
        else :
            result.append("{0}님이 나갔습니다.".format(id_nickname[answer[a][1]]))
        
    
    return result
