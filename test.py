
N, M ,H = map(int, input().split() )
from itertools import combinations
import copy

graph = []
graph = [[0 for _ in range(N)] for _ in range(H)]

    
for i in range(M):
    
    x, y= map(int, input().split())
    x,y = x-1, y-1
    graph[x][y] = 1 # 우 이동
   

pos = []

for i in range(H):
    for j in range(N-1):
        if graph[i][j] == 0 :
            pos.append([i,j])



def search(graph):
    temp = graph
   
    for i in range(N):
        start_x = 0
        start_y = i
        for j in range(H):
            start_x = j
       
            if temp[start_x][start_y] == 1:
                start_y += 1
            elif start_y >= 1:
                if temp[start_x][start_y - 1] == 1:
                    start_y -= 1
       
        if start_y != i:
            return -1
        
    return 1
a = -1
answer =[]
graph_2 = copy.deepcopy(graph)
a = search(graph_2)
if a == 1:
    answer.append(0)
if answer:
    print(min(answer))
else:
    for i in range(len(pos)):
        graph_2 = copy.deepcopy(graph)
        x, y = pos[i][0], pos[i][1]
        if 0 <=  y + 1 <N:
            if graph_2[x][y+1] == 1:
                continue
        if 0 <=y - 1 <N :
            if graph_2[x][y-1] == 1:
                continue
        
        graph_2[x][y] = 1
    
        
        
        a = search(graph_2)
        if a == 1:
            answer.append(1)
            break
    
    if answer:
        print(min(answer))
    else:

        pos_2 = list(combinations(pos,2))

        for i in range(len(pos_2)):
            graph_2 = copy.deepcopy(graph)
            x, y = pos_2[i][0][0], pos_2[i][0][1]
            if 0 <=  y + 1 <N:
                if graph_2[x][y+1] == 1:
                    continue
            if 0 <=y - 1 <N :
                if graph_2[x][y-1] == 1:
                    continue
            graph_2[x][y] = 1
            
        
            
            x, y = pos_2[i][1][0], pos_2[i][1][1]
            if 0 <=  y + 1 <N:
                if graph_2[x][y+1] == 1:
                    continue
            if 0 <=y - 1 <N :
                if graph_2[x][y-1] == 1:
                    continue
            graph_2[x][y] = 1
          
        
            a = search(graph_2)
            if a == 1:
                answer.append(2)
                break
        if answer:
            print(min(answer))
        else:


            pos_3 = list(combinations(pos,3))
            for i in range(len(pos_3)):
                graph_2 = copy.deepcopy(graph)
                x, y = pos_3[i][0][0], pos_3[i][0][1]
                if 0 <=  y + 1 <N:
                    if graph_2[x][y+1] == 1:
                        continue
                if 0 <=y - 1 <N :
                    if graph_2[x][y-1] == 1:
                        continue
                graph_2[x][y] = 1
              
                
                x, y = pos_3[i][1][0], pos_3[i][1][1]
                if 0 <=  y + 1 <N:
                    if graph_2[x][y+1] == 1:
                        continue
                if 0 <=y - 1 <N :
                    if graph_2[x][y-1] == 1:
                        continue
                graph_2[x][y] = 1
             
                
                x, y = pos_3[i][2][0], pos_3[i][2][1]
                if 0 <=  y + 1 <N:
                    if graph_2[x][y+1] == 1:
                        continue
                if 0 <=y - 1 <N :
                    if graph_2[x][y-1] == 1:
                        continue
                graph_2[x][y] = 1
            
            
                    
                a = search(graph_2)
                if a == 1:
                    answer.append(3)
                    break

            if answer:
                print(min(answer))
            else:
                print(-1)

        