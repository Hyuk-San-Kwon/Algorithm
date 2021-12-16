from collections import deque
    
N = int(input())

array = []
data = []

for i in range(N):
    array.append(list(map(int, input().split())))
    for j in range(N):
        if array[i][j] != 0 and array[i][j] != 9:
            data.append((i,j, array[i][j]))
        elif array[i][j] == 9:
            X, Y = i, j


data.sort(key= lambda x: x[2])

q = deque(data)

size = 2
eat_num = 0
time = 0

while q:
    fish_temp = []
    print(q)
    print(q[0][2])
    while q[0][2] < size:
        x, y, fish_num = q.popleft()
        fish_temp.append((abs(X-x) + abs(Y-y), X-x, Y-y, x, y ,fish_num))
    
    if fish_temp == []:
        break   
        
        
    fish_temp.sort(key=lambda x: (x[0] , x[2], x[1]))
    if fish_temp:
        dis , x_dis, y_dis, x, y ,fish_num = fish_temp.pop(0)
 
    array[x][y] = 9
    array[X][Y] = 0
    X, Y = x, y
    eat_num += 1
    time += dis
    if eat_num == size:
        eat_num = 0
        size += 1
    fish_temp.sort(key= lambda x: x[5])
    fish_temp.reverse()
    for i in range(len(fish_temp)):
        dis , x_dis, y_dis, x, y ,fish_num = fish_temp[i]
        q.appendleft((x, y ,fish_num))



print(time)
    
    
