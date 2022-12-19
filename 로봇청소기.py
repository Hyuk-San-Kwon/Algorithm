N ,M = map(int , input().split())

graph = []

x, y, dir = map(int , input().split()) #0123 북동남서

for i in range(N):
    graph.append(list(map(int, input().split())))
    
dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0,-1]   

count = 1

while True:
   
    
    graph[x][y] = -1
    next_dir = dir - 1
    if next_dir == -1:
        next_dir = 3
    nx = x + dx[next_dir]
    ny = y + dy[next_dir]
    if (0 <= nx < N) and (0 <= ny < M):
        if graph[nx][ny] == 0:
            x,y = nx, ny
            dir = next_dir
            count += 1
            continue
    next_dir = next_dir - 1
    if next_dir == -1:
        next_dir = 3
    nx = x + dx[next_dir]
    ny = y + dy[next_dir]
    if (0 <= nx < N) and (0 <= ny < M):
        if graph[nx][ny] == 0:
            x,y = nx, ny
            dir = next_dir
            count += 1
            continue
    next_dir = next_dir - 1
    if next_dir == -1:
        next_dir = 3
    nx = x + dx[next_dir]
    ny = y + dy[next_dir]
    if (0 <= nx < N) and (0 <= ny < M):
        if graph[nx][ny] == 0:
            x,y = nx, ny
            dir = next_dir
            count += 1
            continue
    next_dir = next_dir - 1
    if next_dir == -1:
        next_dir = 3
    nx = x + dx[next_dir]
    ny = y + dy[next_dir]
    if (0 <= nx < N) and (0 <= ny < M):
        if graph[nx][ny] == 0:
            x,y = nx, ny
            dir = next_dir
            count += 1
            continue
    # 후진
    
    next_dir = dir
    nx = x - dx[next_dir]
    ny = y - dy[next_dir]
    if (0 <= nx < N) and (0 <= ny < M):
        if graph[nx][ny] == -1:
            x,y = nx, ny
            dir = next_dir
            continue
        if graph[nx][ny] == 1 :
            break

    

print(count)