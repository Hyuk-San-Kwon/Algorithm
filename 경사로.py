import copy

N, L = map(int, input().split())

graph = []
graph_2 = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    graph.append(list(map(int, input().split())))
    
count = 0
for i in range(N): #가로부터
    j = 0
    while j < N:
        temp = copy.deepcopy(graph_2[i])
     
        if j == N - 1:
            count += 1
          
            break
        if graph[i][j] == graph[i][j+1]: # 둘이 높이가 같을떄
            j = j + 1
            continue 
        
        if graph[i][j] != graph[i][j+1]: # 둘이 높이가 다를때
            if abs(graph[i][j] - graph[i][j+1]) >= 2:
                j = j + 1
                graph_2[i] = temp
                break
            
            if (graph[i][j] - graph[i][j+1]) == 1:  # 5 4
                for k in range(1,L+1):
                    temp_j = j + k
                    fail = 0
                    if temp_j >= N:
                        fail = 1
                        break
                    if graph[i][temp_j] != graph[i][j+1]:
                        fail = 1
                        break
                    
                if fail:
                    j = j + 1
                    graph_2[i] = temp
                    break
                
                if not fail:
                    
                    for k in range(1,L+1):
                        temp_j = j + k
                        graph_2[i][temp_j] = -1
                    j = j + 1
                    continue
               
            if (graph[i][j] - graph[i][j+1]) == -1:
                for k in range(1,L+1):
                    temp_j = j + 1 - k
                    fail = 0
                    if temp_j < 0:
                        fail = 1
                        break
                    if graph[i][temp_j] != graph[i][j]:
                        fail = 1
                        break
                    if graph_2[i][temp_j] == -1:
                        fail = 1
                        break
                    
                if fail:
                    j = j + 1
                    graph_2[i] = temp
                    break
                if not fail:
                    
                    for k in range(1,L+1):
                        temp_j = j + 1 - k
                        graph_2[i][temp_j] = -1
                    j = j + 1
                    continue


temp_graph = [[0 for _ in range(N)] for _ in range(N)]
graph_3 = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        temp_graph[j][i] = graph[i][j]
graph = temp_graph      

graph_2 = graph_3
        
for i in range(N): #가로부터
    j = 0
    while j < N:
       
        temp = copy.deepcopy(graph_2[i])
        if j == N - 1:
            count += 1
          
            break
        if graph[i][j] == graph[i][j+1]: # 둘이 높이가 같을떄
            j = j + 1
            continue 
        
        if graph[i][j] != graph[i][j+1]: # 둘이 높이가 다를때
            if abs(graph[i][j] - graph[i][j+1]) >= 2:
                j = j + 1
                graph_2[i] = temp
                break
            
            if (graph[i][j] - graph[i][j+1]) == 1:  # 5 4
                for k in range(1,L+1):
                    temp_j = j + k
                    fail = 0
                    if temp_j >= N:
                        fail = 1
                        break
                    if graph[i][temp_j] != graph[i][j+1]:
                        fail = 1
                        break
                    
                if fail:
                    j = j + 1
                    graph_2[i] = temp
                    break
                
                if not fail:
                    
                    for k in range(1,L+1):
                        temp_j = j + k
                        graph_2[i][temp_j] = -1
                    j = j + 1
                    continue
                   
            
            
            if (graph[i][j] - graph[i][j+1]) == -1:
                for k in range(1,L+1):
                    temp_j = j + 1 - k
                    fail = 0
                    if temp_j < 0:
                        fail = 1
                        break
                    if graph[i][temp_j] != graph[i][j]:
                        fail = 1
                        break
                    if graph_2[i][temp_j] == -1:
                        fail = 1
                        break
                    
                if fail:
                    j = j + 1
                    graph_2[i] = temp
                    break
                if not fail:
                    
                    for k in range(1,L+1):
                        temp_j = j + 1 - k
                        graph_2[i][temp_j] = -1
                    j = j + 1
                    continue
print(count)