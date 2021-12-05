n, m = map(int, input().split())

x, y, dir = map(int, input().split())

count = 0
array = []
for i in range(n):
    array.append(list(map(int, input().split())))
 
#상좌하우
dx = [-1, 0, 1, 0, -1, 0, 1, 0]
dy = [ 0,-1, 0, 1 , 0,-1, 0, 1]

def dir_change(dir):
    dir += 1
    if dir == 4:
        dir = 0
        
    return dir


while True:
    for i in range(4):
        array[x][y] = -1
        dir = dir_change(dir)
        nx = x + dx[dir]
        ny = y + dy[dir]
        if array[nx][ny] == 0:
            x = nx
            y = ny
            i = 0
            count += 1
    
    nx = x + dx[dir + 2]
    ny = y + dy[dir + 2]    
    print(dir)
    if array[nx][ny] == 1:
        print(1)
        break
    else:
        x = nx
        y = ny
        count += 1
print(count)
           