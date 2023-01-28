N = int(input())

graph = []
total = 0
for i in range(N):
    a = list(map(int, input().split()))
    total += sum(a)
    graph.append(a)
    

back = [[0 for _ in range(N)] for _ in range(N)]

answer = []
for i in range(N):
    for j in range(N):
        x, y = i ,j
        
        if x == N-1 :
            continue
        elif y == N -1:
            continue
        
        
        for d_1 in range(1, N-1):
            for d_2 in range(1, N-1):
                if x+d_1 >=N or y-d_1 < 0 or x+d_2 >= N or y+d_2 >=N or x+d_2+d_1 >= N or y+d_2-d_1 >= N or y+d_2-d_1 < 0:
                    continue
                person = [0,0,0,0,0]
                back = [[0 for _ in range(N)] for _ in range(N)]
                #(x,y)(x+d_1, y-d_1)(x+d_2, y+d_2)(x+d2+d1, y+d2-d1)
                four_point = [(x,y),(x+d_1, y-d_1),(x+d_2, y+d_2),(x+d_2+d_1, y+d_2-d_1)]
                back[x][y] = 5
                d = 0
                while True:
                    d += 1
                    back[x+d][y-d] = 5
                    if x+d == x+d_1:
                        break
                d = 0
                while True:
                    d += 1
                    back[x+d][y+d] = 5
                    if x+d == x+d_2:
                        break   
                 
                d = 0
                while True:
                    d += 1
                    back[x+d_1+d ][y-d_1+d] = 5
                    if x+d_1+d == x+d_1+d_2:
                        break            
                
                d = 0
                while True:
                    d += 1
                    back[x+d_2+d ][y+d_2-d] = 5
                    if x+d_2+d == x+d_1+d_2:
                        break
                for a in range(x+d_1):  # 2 + 2 - 1  0,1,2
                    for b in range(y+1):
             
                        if back[a][b] == 5:
                            break
            
                        person[0] += graph[a][b]   
                
                for a in range(x+d_2+1):  # 2 + 2 - 1  0,1,2
                    for b in range(N-1 , y , -1): #6 5 4
                        if back[a][b] == 5:
                            break
                        person[1] += graph[a][b] 
                # 0 1
                for a in range(x+d_1, N):  # 2 + 2 - 1  0,1,2
                    for b in range(y - d_1 + d_2): #6 5 4
                        if back[a][b] == 5:
                            break
                        person[2] += graph[a][b]
                
                for a in range(x+d_2+1, N):  # 2 + 2 - 1  0,1,2
                    for b in range(N-1 , y - d_1 + d_2 - 1 , -1 ): #6 5 4
                        if back[a][b] == 5:
                            break
                        person[3] += graph[a][b]       
                
                
                person[4] = total - sum(person)
                answer.append(max(person) - min(person))
                
                        
print(min(answer))
        
        