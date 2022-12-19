from collections import deque
import sys
input = sys.stdin.readline
n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())) )

size = 2
eat_count = 0

x_0, y_0 = 0,0 

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x_0, y_0 = i, j

dx = [-1, 1, 0, 0]
dy = [ 0, 0,-1, 1]#상하 좌우
           
            
def bfs(x,y):
    
    queue =deque()
    queue.append((x,y,0))
    answer = []
    zero_list = []
    size_list =[]
    while queue:

        x,y,distance = queue.popleft()
        find = 0

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or ny < 0 or nx >= n or ny >=n: #그래프 바깥
                continue
            elif graph[nx][ny] > size: # 물고기가 크면
                continue
            elif graph[nx][ny] < size and graph[nx][ny] != 0:
                answer.append((nx,ny,distance + 1))
                find = 1
                continue
            elif find == 0:
                
                if graph[nx][ny] == 0:
                    zero_list.append((nx,ny))
                    queue.append((nx,ny,distance + 1))
                    graph[nx][ny] = 100
                if graph[nx][ny] == size:              
                    size_list.append((nx,ny))  
                    queue.append((nx,ny,distance + 1))
                    graph[nx][ny] = 100    
                
    
    if not answer:
        return -1, -1, 0 
      
    x_1, y_1,distance = 100, 100 , 10000
    for i in range(len(zero_list)):
        kx, ky = zero_list[i]
        graph[kx][ky] = 0
    for i in range(len(size_list)):
        gx, gy = size_list[i]
        graph[gx][gy] = size 
    
   

    while answer:
        temp_x, temp_y, temp_distance = answer.pop()
      
        if temp_distance < distance:
            distance = temp_distance
            x_1 = temp_x 
            y_1 = temp_y
            continue
        elif  temp_distance > distance:
            continue
        if temp_x < x_1:
            x_1 = temp_x 
            y_1 = temp_y
        elif temp_x == x_1:
            if temp_y < y_1:
                y_1 = temp_y
    return x_1, y_1, distance


total_disance = 0



while True:
    
    x_1, y_1, distance = bfs(x_0,y_0)
    
    if x_1 == -1:
        break
    eat_count += 1
    if eat_count == size:
        size+=1
        eat_count = 0
    graph[x_0][y_0] = 0
    graph[x_1][y_1] = 9
    x_0, y_0 = x_1, y_1

    total_disance += distance

print(total_disance)