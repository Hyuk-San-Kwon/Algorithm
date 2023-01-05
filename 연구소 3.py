from itertools import combinations
from collections import deque
import copy


N, M = map(int, input().split())

graph = []


for i in range(N):
    graph.append(list( map(int, input().split())))
  

viruses = []  
    
for i in range(N):
    for j in range(N):
        if graph[i][j] == 2:
            viruses.append((i,j))
        if graph[i][j] == 1:
            graph[i][j] = '-'
            
dx = [-1, 1, 0, 0]
dy = [ 0, 0,-1 ,1]


queue = deque()
answer = []
for virus_combi in combinations(viruses,M):
    graph_copyed = copy.deepcopy(graph)
    for i in range(len(virus_combi)):
        
     
        #for j in range(len(virus_combi[i])):
        x, y = virus_combi[i]
        graph_copyed[x][y] = '2'
        queue.append((x,y,0))
    temp = []
    while queue:
        x, y, t = queue.popleft()
        
        
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            elif graph_copyed[nx][ny] == '-':
                continue
            elif graph_copyed[nx][ny] == '2':
                continue
            elif graph_copyed[nx][ny] == 0:
                graph_copyed[nx][ny] = t + 1
                queue.append((nx, ny, t + 1)) 
                temp.append(t+1)
            elif graph_copyed[nx][ny] == 2:
                graph_copyed[nx][ny] = '*'
                queue.append((nx, ny, t + 1))       
    fail = 0 
    for i in range(len(graph_copyed)):
    
        if 0 in graph_copyed[i]:
            fail = 1
            break
    if fail == 0:
        
        if temp:
            answer.append(max(temp)) 

        else:
            answer.append(0)
if answer:
    print(min(answer))         
else:
    print(-1)


