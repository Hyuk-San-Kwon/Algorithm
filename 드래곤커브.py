from collections import deque
from re import L
N = int(input())

orders = []
for i in range(N):
    orders.append(list(map(int, input().split())))
    
temp_map =101

graph = [[ 0 for _ in range(temp_map)] for _  in range(temp_map)]

# dir 0,1,2,3 우 상 좌 하

dx = [0,-1, 0, 1]
dy = [1, 0,-1, 0]

for i in range(len(orders)):

    x, y, dir, gen = orders[i]
    
    y,x = x, y
    graph[x][y] = 1
 
    y = y + dy[dir]
    x = x + dx[dir]
    
    graph[x][y] = 1
    
    dir_list = []
    dir_list.append(dir)
    
    for j in range(gen):
        temp_dir = dir_list[::-1]
        
        for k in range(len(temp_dir)):
            dir = temp_dir[k]
            dir += 1
            if dir == 4:
                dir = 0
            dir_list.append(dir)
            y = y + dy[dir]
            x = x + dx[dir]
            graph[x][y] = 1


count = 0
for i in range(temp_map-1):
    for k in range(temp_map - 1):
        if graph[i][k] == 1 and graph[i+1][k] == 1 and graph[i][k+1] == 1 and graph[i+1][k+1] == 1:
            count += 1
        
        
print(count)
        