# 1번 수포자는 12345 반복
# 2번 수포자는 21232423(8) 반복
# 3번 수포자는 3311224455(10) 반복
# 아주 단순한게는 1명당 10000번씩 돌려 * 3

# 아이디어
# 각 배열 별 숫자 구하는 함수 설정
# 모든 배열 별 숫자 구하도록 함수 실행 

def supo(answers, repeat_arr, repeat_cnt) :
    result = 0 
    for i in range(len(answers)) :
        if repeat_arr[i % repeat_cnt] == answers[i] :
            result += 1
    return result 


def solution(answers):
    final = []
    answer =[]
    
    answer.append([supo(answers,[1,2,3,4,5], 5),1])
    answer.append([supo(answers,[2,1,2,3,2,4,2,5], 8),2])
    answer.append([supo(answers,[3,3,1,1,2,2,4,4,5,5], 10) ,3])
    
    # 첫번째 값 기준 내림차순
    answer.sort(key=lambda x:x[0],reverse=True)
    
    maxNum = answer[0][0]
    for num, person in answer :
        if maxNum ==  num :
            final.append(person)
        
    return final


# 다른 사람의 풀이
# 해당 풀이는 배열을 한 번만 순회하게 되어 시간복잡도가 유리함.
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result