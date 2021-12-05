import copy

fish = [[None] * 4 for _ in range(4) ]
fish_dir = [[None] * 4 for _ in range(4)]
all_answer = []

for i in range(4):
    data = list(map(int,input().split()))
    for j in range(4):
        fish[i][j] = data[j * 2]
        fish_dir[i][j] = data[j * 2 + 1]
    
#print(fish, fish_dir)
#     0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16
dx = [0,-1,-1, 0, 1, 1, 1, 0,-1,-1,-1, 0, 1, 1, 1, 0,-1]
dy = [0, 0,-1,-1,-1, 0 ,1 ,1 ,1, 0,-1,-1,-1, 0 ,1 ,1 ,1]

def fish_movement(x,y,fish_mov_copy, fish_dir_mov_copy):
   
    #nx, ny = x + dx[fish_dir[x][y]], y + dy[fish_dir[x][y]]
    i = 0
    while True:   #상어가 있꺼나 칸을 벗어나면 그리고 물고기가 없다면
        #(nx < 0 or ny < 0 or nx >= 4 or ny >= 4) or fish[nx][ny] == 100 or fish[nx][ny] == -1
        if i == 9:
            return

        nx, ny = x + dx[fish_dir_mov_copy[x][y] + i], y + dy[fish_dir_mov_copy[x][y] + i]
        
        if (nx < 0 or ny < 0 or nx >= 4 or ny >= 4) or fish_mov_copy[nx][ny] == -2: #칸을 벗어나면 상어가 잇으면
            i += 1
            continue
        else:
            break
        '''
        elif fish[nx][ny] == -2: #상어가 잇다면
            i += 1
            continue
        '''
        

    
    fish_mov_copy[x][y], fish_mov_copy[nx][ny] = fish_mov_copy[nx][ny], fish_mov_copy[x][y] 
    temp = fish_dir_mov_copy[x][y] 
    fish_dir_mov_copy[x][y] = fish_dir_mov_copy[nx][ny]
    
    if (temp + i) % 8 == 0:
        fish_dir_mov_copy[nx][ny] = 8
    else:
        fish_dir_mov_copy[nx][ny] = (temp + i) % 8 #0이 되는 경우는?
    return


def fish_turn(fish_2, fish_dir_2):

    fish_num = 1
    find = False
    while True:
        if fish_num > 16:
            return
        for i in range(4):
            for j in range(4):
                if fish_2[i][j] == fish_num:
                    fish_movement(i,j, fish_2, fish_dir_2)
                    #print(fish_2)
                    find = True
                    break
            if find:
                break
                

    #더블루프 진짜 조심하자
        #print(fish_num)
        fish_num += 1
        find = False
        
            



def dfs(x, y, eat_fish_num, fish_dfs, fish_dir_dfs):

    fish_copy = copy.deepcopy(fish_dfs)
    fish_dir_copy = copy.deepcopy(fish_dir_dfs)
    if x < 0 or y < 0 or x >=4 or y >= 4:
        return
    elif fish_copy[x][y] == -1:
        return

    #print(fish_copy[x][y])
    eat_fish_num += fish_copy[x][y]
    all_answer.append(eat_fish_num)
    fish_copy[x][y] = -2
    shark_pos = [x,y]
    shark_dir = fish_dir_copy[x][y]
 
    
    # 여까지 상어가 먹었고
    fish_turn(fish_copy, fish_dir_copy)
    fish_copy[x][y] = -1
    '''
    fish_copy1 = copy.deepcopy(fish_copy)
    fish_copy2 = copy.deepcopy(fish_copy)
    fish_copy3 = copy.deepcopy(fish_copy)

    fish_dir_copy1 = copy.deepcopy(fish_dir_copy)   
    fish_dir_copy2 = copy.deepcopy(fish_dir_copy)  
    fish_dir_copy3 = copy.deepcopy(fish_dir_copy)  
'''
    #print(fish_copy)
    dfs(x + dx[shark_dir], y + dy[shark_dir], eat_fish_num, fish_copy, fish_dir_copy)
    dfs(x + dx[shark_dir] * 2, y + dy[shark_dir] * 2, eat_fish_num, fish_copy, fish_dir_copy)
    dfs(x + dx[shark_dir] * 3, y + dy[shark_dir] * 3, eat_fish_num, fish_copy, fish_dir_copy)
    
    return eat_fish_num
    
   
    
dfs(0,0,0,fish,fish_dir)   
 
print(max(all_answer))