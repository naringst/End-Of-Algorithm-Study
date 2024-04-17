# 아이디어
## dict_genres = {'classic': {0: 500, 2:150, 3:800}, {1:600, 4:2500}}
## dict_play_genre = {'classic':1450, 'pop':3100}
## dict_play_genre를 value를 기준으로 내림차순 정렬하여, 그 안에서 각 장르에 대해 노래를 
## 재생 수를 기준으로 정렬한다. 마지막으로 각 장르당 2개만 넣어줘서 해결하였다.

# 예상 시간복잡도
## O(n) n=10000

# 풀이시간 
## 32분

# 실행시간 
## 0.01ms~ 0.10ms

from collections import defaultdict

def solution(genres, plays):
    answer = []
    
    dict_genres = defaultdict(dict)
    dict_play_genre = defaultdict(int)

    for i in range(len(genres)):
        dict_genres[genres[i]][i] = plays[i]
        dict_play_genre[genres[i]] += plays[i]

    # 속한 노래가 많이 재생된 장르 순 정렬
    sorted_genre = dict(sorted(dict_play_genre.items(), key=lambda x:x[1], reverse = True))

    # 장르 내에서 많이 재생된 노래 먼저 수록
    for key in sorted_genre.keys():
        genre_song = dict_genres[key]
        
        sorted_genre_song = list(sorted(genre_song.items(), key=lambda x:x[1], reverse = True))
        
        # 여기서 2개만 넣는다
        for item in sorted_genre_song[:2]:
            answer.append(item[0])
    return answer