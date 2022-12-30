import copy


N, M = map(int, input().split())

graph = []

for i in range(N):
    graph.append(list( map(int,(input().split()))))


pos = []
    
for i in range(N):
    for j in range(M):
        if graph[i][j] != 0 and graph[i][j] != 6:
            pos.append((i,j,))
            
end = len(pos)
answer = []

dx = [-1, 1, 0, 0]
dy = [ 0, 0,-1, 1]





def search(graph, number):

    
    if number == end :
        count = 0
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 0:
                    count += 1
                    
        answer.append(count)
        
        return
    
    x, y = pos[number][0], pos[number][1]     
    
    
    cam = graph[x][y]

    if cam == 1:
        nx, ny  = x, y
        graph_1_1 = copy.deepcopy(graph)
        while True: #상
            nx, ny = nx + dx[0], ny + dy[0]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_1_1[nx][ny] == 6:
                break
            else:
                if graph_1_1[nx][ny] == 0:
                    graph_1_1[nx][ny] = '#'
        
        search(graph_1_1, number+ 1)
        
        nx, ny  = x, y
        
        graph_1_2 = copy.deepcopy(graph)
        while True: #하
            nx, ny = nx + dx[1], ny + dy[1]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_1_2[nx][ny] == 6:
                break
            else:
                if graph_1_2[nx][ny] == 0:
                    graph_1_2[nx][ny] = '#'
        
        search(graph_1_2, number+ 1)
        
        nx, ny  = x, y
        
        graph_1_3 = copy.deepcopy(graph)
        while True: #좌
            nx, ny = nx + dx[2], ny + dy[2]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_1_3[nx][ny] == 6:
                break
            else:
                if graph_1_3[nx][ny] == 0:
                    graph_1_3[nx][ny] = '#'
        
        search(graph_1_3, number+ 1)
        
        
        nx, ny  = x, y
        
        graph_1_4 = copy.deepcopy(graph)
        while True: #좌
            nx, ny = nx + dx[3], ny + dy[3]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_1_4[nx][ny] == 6:
                break
            else:
                if graph_1_4[nx][ny] == 0:
                    graph_1_4[nx][ny] = '#'
        
        search(graph_1_4, number+ 1)
        
            
    if cam == 2:
        nx, ny  = x, y
        graph_2_1 = copy.deepcopy(graph)
        while True: #상
            nx, ny = nx + dx[0], ny + dy[0]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_2_1[nx][ny] == 6:
                break
            else:
                if graph_2_1[nx][ny] == 0:
                    graph_2_1[nx][ny] = '#'
        nx, ny  = x, y
        while True: #하
            nx, ny = nx + dx[1], ny + dy[1]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_2_1[nx][ny] == 6:
                break
            else:
                if graph_2_1[nx][ny] == 0:
                    graph_2_1[nx][ny] = '#'
        
        search(graph_2_1, number+ 1)
        
        
        nx, ny  = x, y
        graph_2_2 = copy.deepcopy(graph)
        while True: #좌
            nx, ny = nx + dx[2], ny + dy[2]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_2_2[nx][ny] == 6:
                break
            else:
                if graph_2_2[nx][ny] == 0:
                    graph_2_2[nx][ny] = '#'
        nx, ny  = x, y
        while True: #우
            nx, ny = nx + dx[3], ny + dy[3]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_2_2[nx][ny] == 6:
                break
            else:
                if graph_2_2[nx][ny] == 0:
                    graph_2_2[nx][ny] = '#'
        
        search(graph_2_2, number+ 1)
    
    
    if cam == 3:
        nx, ny  = x, y
        graph_3_1 = copy.deepcopy(graph)
        while True: #상
            nx, ny = nx + dx[0], ny + dy[0]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_3_1[nx][ny] == 6:
                break
            else:
                if graph_3_1[nx][ny] == 0:
                    graph_3_1[nx][ny] = '#'
        nx, ny  = x, y
        while True: #우
            nx, ny = nx + dx[3], ny + dy[3]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_3_1[nx][ny] == 6:
                break
            else:
                if graph_3_1[nx][ny] == 0:
                    graph_3_1[nx][ny] = '#'
        
        search(graph_3_1, number+ 1)
        
        
        nx, ny  = x, y
        graph_3_2 = copy.deepcopy(graph)
        while True: #우
            nx, ny = nx + dx[3], ny + dy[3]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_3_2[nx][ny] == 6:
                break
            else:
                if graph_3_2[nx][ny] == 0:
                    graph_3_2[nx][ny] = '#'
        nx, ny  = x, y
        while True: #하
            nx, ny = nx + dx[1], ny + dy[1]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_3_2[nx][ny] == 6:
                break
            else:
                if graph_3_2[nx][ny] == 0:
                    graph_3_2[nx][ny] = '#'
        
        search(graph_3_2, number+ 1)
        
        nx, ny  = x, y
        graph_3_3 = copy.deepcopy(graph)
        while True: #하
            nx, ny = nx + dx[1], ny + dy[1]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_3_3[nx][ny] == 6:
                break
            else:
                if graph_3_3[nx][ny] == 0:
                    graph_3_3[nx][ny] = '#'
        nx, ny  = x, y
        while True: #좌
            nx, ny = nx + dx[2], ny + dy[2]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_3_3[nx][ny] == 6:
                break
            else:
                if graph_3_3[nx][ny] == 0:
                    graph_3_3[nx][ny] = '#'
        
        search(graph_3_3, number+ 1)

        
        nx, ny  = x, y
        graph_3_4 = copy.deepcopy(graph)
        while True: #좌
            nx, ny = nx + dx[2], ny + dy[2]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_3_4[nx][ny] == 6:
                break
            else:
                if graph_3_4[nx][ny] == 0:
                    graph_3_4[nx][ny] = '#'
        nx, ny  = x, y
        while True: #상
            nx, ny = nx + dx[0], ny + dy[0]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_3_4[nx][ny] == 6:
                break
            else:
                if graph_3_4[nx][ny] == 0:
                    graph_3_4[nx][ny] = '#'
        
        search(graph_3_4, number+ 1)
        
        
    if cam == 4:
       
        nx, ny  = x, y
        graph_4_1 = copy.deepcopy(graph)
        while True: #좌
            nx, ny = nx + dx[2], ny + dy[2]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_4_1[nx][ny] == 6:
                break
            else:
                if graph_4_1[nx][ny] == 0:
                    graph_4_1[nx][ny] = '#'
                
        nx, ny  = x, y
        while True: #상
            nx, ny = nx + dx[0], ny + dy[0]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_4_1[nx][ny] == 6:
                break
            else:
                if graph_4_1[nx][ny] == 0:
                    graph_4_1[nx][ny] = '#'
        nx, ny  = x, y
        while True: #우
            nx, ny = nx + dx[3], ny + dy[3]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_4_1[nx][ny] == 6:
                break
            else:
                if graph_4_1[nx][ny] == 0:
                    graph_4_1[nx][ny] = '#'
        
        search(graph_4_1, number+ 1)
        
        nx, ny  = x, y
        graph_4_2 = copy.deepcopy(graph)
        
        while True: #상
            nx, ny = nx + dx[0], ny + dy[0]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_4_2[nx][ny] == 6:
                break
            else:
                if graph_4_2[nx][ny] == 0:
                    graph_4_2[nx][ny] = '#'
        nx, ny  = x, y
        while True: #우
            nx, ny = nx + dx[3], ny + dy[3]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_4_2[nx][ny] == 6:
                break
            else:
                if graph_4_2[nx][ny] == 0:
                    graph_4_2[nx][ny] = '#'
        nx, ny  = x, y
        while True: #하
            nx, ny = nx + dx[1], ny + dy[1]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_4_2[nx][ny] == 6:
                break
            else:
                if graph_4_2[nx][ny] == 0:
                    graph_4_2[nx][ny] = '#'
                
                
        search(graph_4_2, number+ 1)
        
        nx, ny  = x, y
        graph_4_3 = copy.deepcopy(graph)
        
        while True: #좌
            nx, ny = nx + dx[2], ny + dy[2]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_4_3[nx][ny] == 6:
                break
            else:
                if graph_4_3[nx][ny] == 0:
                    graph_4_3[nx][ny] = '#'
        nx, ny  = x, y
        while True: #우
            nx, ny = nx + dx[3], ny + dy[3]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_4_3[nx][ny] == 6:
                break
            else:
                if graph_4_3[nx][ny] == 0:
                    graph_4_3[nx][ny] = '#'
        nx, ny  = x, y
        while True: #하
            nx, ny = nx + dx[1], ny + dy[1]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_4_3[nx][ny] == 6:
                break
            else:
                if graph_4_3[nx][ny] == 0:
                    graph_4_3[nx][ny] = '#'
                
                
        search(graph_4_3, number+ 1)
        
        
        nx, ny  = x, y
        graph_4_4 = copy.deepcopy(graph)
        
        while True: #좌
            nx, ny = nx + dx[2], ny + dy[2]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_4_4[nx][ny] == 6:
                break
            else:
                if graph_4_4[nx][ny] == 0:
                    graph_4_4[nx][ny] = '#'
        nx, ny  = x, y
        while True: #상
            nx, ny = nx + dx[0], ny + dy[0]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_4_4[nx][ny] == 6:
                break
            else:
                if graph_4_4[nx][ny] == 0:
                    graph_4_4[nx][ny] = '#'
        nx, ny  = x, y
        while True: #하
            nx, ny = nx + dx[1], ny + dy[1]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_4_4[nx][ny] == 6:
                break
            else:
                if graph_4_4[nx][ny] == 0:
                    graph_4_4[nx][ny] = '#'
                
                
        search(graph_4_4, number+ 1)
        
    if cam == 5:
       
        nx, ny  = x, y
        graph_5_1 = copy.deepcopy(graph)
        while True: #좌
            nx, ny = nx + dx[2], ny + dy[2]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_5_1[nx][ny] == 6:
                break
            else:
                if graph_5_1[nx][ny] == 0:
                    graph_5_1[nx][ny] = '#'
                
        nx, ny  = x, y
        while True: #상
            nx, ny = nx + dx[0], ny + dy[0]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_5_1[nx][ny] == 6:
                break
            else:
                if graph_5_1[nx][ny] == 0:
                    graph_5_1[nx][ny] = '#'
        nx, ny  = x, y
        while True: #우
            nx, ny = nx + dx[3], ny + dy[3]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_5_1[nx][ny] == 6:
                break
            else:
                if graph_5_1[nx][ny] == 0:
                    graph_5_1[nx][ny] = '#'
        
        nx, ny  = x, y
        while True: #하
            nx, ny = nx + dx[1], ny + dy[1]
            if nx < 0 or ny < 0 or nx >= N or ny >=M:
                break
            if graph_5_1[nx][ny] == 6:
                break
            else:
                if graph_5_1[nx][ny] == 0:
                    graph_5_1[nx][ny] = '#'
        
        search(graph_5_1, number+ 1)


search(graph, 0)
print(min(answer))