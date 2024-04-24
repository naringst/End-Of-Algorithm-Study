# 아이디어
##

## 링크드 리스트!!!!

# 예상 시간복잡도
##

# 풀이시간 
## 분

# 실행시간 
## ms~ ms


n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]

list = [i for i in range(n-1)]
chk = [True for i in range(n)]

#현재 위치
delete = []
for i in cmd:
    if i.startswith("D"):
        for j in range(int(i.split()[1])):
            k+=1
            if not chk[k]: j-=1
        if(k>len(list)): k = len(list)

    elif(i.startswith("U")):
        for j in range(int(i.split()[1])):
            k-=1
            if not chk[k]: j-=1
        if(k<1): k = 1
        print()

    elif(i.startswith("C")):
        tmp = list[k-1]
        delete.append(tmp+1)
        chk[k] = False

    elif(i.startswith("Z")):
        now = delete.pop()
        chk[now] = True



answer = ""
for i in range(n):
    if(chk[i]) : answer+="O"
    else : answer+="X"
print(answer)