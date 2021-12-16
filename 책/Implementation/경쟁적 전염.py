from collections import deque
N, K = map(int, input().split())


array = []
data = []


for i in range(N):
    array.append(list(map(int, input().split())))
    for j in range(N):
        if array[i][j] != 0 :
            data.append((array[i][j], 0, i ,j))
            

S, X, Y = map(int, input().split())

X = X - 1
Y = Y - 1

q = deque()
data.sort()
q = deque(data)
print(q)

#상하좌우
dx = [-1, 1, 0, 0]
dy = [0 , 0, -1, 1]


while q:
    virus_num, s ,x, y = q.popleft()
    print(q)
    if s == S:
        break
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            continue
        else:
            if array[nx][ny] == 0:
                array[nx][ny] = virus_num
                q.append((virus_num, s + 1, nx, ny))
        
        
print(array)
print(array[X][Y])












'''
for time in range(S):
    
        
    
    
    
    for virus_num in range(1, K+1):
        for i in range(N):
            for j in range(N): #바이러스가 그 리스트 안에 있다면
                if array[i][j] == virus_num:
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if nx < 0 or ny < 0 or nx >= N or ny >= N:
                            continue
                        elif array[nx][ny] == 0:
                            array[nx][ny] = -array[i][j]
                        else:
                            continue
                        
                        
    
    for i in range(N):
        for j in range(N):
            if array[i][j] < 0:
                array[i][j] = abs(array[i][j])
                    
     
print(array[X][Y])           

                
                
               '''
            
            
            
            
            
            
                    