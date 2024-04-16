# 아이디어
## 주석 참고

# 예상 시간복잡도
## O(n), n = 최대 100000

# 풀이시간 
## 8분

# 실행시간 
## 0.02ms~ 195.42ms


def solution(record):
    answer = []
    # 유저 이름 기록하고, 마지막에 유저 아이디를 닉네임으로 치환
    # 유저 아이디 - 닉네임 -> 딕셔너리로 관리
    dict = {}
    
    for line in record:
        # Enter, Change 일 때 dict 변경
        if line.startswith("Enter") or line.startswith("Change"):
            user_id, nickname = line.split()[1], line.split()[2]
            dict[user_id] = nickname
                
    for line in record:
        if line.startswith("Enter"):
            user_id, nickname = line.split()[1], line.split()[2]
            answer.append(dict[user_id]+'님이 들어왔습니다.')
        elif line.startswith("Leave"):
            user_id = line.split()[1]
            answer.append(dict[user_id]+'님이 나갔습니다.')
    return answer

