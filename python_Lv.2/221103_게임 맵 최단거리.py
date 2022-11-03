from collections import deque

def solution(maps):

    n = len(maps)-1
    m = len(maps[0])-1

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    way = deque()
    way.append((0,0))
    
    while way:
        x, y = way.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx<0 or ny<0 or nx>n or ny>m:
                continue
            
            if maps[nx][ny] == 0:
                continue
            
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                way.append((nx,ny))
    if maps[n][m] < 2:
        return -1
            
    return maps[n][m]
