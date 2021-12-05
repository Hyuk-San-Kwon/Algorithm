n = int(input())
x,y = 1, 1
plans = input().split()

#상하좌우
dx = [-1, 1, 0, 0]
dy = [0,  0, -1, 1]
move_types = ['U', 'D','L', 'R']

for plan in plans:
    for i in range(4):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            
    if nx <= 0 or ny <= 0 or nx > n or ny > n:
        continue
    else:
        x = nx
        y = ny
        
print(x,y)