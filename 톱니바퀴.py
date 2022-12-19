from collections import deque


graph = [[0]]

for i in range(4):
    graph.append(deque(map(int, input())))


time = int(input())


rotation_list = []
for i in range(time):
    rotation_list.append(list(map(int, input().split())))


# 2번 우측 6번 좌측 N = 0, S = 1 1시계 -1 반시계
def rotate(order, direction): # rotation  바퀴 =  order
    if direction == 1:
        temp = graph[order].pop()
        graph[order].appendleft(temp)
    elif direction == -1:
        temp = graph[order].popleft()
        graph[order].append(temp)


a = [-1,1,-1,1]
b = [1,-1,1,-1]
for i in range(time):
    order, direction = rotation_list[i]
    second_list = [[0]]
    sixth_list = [[0]]
    for j in range(4):
        second_list.append(graph[j+1][2])
        sixth_list.append(graph[j+1][6])    
    
    rotate(order, direction)
    right_order = order
    temp_dircetion = direction
    while True:
        right_order += 1
        if  right_order == 5:
            break
        if sixth_list[right_order] != second_list[right_order-1]:
            if temp_dircetion == -1:
                temp_dircetion =1
            elif temp_dircetion == 1:
                temp_dircetion = -1
            rotate(right_order, temp_dircetion)
        else:
            break
    left_order = order
    temp_dircetion = direction
    while True:
        left_order -= 1
        if  left_order == 0:
            break
        if second_list[left_order] != sixth_list[left_order+1]:
            if temp_dircetion == -1:
                temp_dircetion =1
            elif temp_dircetion == 1:
                temp_dircetion = -1
            rotate(left_order, temp_dircetion)
        else:
            break
    

answer = 0
if graph[1][0] == 1:
    answer += 1
if graph[2][0] == 1:
    answer += 2
if graph[3][0] == 1:
    answer += 4
if graph[4][0] == 1:
    answer += 8
print(answer)    
    