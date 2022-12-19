
N = int(input())

apple_num = int(input())

graph = [[0 for _ in range(N)] for _ in range(N)]

for i in range(apple_num):
    x ,y = map(int,(input().split()))
    graph[x-1][y-1] = 1
    
#print(graph)

turn_time = int(input())

turn = []

for i in range(turn_time):
    a,b = input().split()
    a = int(a)
    turn.append((a,b))


time = 0

direction = 0# 0123 우하좌상

dx = [ 0, 1, 0,-1]
dy = [ 1, 0,-1, 0]
x,y = 0,0
graph[0][0] = -1
snake = []
snake.append((x,y))

turn_count = 0
while True:
    time += 1
   
    x, y = snake[0]
    
    nx = x + dx[direction]
    ny = y + dy[direction]
    
    if nx < 0 or ny < 0 or nx >= N or ny >= N:
        break
    if (nx, ny) in snake:
        break
    if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        graph[nx][ny] = -1
        snake.insert(0, (nx, ny))
    else:
        snake.insert(0, (nx, ny))
        kx, ky = snake.pop()
        graph[kx][ky] = 0
        graph[nx][ny] = -1
    x = nx
    y = ny
    if turn_count < turn_time and turn[turn_count][0] == time:
        #print(time, 'turn')
        if turn[turn_count][1] == 'L':
            direction -= 1
            if direction == -1:
                direction = 3
        if turn[turn_count][1] == 'D':
            direction += 1
            if direction == 4:
                direction = 0    
        turn_count +=1
    #for i in range(N):
    #    print(graph[i])
    #print()
print(time)
    