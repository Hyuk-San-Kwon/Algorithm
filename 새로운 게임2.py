
N, K = map(int, input().split())

graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))  #0흰색 1빨간색, 2파란색
    
graph_horse = [[[] for _ in range(N)] for _ in range(N)] # 말의 위치

dx = [0, 0,-1, 1]
dy = [1,-1, 0, 0] #우좌상하

horse_pos = [0]
horse_move = []
for i in range(K):
    x, y, dir = map(int, input().split())
    horse_pos.append([x-1,y-1,dir-1]) #마지막
    graph_horse[x-1][y-1].append(i+1)



def movement(x, y, dir, horse_num):
    nx = x + dx[dir]
    ny = y + dy[dir]
  
    if (nx < 0  or ny < 0 or nx >= N or ny >= N) or graph[nx][ny] == 2:

        dir = change_dir_blue(dir)
        idx = get_horse_index(x,y, horse_num)
        nx = x + dx[dir]
        ny = y + dy[dir]
        if (nx < 0  or ny < 0 or nx >= N or ny >= N):
            horse_pos[horse_num] = [x, y, dir]
            return x, y, dir
        if graph[nx][ny] == 2:
            horse_pos[horse_num] = [x, y, dir]
            return x, y, dir
        
        elif graph[nx][ny] == 0:
            end = len(graph_horse[x][y])

            for i in range(idx, end):
                graph_horse[nx][ny].append(graph_horse[x][y][idx])
                if i == idx:
                    horse_pos[graph_horse[x][y][idx]] = [nx, ny, dir]
                    graph_horse[x][y].remove(graph_horse[x][y][idx])
                else:
                    horse_pos[graph_horse[x][y][idx]][0], horse_pos[graph_horse[x][y][idx]][1] = nx, ny
                    graph_horse[x][y].remove(graph_horse[x][y][idx])
            
            return nx, ny, dir
        
        elif graph[nx][ny] == 1:
            end = len(graph_horse[x][y])
            for i in range(end-1, idx-1, -1):
                graph_horse[nx][ny].append(graph_horse[x][y][-1])
                
                if i == idx:
                    horse_pos[graph_horse[x][y][-1]] = [nx, ny, dir]
                    graph_horse[x][y].remove(graph_horse[x][y][-1])
                else:
                    horse_pos[graph_horse[x][y][-1]][0] ,horse_pos[graph_horse[x][y][-1]][1] = nx, ny
                    graph_horse[x][y].remove(graph_horse[x][y][-1])
            
            return nx, ny, dir
        
    elif graph[nx][ny] == 0:
        idx = get_horse_index(x,y, horse_num)
        end = len(graph_horse[x][y])
        for i in range(idx, end):
            graph_horse[nx][ny].append(graph_horse[x][y][idx])

            if i == idx:
                horse_pos[graph_horse[x][y][idx]] = [nx, ny, dir]
                graph_horse[x][y].remove(graph_horse[x][y][idx])
            else:
                horse_pos[graph_horse[x][y][idx]][0], horse_pos[graph_horse[x][y][idx]][1] = nx, ny
                graph_horse[x][y].remove(graph_horse[x][y][idx])
        
        return nx, ny, dir    
    
    elif graph[nx][ny] == 1:
        idx = get_horse_index(x,y, horse_num)
        end = len(graph_horse[x][y])
        for i in range(end-1, idx-1, -1):
            graph_horse[nx][ny].append(graph_horse[x][y][-1])
            
            if i == idx:
                horse_pos[graph_horse[x][y][-1]] = [nx, ny, dir]
                graph_horse[x][y].remove(graph_horse[x][y][-1])
            else:
                horse_pos[graph_horse[x][y][-1]][0] ,horse_pos[graph_horse[x][y][-1]][1] = nx, ny
                graph_horse[x][y].remove(graph_horse[x][y][-1])
        
        return nx, ny, dir
        
        
def get_horse_index(x,y, horse_num):
    return graph_horse[x][y].index(horse_num)

def change_dir_blue(dir):
    if dir == 0:
        dir = 1
    elif dir == 1:
        dir = 0
    elif dir == 2:
        dir = 3
    elif dir == 3:
        dir = 2
    
    return dir

time = 0
SUCCESS = 0
while True:
    time += 1
    if time == 1001:
        break
    for horse_num in range(1, len(horse_pos)):
        x, y, dir = horse_pos[horse_num]
        x, y, dir = movement(x, y, dir, horse_num)
        if len(graph_horse[x][y]) >= 4:
            SUCCESS = 1
            break
     

    if SUCCESS == 1:
        break
if time == 1001:
    print(-1)
else: 
    print(time)
            

#graph_horse 말 위치 horse_pos 말 좌표
