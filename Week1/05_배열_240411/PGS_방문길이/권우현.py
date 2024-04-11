dirs=input()

#왼쪽에서 오른쪽 기준
visit_row = [[False]*11 for _ in range(11)]
#아래에서 위 기준
visit_column = [[False]*11 for _ in range(11)]

move=list(dirs)
#현재위치
position_x=0
position_y=0

#이동시작
for i in move:
    #오른쪽이면 움직이고 그좌표에 true
    if i == 'R':
        if position_x == 5: continue
        position_x += 1
        visit_row[position_x][position_y]=True
    #왼쪽이면 움직이고 움직이기 전 좌표에 true
    elif i == 'L':
        if position_x == -5: continue
        position_x -= 1
        visit_row[position_x+1][position_y]=True
    #위쪽이면 움직이고 그좌표에 true
    elif i == 'U':
        if position_y == 5: continue
        position_y += 1
        visit_column[position_x][position_y]=True
    #아래쪽이면 움직이고 움직이기 전 좌표에 true
    elif i == 'D':
        if position_y == -5: continue
        position_y -= 1
        visit_column[position_x][position_y+1]=True
answer = 0

#배열 두개 돌면서 true개수 체크
for i in visit_row:
    for chk in i:
        if chk: answer+=1

for i in visit_column:
    for chk in i:
        if chk: answer+=1

print(answer)