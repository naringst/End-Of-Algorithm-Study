# 아이디어
## 특정 유저를 신고한 사람들을 value로 하는 dict을 하나 만든다.
## k번 이상 신고된 사람들을 따로 리스트로 만든다
## 그 리스트를 돌면서 그 사람을 신고한 유저들의 인덱스를 id_list에서 확인 후, 정답 배열에
## 추가해준다.
## + 시간이 생각보다 많이 나오는게 걱정. 시간을 줄일 수 있는 방법을 찾아봐야겠다

# 예상 시간복잡도
## O(n^2)
 
# 풀이시간 
## 23분

# 실행시간 
## 0.01ms~ 1983.99ms

def solution(id_list, report, k):
    answer = [0] * len(id_list)
    # 유저를 신고한 사람을 value로 하는 dict
    dict = {}
    reported_user = []
    for i in range(len(report)):
        userA, userB = report[i].split()
        if userB not in dict:
            dict[userB] = []
        if userA not in dict[userB]:
            dict[userB].append(userA)
        if len(dict[userB]) >= k and userB not in reported_user:
            reported_user.append(userB)
        
    # 만약, 신고 횟수가 초과된다면, 신고 한 사람에게 베일 주기
    for i in range(len(reported_user)):
        alarm_users = dict[reported_user[i]]
        for j in range(len(alarm_users)):
            idx = id_list.index(alarm_users[j])
            answer[idx] += 1
            
    return answer