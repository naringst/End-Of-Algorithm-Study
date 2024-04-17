# 아이디어
## 신고당한사람: 신고 한 사람 set을 생성해 저장한다.
## 그리고 k이상이 신고자는 메일을 받고, 이를 처음 입력받은 id_list 순서대로 출력한다.

# 예상 시간복잡도
## O(report길이) = O(200,000)

# 풀이시간 
## 13분

# 실행시간 
## 0.01ms~ 125.46msms

from collections import defaultdict
def solution(id_list, report, k):
    answer = []
    #신고 당한 사람 : [신고 했던 사람]  
    reported = defaultdict(set)
    mailed = defaultdict(int)
    
    for line in report : 
        reporter, bad_user = line.split()
        reported[bad_user].add(reporter)
    
    for r in reported :
        if len(reported[r]) >= k :
            for j in reported[r] :
                mailed[j] += 1
                
    for id in id_list :
        answer.append(mailed[id])
    
    return answer