# 아이디어 
# dictionary 와 set 이용.
# 방향에 따른 이동하는 x,y 좌표는 dict, 그리고 방문한 간선의 위치는 set을 활용해 중복 방문한 곳은 1번으로 계산하도록 한다. 

# 예상 시간복잡도
# dirs 한 번 순회, dirs의 길이는 500 이하의 자연수 
# 여기에 min, max 계산 한번 
# => 총 n번의 계산


# 풀이시간 20분
# 실행시간 0.01~0.55ms


def solution(dirs):
    directions = {'U' : (1,0), 'D' : (-1,0) , 'L' : (0,-1) , 'R': (0, 1)}
    answer = 0
    x, y = 0, 0
    visited = set([])
    
    for i in range(len(dirs)) :
        dx, dy = directions[dirs[i]]
        nx = x + dx
        ny = y + dy
        
        if (-5 <= nx <= 5 and -5 <= ny <= 5) :
            # 이동
            if ( nx == x) :
                visited.add((nx,min(ny,y), (nx,max(ny,y))))
            else :
                visited.add(((min(nx,x),ny), (max(x,nx),y)))
            x = nx 
            y = ny
        else : 
            continue
    
    
    return len(visited)