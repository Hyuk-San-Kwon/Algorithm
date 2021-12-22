import copy

fish_num = [[],[],[],[]]
fish_dir = [[] ,[],[],[]      ]


for i in range(4):
    a = list(map(int, input().split()))
    for j in range(0,8,2):
        fish_num[i].append(a[j])
        fish_dir[i].append(a[j+1])

dir = [(0,0),(-1,0),(-1,-1),(0, -1), (1,-1), (1,0),(1,1)  ,(0,1),(-1,1),  (-1,0),(-1,-1),(0, -1), (1,-1), (1,0),(1,1)  ,(0,1),(-1,1)]   

def fish_move(fish, fish_num1, fish_dir1):
    found = False
    for i in range(4):
        for j in range(4):
            if fish_num1[i][j] == fish:
                found = True
                break
    if found == False:
        return
        
    direction = fish_dir1[i][j]
    for k in range(8):
        
        a = direction + k
        nx = i + dir[a][0]
        ny = j + dir[a][1]
        if nx < 0 or ny < 0 or nx >=3 or ny >=3:
            continue
        elif fish_num == 100: #상어 숫자
            continue
        else:
            fish_num1[i][j], fish_num1[nx][ny] =  fish_num1[nx][ny] ,fish_num1[i][j]
            if a >= 9:
                a -= 8
            fish_dir1[i][j] = a
            fish_dir1[i][j], fish_dir1[nx][ny] =  fish_dir1[nx][ny],fish_dir1[i][j]
            break
  
  

  
  

   
eat_count = 0       
eat_count += fish_num[0][0]
fish_num[0][0] = 100
fish_dir[0][0] = 6



answer = []

def shark_move(shark_x_dir, shark_y_dir, eat_count , fish_num12, fish_dir12):
    
    fish_num2 = copy.deepcopy(fish_num12)
    fish_dir2 = copy.deepcopy(fish_dir12)
    if eat_count == 136:
        answer.append(eat_count)
        return
    for i in range(1,17):
        
        fish_move(i, fish_num2, fish_dir2)
        
        
        
        
    for i in range(1,4):
        #print(fish_dir2[shark_x_dir][shark_y_dir])
        nx = shark_x_dir + i * dir[fish_dir2[shark_x_dir][shark_y_dir]][0]
        ny = shark_y_dir + i * dir[fish_dir2[shark_y_dir][shark_y_dir]][1]
        if nx< 0 or ny<0 or nx>=3 or ny>=3:
            answer.append(eat_count)
            continue
        if fish_num2[nx][ny] == 0:
            continue
        eat_count += fish_num2[nx][ny]
        fish_num2[nx][ny] = 0
        fish_num2[shark_x_dir][shark_y_dir], fish_num2[nx][ny] =  fish_num2[nx][ny] ,fish_num2[shark_x_dir][shark_y_dir]
        fish_dir2[shark_x_dir][shark_y_dir], fish_dir2[nx][ny] =  fish_dir2[nx][ny],fish_dir2[shark_x_dir][shark_y_dir]
        shark_move(nx, ny, eat_count, fish_num2, fish_dir2)
    
shark_move(0,0,eat_count, fish_num, fish_dir)

print(answer)
