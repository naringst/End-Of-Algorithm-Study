# 아이디어
## 먼저 set으로 장르 종류만 찾아내고 이를 바탕으로 best_plays, best_plays_sum 배열 생성 
## 이들 각각을 []과 0으로 초기화 한후, best_plays에는 인덱스와 들은 횟수를, best_plays_sum에는 장르별 총 합을 구한다.
## best_plays_sum 배열을 정렬한 것을 기준으로, 순서대로 best_plays의 배열을 가져와 정렬한 후 들은 횟수가 많은 것부터 출력한다.
## "장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다" 
## => 조건 처리를 안했는데 처음에 key로 sort하면서 알아서 된 것 같다. 
## => 알고보니 처음에 넣을 때 인덱스 순서대로 넣어서, 들은 횟수로 sort해도 같은 값은 움직이지 않기 때문에 인덱스 순서대로 가는듯?
## => 같은 값이면 원래 배열 내 순서를 따른다!
# sorted_arr = [[2,200],[3,100],[1,100],[6,200],[5,100]]
## sorted_arr.sort(key=lambda x:x[1], reverse=True)
## print(sorted_arr) =>	[[2, 200], [6, 200], [3, 100], [1, 100], [5, 100]]

# 예상 시간복잡도
## 장르 종류에 따른 dict를 sort => nlogn => 100 log100
## genres 배열 순회 => 10000
## 장르 종류에 따른 dict의 value들 sort => 100 * (10000/100)log(10000/100) => 100 * 1000 * log1000 = 약 10만?

# 풀이시간 
## 20분

# 실행시간 
## 0.02ms~ 0.11ms


# 장르에 속한 곡이 하나면 하나만 선택!!
def solution(genres, plays):
    answer = []
    only_genres = list(set(genres))
    best_plays = {}
    best_plays_sum = {}
    
    for o in range(len(only_genres)) :
        best_plays[only_genres[o]] = []
        best_plays_sum[only_genres[o]] = 0
        
    for g in range(len(genres)) :
        best_plays[genres[g]].append([g,plays[g]])
        best_plays_sum[genres[g]] += plays[g]
    
    sorted_dict = dict(sorted(best_plays_sum.items(), key=lambda x: x[1], reverse=True))
    
    for key in sorted_dict :
        best_plays[key].sort(key=lambda x:x[1], reverse=True)
        if len(best_plays[key]) >= 2 :
            for i in range(2) :
                answer.append(best_plays[key][i][0])     
        else :
            answer.append(best_plays[key][0][0])   
            
    return answer
