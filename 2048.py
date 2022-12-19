import copy
from itertools import product
n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int, input().split())))

def movement(dir, graph):
    
    if dir == 1:
        
        for i in range(n):
         
            zero_count = 0
            j = -1
            while j < n - 1:
                y = i
                j = j + 1 
                
                if graph[y][j] == 0:
                    now = y
                    while graph[y][j] == 0:
                        y = y +1
                        if y == n:
                            break
                    if y == n:
                        continue
                    count = y - now
                    while (now + count) < n:

                        graph[now][j] = graph[now+count][j]
           
                        now = now + 1
                    graph[n-1][j] = 0
                    
        
        for i in range(n):
            for j in range(n):
                if graph[i][j] != 0:
                    if i == n-1:
                        continue
                    if graph[i][j] == graph[i+1][j]:
                        graph[i][j]= graph[i][j]*2
                        graph[i+1][j] = 0
                        now = i+1
                        while now < n-1:
                            graph[now][j] =graph[now+1][j]
                            now += 1
                        graph[n-1][j] = 0
                            
        
    
    if dir == 2:
        rumble(1,graph)
        graph = movement(1,graph)
        rumble(1,graph)
        
    if dir == 3: #좌
        rumble(2,graph)
        graph = movement(1,graph)
        rumble(3,graph)
        
    if dir == 4: # 우
        rumble(3,graph)
        graph = movement(1,graph)
        rumble(2,graph)
    return graph 
        
       
    
def rumble(dir,graph):
    if dir == 1: # 상하 반전
        for i in range(int(n/2)):
            temp = graph[i]

            graph[i] = graph[n-1-i]
            graph[n-1-i] = temp
    
    if dir == 2: #우로 회전
        temp = copy.deepcopy(graph)
        for i in range(n):
            for j in range(n):
                graph[i][j] = temp[n-1-j][i]
                
    if dir == 3: #좌로 회전
        temp = copy.deepcopy(graph)
        for i in range(n):
            for j in range(n):
                graph[i][j] = temp[j][n-1-i]


a= [1,2,3,4]
answer = [2]
temp = list(product(a, repeat = 5))
'''
print(temp[0])
temp_graph = copy.deepcopy(graph)
for j in (temp[10]):
    
    temp_graph = movement(j, temp_graph)
    for i in range(n):
        print(temp_graph[i])
    print()
'''
temp = list(product(a, repeat = 5))
for i in temp:
 
    temp_graph = copy.deepcopy(graph)
    
    for j in range(len(i)):
        movement(i[j], temp_graph)
    
    
    if answer and max(map(max, temp_graph)) > max(answer) :
        answer.append(max(map(max, temp_graph)))
print((answer))

