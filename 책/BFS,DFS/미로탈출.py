from collections import deque

n, m = map(int, input().split())


array = []

for i in range(n):
    array.append(list(map(int, input())))
    

dx = [-1, 1, 0, 0]
dy = [ 0, 0,-1, 1]

(x,y) = (0, 0)
queue = deque()
queue.append((x,y))
while queue:
    (x,y) = queue.popleft()
    if (x,y) == (n-1,m-1):
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            continue
        elif array[nx][ny] == 0:
            continue
        elif array[nx][ny] == 1:
            queue.append((nx,ny))
            array[nx][ny] += array[x][y]
            
        

print(array[n-1][m-1])