from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
size = int(2)

space = []
for i in range(n):
    space.append(list(map(int, input().split())))
#상좌우하
dx = [-1,0,0,1]
dy = [0,-1,1,0]

for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            x,y = i ,j
            break


def searching(x,y,z,queue,answer,size ):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z
 
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        elif space[nx][ny] != 0 and space[nx][ny] > size:
            continue
        elif space[nx][ny] == 0:
            nz += 1
            space[nx][ny] = 99 #지나옴
            queue.append((nx,ny,nz))
            continue
        elif space[nx][ny] == size:
            nz += 1
            space[nx][ny] = 10 #지나옴
            queue.append((nx,ny,nz))
            continue
        elif space[nx][ny] < size:
            nz += 1
            answer.append((nx,ny,nz))
        

            
    




def bfs(x,y,size):

    orix, oriy = x, y
    queue = deque()
    queue.append((x,y,0))
    eatcounts = 0
    movement = 0
    answer = deque()
    change = False

    while queue:
        

        x,y,z = queue.popleft()
        queue.append((x,y,z))


        while queue:
            x,y,z = queue.popleft()
            searching(x,y,z,queue,answer,size)
      
     
        x,y,z = 10e9,10e9,10e9
        while answer:
            while queue:
                queue.pop()
            change = True
            
            #print(answer)
            nx, ny, nz = answer.pop()
            
            if nz < z:
                z = nz
                x = nx
                y = ny
                
                
            if nz == z:
                if nx < x:
                    x = nx
                    y = ny
                    
                elif nx == x:
                    if ny < y:
                        y = ny
            #print(x, y, z)


        if change == True:
            
            eatcounts += 1
            #print(eatcounts)
            
                        
            for j in range(n):
                for k in range(n):
                    if space[j][k] == 99:
                        space[j][k] = 0
                    elif space[j][k] == 10:
                        space[j][k] = size
                                    
            if eatcounts == size and size < 7:
                size += 1
                eatcounts = 0


            space[orix][oriy] = 0
            space[x][y] = 9
            orix, oriy = x, y
            movement = z 
            queue.append((x,y,z))
            #print(space)
            change = False
            #print(space)
    return movement


print(bfs(x,y,size))
