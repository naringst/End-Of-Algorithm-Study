# 아이디어
##

# 예상 시간복잡도
##

# 풀이시간 
## 분

# 실행시간 
## ms~ ms


genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

totalMusic = {i:0 for i in genres}
music = {i:[] for i in genres}
topTwo = {i:[-1, -1] for i in genres}

for i in range(len(genres)):
    totalMusic[genres[i]] += plays[i]
    if topTwo[genres[i]][0] == -1:
        topTwo[genres[i]][0] = i

    elif topTwo[genres[i]][1] == -1:
        if plays[i] > plays[topTwo[genres[i]][0]]:
            topTwo[genres[i]][1] = topTwo[genres[i]][0]
            topTwo[genres[i]][0] = i
        else: topTwo[genres[i]][1] = i

    elif plays[i]>plays[topTwo[genres[i]][0]]:
        topTwo[genres[i]][1] = topTwo[genres[i]][0]
        topTwo[genres[i]][0] = i

    elif plays[i]==plays[topTwo[genres[i]][0]]==plays[topTwo[genres[i]][1]]:
        pass

    elif plays[i]==plays[topTwo[genres[i]][0]]:
        topTwo[genres[i]][1] = i


    elif plays[i]>plays[topTwo[genres[i]][1]]:
        topTwo[genres[i]][1] = i


totalMusic = sorted(totalMusic.items(), key=lambda x: x[1], reverse=True)

answer = []
for i in totalMusic:
    genre = i[0]
    answer.append(topTwo[genre][0])
    if topTwo[genre][1] != -1:
        answer.append(topTwo[genre][1])

print(answer)