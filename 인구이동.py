from collections import deque
import queue
N, L, R = map(int, input().split())

graph = []

for i in range(N):
    graph.append(list( map (int, input().split())))
    
    


dx = [-1, 1, 0, 0]
dy = [0,  0,-1, 1]# 상하좌우

answer = 0

def bfs(x ,y, count):
    
    sum = graph[x][y]
    counting_country = 1
    x_0, y_0 = queue[0]
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if back_track[nx][ny] == count:
                continue
            if back_track[nx][ny] == 10000:
                    continue
            if L <= abs(graph[nx][ny] - graph[x][y]) <= R:
                back_track[nx][ny] = count
                counting_country += 1
                sum += graph[nx][ny]
                queue.append((nx, ny))
    
    final_man = sum // counting_country
    queue.append((x_0,y_0))
    
    
    
    while queue:

        x, y = queue.popleft()
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if back_track[nx][ny] == 10000:
                    continue
            if back_track[nx][ny] == count:
                graph[nx][ny] = final_man
                back_track[nx][ny] = 10000
                queue.append((nx, ny))
    
    
answer =0
   
while True:          
    done = 0
    count = 0
    queue = deque()
    back_track = [[0 for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if back_track[i][j] != 0:
                continue
            if back_track[i][j] == 10000:
                continue
            
            x, y = i, j
            back_track[x][y] = -1 #지나왔음
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx < 0 or ny < 0 or nx >= N or ny >= N:
                    continue
                if back_track[nx][ny] == 10000:
                    continue
                if L <= abs(graph[nx][ny] - graph[x][y]) <= R:
                    count += 1
                    back_track[x][y] = count
                    queue.append((x,y))
                    done = 1
            
            if queue:
                bfs(x, y, count)

    if done:
        answer += 1
    if not done:
        break

print(answer)        
