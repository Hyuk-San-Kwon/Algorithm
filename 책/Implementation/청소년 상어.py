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
    x =0
    y = 0
    for i in range(4):
        for j in range(4):
            if fish_num1[i][j] == fish:
                found = True
                x= i 
                y= j
                break
            
            
    if found == False:
        return
        
    direction = fish_dir1[x][y]
    for k in range(8):
        
        a = direction + k
        nx = x + dir[a][0]
        ny = y + dir[a][1]
        if nx < 0 or ny < 0 or nx >=4 or ny >=4:
            continue
        elif fish_num1[nx][ny] == 100: #상어 숫자
            continue
        else:
            fish_num1[x][y], fish_num1[nx][ny] =  fish_num1[nx][ny] ,fish_num1[x][y]
            if a >= 9:
                a -= 8
            fish_dir1[x][y] = a
            fish_dir1[x][y], fish_dir1[nx][ny] =  fish_dir1[nx][ny],fish_dir1[x][y]
            return
  
  

  
  

   
eat_count = 0       
eat_count += fish_num[0][0]
fish_num[0][0] = 100
fish_dir[0][0] = 6



answer = []

def shark_move(shark_x_dir, shark_y_dir, eat_count , fish_num1, fish_dir1):
    
    fish_num2 = copy.deepcopy(fish_num1)
    fish_dir2 = copy.deepcopy(fish_dir1)
    if eat_count == 136:
        answer.append(eat_count)
        return
    for i in range(1,17):
        fish_move(i, fish_num2, fish_dir2)

        
        
        
    for i in range(1,4):
        #print(fish_dir2[shark_x_dir][shark_y_dir])
        nx = shark_x_dir + i * dir[fish_dir2[shark_x_dir][shark_y_dir]][0]
        ny = shark_y_dir + i * dir[fish_dir2[shark_y_dir][shark_y_dir]][1]
        if nx< 0 or ny<0 or nx>=4 or ny>=4:
            answer.append(eat_count)
            print(fish_num2,eat_count)
            continue
        if fish_num2[nx][ny] == 0:
            print(fish_num2,eat_count)
            continue
        eat_count += fish_num2[nx][ny]

        fish_num2[nx][ny] = 100
        fish_num2[shark_x_dir][shark_y_dir] = 0
        #fish_num2[shark_x_dir][shark_y_dir], fish_num2[nx][ny] =  fish_num2[nx][ny] ,fish_num2[shark_x_dir][shark_y_dir]
        fish_dir2[shark_x_dir][shark_y_dir], fish_dir2[nx][ny] =  fish_dir2[nx][ny],fish_dir2[shark_x_dir][shark_y_dir]
        
        shark_move(nx, ny, eat_count, fish_num2, fish_dir2)
    
shark_move(0,0,eat_count, fish_num, fish_dir)

print(answer)
