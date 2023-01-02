
R, C, T = map(int, input().split())

graph = []

for i in range(R):
    graph.append(list(map(int, input().split())))
    


cleaner = []

for i in range(R):
    for j in range(C):
        if graph[i][j] == -1:
            cleaner.append((i,j))

dx = [-1, 1, 0, 0]
dy = [ 0, 0,-1, 1]
t = 0
while True:    
    
    back_track = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):

            if graph[i][j] == 0 or graph[i][j] == -1:
                continue
            check = [0, 0, 0, 0]
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if nx < 0 or ny < 0 or nx >= R or ny >= C:
                    continue
                if graph[nx][ny] == -1:
                    continue
                check[k] = 1
            for k in range(len(check)):
                if check[k]:
                    nx = i + dx[k]
                    ny = j + dy[k]
                    back_track[nx][ny] += graph[i][j] // 5
            sum_check = sum(check)
            graph[i][j] -= graph[i][j] // 5 * sum_check
                
     
    for i in range(R):
     
        for j in range(C):
            graph[i][j] += back_track[i][j]
            
 
    x, y = cleaner[0]
    
    while x > 0:
        x -= 1
        graph[x][y] = graph[x-1][y]
    
    while y < C - 1: # y는 c-1도착
        graph[x][y] = graph[x][y+1]
        y += 1 
        
    while x < cleaner[0][0]:
        x += 1
        graph[x-1][y] = graph[x][y]
        
    while y > 0: # y는 c-1도착
        if graph[x][y-1] == -1:
            graph[x][y] =0
            break
        graph[x][y] = graph[x][y-1]
        y -= 1     
    
    x, y = cleaner[1]
    
    while x < R - 1:
        x += 1

        graph[x-1][y] = graph[x][y]
        
    while y < C - 1: # y는 c-1도착
        graph[x][y] = graph[x][y+1]
        y += 1 
        
    while x > cleaner[1][0]:
        x -= 1
        graph[x+1][y] = graph[x][y]
    
    while y > 0: # y는 c-1도착
        if graph[x][y-1] == -1:
      
            graph[x][y] =0
            break
        graph[x][y] = graph[x][y-1]
        y -= 1   
    x, y = cleaner[1]
    graph[x][y] = -1
    graph[x][y+1] = 0
    t += 1
 
    if t == T:
        break
    
answer = 0

for i in range(R):

    answer += sum(graph[i])
answer +=2
print(answer) 