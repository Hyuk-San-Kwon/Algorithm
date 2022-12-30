
N, M ,H = map(int, input().split() )
from itertools import combinations
import copy

graph = []
graph = [[0 for _ in range(N)] for _ in range(H)]

pos = [[1,1], [5,1], [3,2], [4,2], [1,3], [2,3], [3,4], [5,4]]
    
for i in range(len(pos)):
    
    x, y= pos[i][0], pos[i][1]
    x,y = x-1, y-1
    graph[x][y] = 1 # 우 이동
    graph[x][y+1] = -1 #좌 이동
for i in range(H):
    print(graph[i])




def search(graph):
    temp = graph
  
    for i in range(N):
        start_x = 0
        start_y = i
        for j in range(H):
            start_x = j
       
            if temp[start_x][start_y] == 1:
                start_y += 1
            elif temp[start_x][start_y] == -1:
                start_y -= 1
       
        if start_y != i:
            return -1
        
    return 1

print(search(graph))