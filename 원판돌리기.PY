
N, M, T = map(int,input().split())  # 반지름 길이, 정수 갯수, 회전 횟수


graph = [[-1 for _ in range(M)] for _ in range(N+1)] # 첫쨰줄 더미값

for i in range(N):
    temp = list(map(int, input().split()))
    graph[i + 1] = temp

act_list = []

for i in range(T):
    temp = list(map(int, input().split()))
    act_list.append(temp)

def left_move(moved_list):
    temp = moved_list[0]
    for i in range(len(moved_list) - 1):
        moved_list[i]=moved_list[i+1]
    moved_list[-1] = temp
    
def right_move(moved_list):
    temp = moved_list[-1]
    for i in range((len(moved_list) - 1), 0 ,-1 ):
        moved_list[i]=moved_list[i-1]
    moved_list[0] = temp

    
def rotate(x, d, k): # temp의 값 집어넣기
    ori_x = x 
    while True:

        if x >= N + 1:
            return
        
        if d == 0: #시계방향
            for i in range(k):
                right_move(graph[x])
        
        elif d == 1:
            for i in range(k):
                left_move(graph[x])
                
        x = x + ori_x

dx = [-1, 1, 0, 0] # 상하좌우
dy = [ 0, 0,-1, 1]

def search(graph):
    same = []
    for x in range(1, N + 1):
        for y in range(M):
            if graph[x][y] == -1:
                continue
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx == 0:
                    continue
                elif nx == N+1:
                    continue
                elif ny == M:
                    ny = 0
                elif ny == -1:
                    ny = M - 1
                if graph[nx][ny] == -1:
                    continue
                if graph[x][y] == graph[nx][ny]:
                    same.append([x,y])
                    same.append([nx,ny])                 
                
            
    if same:
        for i in range(len(same)):
            x, y = same[i]
            graph[x][y] = -1           
    else:
        sum = 0
        count = 0.0
        for x in range(1, N + 1):
            for y in range(M):
                if graph[x][y] == -1:
                    continue
                sum += graph[x][y]
                count += 1.0
        if count == 0:
            return
        average = sum / count
        
        for x in range(1, N + 1):
            for y in range(M):
                if graph[x][y] == -1:
                    continue
                if graph[x][y] < average:
                    graph[x][y] += 1
                    continue
                elif graph[x][y] > average:
                    graph[x][y] -= 1
                    continue
                
        
        

for i in range(T):
    x, d, k = act_list[i]
    rotate(x,d,k)
    search(graph)
    

sum = 0
for x in range(1, N + 1):
    for y in range(M):
        if graph[x][y] == -1:
            continue
        sum += graph[x][y]

print(sum)