import copy
import sys
sys.setrecursionlimit(5000)

global time
time = 0
global M
M = 0
global now_shark_num
now_shark_num = 0

N, M, k = map(int, input().split()) #N 정사각형 크기, M 상어 수, k 냄새 남아있는 시간
now_shark_num = M
space = [0] * 500 #나중 수정
smell_space = [[[0,0] for _ in range(N)] for _ in range(N)] #더블 리스트는 이렇게 만들자

#print(smell_space)

for i in range(N):
    space[i] = list(map(int, input().split()))

#print(space)
for i in range(N):
    for j in range(N):
        if space[i][j] > 0 :
            smell_space[i][j] = [space[i][j], k] #앞칸 상어 번호, k 냄새 남은 것


#print(smell_space)


shark_dir = list(map(int, input().split()))
shark_dir.insert(0, 0)

#print(shark_dir)  #현재 상어의 방향

shark_next = [[0] for _ in range(500)] 

#상하좌우
dx = [0,-1, 1, 0 , 0]
dy = [0, 0,  0, -1,1]

for i in range(1, M + 1):
    
    
    data = list(map(int, input().split()))
    data.insert(0,0)
    shark_next[i].append(data)
    data = list(map(int, input().split()))
    data.insert(0,0)
    shark_next[i].append(data)
    data = list(map(int, input().split()))
    data.insert(0,0)
    shark_next[i].append(data)
    data = list(map(int, input().split()))
    data.insert(0,0)
    shark_next[i].append(data)


def shark_movement(now_space, now_shark_dir, now_smell_space):

    global time
    num = M
    x = 0
    y = 0
    global now_shark_num
  
    
    while True:
        num = M
        if now_shark_num == 1:
            print(time)
            return
        if time == 1000:
            print(-1)
            return

        before_space = copy.deepcopy(now_space)
        before_shark_dir = copy.deepcopy(now_shark_dir)
        before_smell_space = copy.deepcopy(now_smell_space)

        while num >= 1:
            
            moving_list_1 = []
            moving_list_2 = []
            num_found = False
            x = 0
            y = 0
            for i in range(N):
                for j in range(N):
                    if before_space[i][j] == num:
                        x,y = i,j
                        num_found = True
                        break
        
            if num_found == False:
                num -= 1
                continue
                
            found = False
            
            for i in range(1,5):
                nx = x + dx[i]
                ny = y + dy[i]
                #print(smell_space[nx][ny])
                #냄새가 없는칸을 찾는다
                if (not (nx < 0 or ny <0 or nx >= N or ny >= N)) :
                    if before_smell_space[nx][ny][1] == 0 :
                        moving_list_1.append((nx, ny))
                        found = True
                
                #없으면 최근에 거쳐온 칸을 찾는다.
                if (not (nx < 0 or ny <0 or nx >= N or ny >= N)):
                    if num == before_smell_space[nx][ny][0] and before_smell_space[nx][ny][1] >= 1:
                        moving_list_2.append((nx,ny))

                    
            if found == True:
                nx = 0
                ny = 0
                for i in range(1,5): 
        
                    if (x + dx[shark_next[num][before_shark_dir[num]][i]], y + dy[shark_next[num][before_shark_dir[num]][i]]) in moving_list_1:
                
                        nx, ny = x + dx[shark_next[num][before_shark_dir[num]][i]], y + dy[shark_next[num][before_shark_dir[num]][i]]
                        now_space[x][y] = 0
                        #smell_space[x][y] = [num, k-1]
                        if now_space[nx][ny] > num:
                            now_shark_num -= 1
                        now_space[nx][ny] = num
                        now_smell_space[nx][ny] = [num,k + 1]
                        break
                        #상어의 전에 이동방향을 넣어서 다음 이동방향 찾기

                

                Dx, Dy = x + dx[shark_next[num][before_shark_dir[num]][i]] - x, y + dy[shark_next[num][before_shark_dir[num]][i]] - y
                if (Dx,Dy) == (-1,0):
                    now_shark_dir[num] = 1
                if (Dx,Dy) == (1,0):
                    now_shark_dir[num] = 2
                if (Dx,Dy) == (0,-1):
                    now_shark_dir[num] = 3
                if (Dx,Dy) == (0,1):
                    now_shark_dir[num] = 4  


            if found == False:
                i = 0
                for i in range(1,5):  
                    #i = i-1
                    #print(1)
                    if (x + dx[shark_next[num][before_shark_dir[num]][i]], y + dy[shark_next[num][before_shark_dir[num]][i]]) in moving_list_2:
                        now_space[x][y] = 0
                        #print(1)
                        nx, ny = x + dx[shark_next[num][before_shark_dir[num]][i]], y + dy[shark_next[num][before_shark_dir[num]][i]]
                        if (now_space[nx][ny]) > num:
                            now_shark_num -= 1
                        now_space[nx][ny] = num
                        now_smell_space[nx][ny] = [num,k + 1]
                        break

                Dx, Dy = x + dx[shark_next[num][before_shark_dir[num]][i]] - x, y + dy[shark_next[num][before_shark_dir[num]][i]] - y

                if (Dx,Dy) == (-1,0):
                    now_shark_dir[num] = 1
                if (Dx,Dy) == (1,0):
                    now_shark_dir[num] = 2
                if (Dx,Dy) == (0,-1):
                    now_shark_dir[num] = 3
                if (Dx,Dy) == (0,1):
                    now_shark_dir[num] = 4

            
            num -= 1
        
        for i in range(N):
            for j in range(N):
                if now_smell_space[i][j][1] > 0:
                    now_smell_space[i][j][1] -= 1
        #print(now_space)
        #print(now_smell_space)
        time += 1

 

shark_movement(space, shark_dir,smell_space)




