from itertools import combinations
from collections import deque

N, M = map(int, input().split())


array = []

two_list = []
one_list = []


dx = [-1, 1, 0, 0]
dy = [ 0, 0, -1,1]


for i in range(N):
    array.append(list(map(int, input().split())))
    for j in range(N):
        if array[i][j] == 2:
            two_list.append((i,j))
        if array[i][j] == 1:
            one_list.append((i,j))

a= list(combinations(two_list, len(two_list) - M ))  #삭제할 치킨집 순번

answers = []

def solution(  delete_pos    ):
    del_temp_list = []
    for i in range(len(delete_pos)):
        x, y = delete_pos[i]
        del_temp_list.append((x,y))
        array[x][y] = 0
    #print(array)
    sum_dis = 0
    for i in range(len(one_list)):
        q = deque()
        pos_and_dis = ( one_list[i][0], one_list[i][1], 0 )
        q.append(pos_and_dis)
        
        while q:
            x, y, distance = q.popleft()

            for j in range(4):
                nx = x + dx[j]
                ny = y + dy[j]
                if nx < 0 or ny < 0 or ny >= N or nx >= N:
                    continue
                
                
                
                elif array[nx][ny] == 2:
                    while q:
                        q.popleft()
                    sum_dis += distance + 1
                    break
                   
                
                elif nx >= 0 or ny >= 0 or ny < N or nx < N:
                    q.append((nx, ny, distance + 1))
                    
    answers.append(sum_dis)
    sum_dis= 0
    #print(array)   
    for k in range(len(del_temp_list)):
        x = del_temp_list[k][0]
        y = del_temp_list[k][1]
        array[x][y] = 2
   
for i in range(len(a)):
    #print(a[i])
    solution(a[i])    
    
print(min(answers)   )
    
    
        




    

    
