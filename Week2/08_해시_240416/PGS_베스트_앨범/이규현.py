# 아이디어
## 두 개의 딕셔너리를 만들어서 정렬
## 인덱스를 들고다니면서 출력

# 예상 시간복잡도
## O(장르 갯수 * 2)

# 풀이시간 
## 40분

# 실행시간 
## 0.01ms~ 0.11ms

from collections import defaultdict
def solution(genres, plays):
    answer = []
    g = defaultdict(int)
    m = defaultdict(list)

    # 딕셔너리 생성
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        g[genre] += play
        m[genre].append([i, play])
      
    # 장르 정렬
    g = sorted(g.items(), key=lambda x : x[1], reverse=True)

    # 우선순위에 따른 인덱스 저장
    for key, val in g:
        a = sorted(m[key], key=lambda x : (x[1], -x[0]))
        for _ in range(2):
            if not a:
                break
            answer.append(a.pop()[0])

    return answer
