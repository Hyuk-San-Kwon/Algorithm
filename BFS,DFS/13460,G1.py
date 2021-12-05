import copy

N, M = map(int, input().split()) # 세로 가로

start_space = [0] * N


for i in range(N):
    data = (input())
    #print(list(data))
    start_space[i] = list(data)
#print(start_space)
answer_list = [11]
#상하좌우
dx = [-1, 1, 0, 0]
dy = [0,  0, -1,1]


def move_bubble(dir, time, space):

    if time == 11:
        return

    xb = 0
    yb = 0 # 파랑구슬 좌표
    xr = 0
    yr = 0 # 빨강구슬 좌표
    now_space = copy.deepcopy(space)
    for i in range(N):
        for j in range(M):
            if space[i][j] == 'R':
                #print(1) 
                xr, yr = i,j
            if space[i][j] == 'B':
                xb, yb = i,j    
    R_exist = True
    B_exist = True
    #위
    if dir == 0:
        #빨간구슬 이동
        while space[xr - 1][yr] == '.' or  space[xr-1][yr] == 'O':
            
            if space[xr-1][yr] == 'O':
                space[xr][yr] = '.'
                R_exist = False
                break
            space[xr][yr] ='.'
            xr = xr - 1
            space[xr][yr] = 'R'
        
        while space[xb - 1][yb] == '.' or space[xb-1][yb] == 'O':
            
            if space[xb-1][yb] == 'O':
                space[xb][yb] = '.'
                B_exist = False
                break
            space[xb][yb] ='.'
            xb = xb - 1
            space[xb][yb] = 'B'

        while space[xr - 1][yr] == '.' or space[xr-1][yr] == 'O':
            
            if space[xr-1][yr] == 'O':
                space[xr][yr] = '.'
                R_exist = False
                break
            space[xr][yr] ='.'
            xr = xr - 1
            space[xr][yr] = 'R'
        
    if dir == 1:
        #빨간구슬 이동
        while space[xr + 1][yr] == '.' or space[xr+1][yr] == 'O':
            
            if space[xr+1][yr] == 'O':
                space[xr][yr] = '.'
                R_exist = False
                break
            space[xr][yr] ='.'
            xr = xr + 1
            space[xr][yr] = 'R'
        
        while space[xb + 1][yb] == '.' or space[xb+1][yb] == 'O':
            
            if space[xb+1][yb] == 'O':
                space[xb][yb] = '.'
                B_exist = False
                break
            space[xb][yb] ='.'
            xb = xb + 1
            space[xb][yb] = 'B'

        while space[xr + 1][yr] == '.' or space[xr+1][yr] == 'O':
            
            if space[xr+1][yr] == 'O':
                space[xr][yr] = '.'
                R_exist = False
                break
            space[xr][yr] ='.'
            xr = xr + 1
            space[xr][yr] = 'R'
        
    if dir == 2:
        #빨간구슬 이동
        while space[xr][yr-1] == '.' or space[xr][yr-1] == 'O':
            
            if space[xr][yr-1] == 'O':
                space[xr][yr] = '.'
                R_exist = False
                break
            space[xr][yr] ='.'
            yr = yr - 1
            space[xr][yr] = 'R'
        
        while space[xb][yb-1] == '.' or space[xb][yb-1] == 'O':
            
            if space[xb][yb-1] == 'O':
                space[xb][yb] = '.'
                B_exist = False
                break
            space[xb][yb] ='.'
            yb = yb - 1
            space[xb][yb] = 'B'

        while space[xr][yr-1] == '.' or space[xr][yr-1] == 'O':
            
            if space[xr][yr-1] == 'O':
                space[xr][yr] = '.'
                R_exist = False
                break
            space[xr][yr] ='.'
            yr = yr - 1
            space[xr][yr] = 'R'

    if dir == 3:
        #빨간구슬 이동
        while space[xr][yr+1] == '.' or space[xr][yr+1] == 'O':
            
            if space[xr][yr+1] == 'O':
                space[xr][yr] = '.'
                R_exist = False
                break
            space[xr][yr] ='.'
            yr = yr + 1
            space[xr][yr] = 'R'
        
        while space[xb][yb+1] == '.' or space[xb][yb+1] == 'O':
            
            if space[xb][yb+1] == 'O':
                space[xb][yb] = '.'
                B_exist = False
                break
            space[xb][yb] ='.'
            yb = yb + 1
            space[xb][yb] = 'B'

        while space[xr][yr+1] == '.' or space[xr][yr+1] == 'O':
            
            if space[xr][yr+1] == 'O':
                space[xr][yr] = '.'
                R_exist = False
                break
            space[xr][yr] ='.'
            yr = yr + 1
            space[xr][yr] = 'R'


    if now_space == space:
        return

    
    
    if B_exist == False:
        
        return
    time += 1
    if R_exist == False and B_exist == True:
        answer_list.append(time)
        return
    
    
    next_space1 = copy.deepcopy(space)
    next_space2 = copy.deepcopy(space)
    next_space3 = copy.deepcopy(space)
    next_space4 = copy.deepcopy(space)
    move_bubble(0, time, next_space1)
    move_bubble(1, time, next_space2)
    move_bubble(2, time, next_space3)
    move_bubble(3, time, next_space4)

next_space1 = copy.deepcopy(start_space)
next_space2 = copy.deepcopy(start_space)
next_space3 = copy.deepcopy(start_space)
next_space4 = copy.deepcopy(start_space)

move_bubble(0, 0, next_space1)
move_bubble(1, 0, next_space2)
move_bubble(2, 0, next_space3)
move_bubble(3, 0, next_space4)

if min(answer_list) == 11:
    print(-1)
else:
    print(min(answer_list))