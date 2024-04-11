# [초기 아이디어]
# stages돌면서 보다 작은곳에 total++, clear++하고 실패율 계산해서 내림차순 정렬
# -> 500*200000이라서 시간제한 빡빡하면 오버될 수 도 있겠다.
#
# [최종 아이디어]
# stages돌면서 각 스테이지에 멈춰있는 사람이 몇명인지 먼저 정리
# 1단계부터 마지막 단계까지 돌면서 작은 곳에 사람수만큼 더해주기(최악의 경우 500*500이라서 여유로움)
# 실패율계산후 내림차순정렬, 동일할 시 index 작은것이 앞으로 오게끔 정렬


#입력받기
n = int(input())
stages = input()
stages = [int(i) for i in stages.split()]

#각 스테이지에서 멈춘 사람들(다 깬 사람 n+1받기위해 n+2로 설정)
users = [0]*(n+2)
for i in stages:
    users[i]+=1

# 스테이지 도전자 수, 깬사람수, 실패한 사람수, 실패율
total = [0]*(n+1)
clear = [0]*(n+1)
fail = [0]*(n+1)
probability = [0]*(n+1)

#스테이지 지나간 사람, 깬사람 배열에 넣기
for index, i in enumerate(users):
    for j in range(1, index+1):
        if j> n : continue # j=n+1은 다 깬 사람이니까 n+1까지만 넣기
        total[j] += i
        if j != index : clear[j] += i # 스테이지에서 멈춘사람은 못깬사람

#실패한 사람, 실패율 넣기
for i in range(1, len(total)):
    fail[i] = total[i] - clear[i]
    if total[i] == 0 : probability[i] = 0
    else : probability[i] = fail[i]/total[i]

#실패율 내림차순 정렬, 실패율 동일하면 index가 작은게 앞으로 오게
answer = sorted(range(1, len(probability)), key = lambda i: (probability[i], -i), reverse=True)
print(answer)