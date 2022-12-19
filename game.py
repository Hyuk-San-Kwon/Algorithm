from xml.etree.ElementTree import TreeBuilder


n, m = map(int , (input().split()))

d = [[0] * m for _ in range(n)]


x, y, pos = map(int, (input().split()))

for i in range(n):
    d[i] = list(map(int , (input().split())))
    
for i in range(n):
    print(d[i])
d[x][y] = 1    
    
dx = [-1, 0, 1, 0]
dy = [ 0, 1, 0,-1]  # pos 0 to 3 북 동 남 서 

pos
  
def turn_left(pos):
    pos -= 1
    if pos == -1:
        pos = 3
    
    return pos

count = 1
turn_time = 0

while True:
    
    pos = turn_left(pos)
    
    nx = x + dx[pos]
    ny = y + dy[pos]
    
    if d[nx][ny] == 0:
        d[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue
    
    else:
        turn_time += 1
    print(turn_time)
    
    if turn_time == 4:
        nx = x - dx[pos]
        ny = y - dy[pos]
        
        if d[nx][ny] == 0:
            x = nx
            y = nx
        else:
            break
        turn_time = 0
        
        
for i in range(n):
    print(d[i])
print(count)
    


