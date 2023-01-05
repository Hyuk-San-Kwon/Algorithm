
R, C, M = map(int, input().split())

graph = [[0 for _ in range(C)] for _ in range(R)] 
for i in range(M):
    r, c, s, d, z= map(int, input().split()) # x, y, 속력, 이동방향, 크기
    r = r - 1
    c = c - 1
    d = d - 1 # 0,1,2,3 상하우좌
    graph[r][c] = (s,d,z)


t = -1 # 사람위치
count = 0


dx = [-1, 1, 0, 0]
dy = [ 0, 0, 1,-1]


def move(x, y, d, s):
    
    
    while s > 0:
        
        if d == 0:
            x -= 1
            s -= 1
            if x == -1:
                x = 1
                d = 1
    
        elif d == 1:
            x += 1
            s -= 1 
            if x == R:
                x = R - 2
                d = 0
        
        elif d == 2:
            y += 1
            s -= 1
            if y == C:
                y = C - 2
                d = 3
                
        elif d == 3:
            y -= 1
            s -= 1
            if y == -1:
                y = 1
                d = 2
    
    return x,y,d,s

while True:    
    t += 1 
    if t == C:
        break

    back_track = [[0 for _ in range(C)] for _ in range(R)] 
    for i in range(R):
        if graph[i][t] != 0:
            count += graph[i][t][2]
            graph[i][t] = 0
            break
    for i in range(R):
        for j in range(C):
            if graph[i][j] == 0:
                continue
       
            s = graph[i][j][0]
            d = graph[i][j][1]
            z = graph[i][j][2]
            x,y = i,j
            if d == 0 or d == 1:
                s_copy = s % (2 * R - 2)
            if d == 2 or d == 3:
                s_copy = s % (2 * C - 2)

            x,y,d,s_copy = move(x,y,d,s_copy)
              
        
            graph[i][j] = 0
            if back_track[x][y] == 0:
                back_track[x][y] = (s, d, z)
            elif back_track[x][y] != 0:
                if back_track[x][y][2] > z:
                    continue 
                else:
                    back_track[x][y] = (s, d, z)    
    graph = (back_track)        

print(count)
                
    
    