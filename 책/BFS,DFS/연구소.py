from itertools import combinations, permutations
import copy
from collections import deque

global N
global M

N, M = map(int, input().split())



array = []

for i in range(N):
    a = list(map(int, input().split()))
    array.append(a)

zero_listed = []
one_listed = []
two_listed = []
count = 0
for i in range(N):
    for j in range(M):
        if array[i][j] == 2:
            two_listed.append((i,j))
            count += 1
        elif array[i][j] == 1:
            one_listed.append((i,j))
            count += 1
        else:
            zero_listed.append((i,j))

zero_count = N * M - count

dx = [-1, 1, 0, 0]
dy = [ 0, 0, -1,1]        
        

def bfs(test_array, two_list, zero_count):
    queue = deque()
    zero_count_temp = zero_count
    for i in range(len(two_list)):
        queue.append(two_list[i])
    while queue:
        x ,y = queue.popleft()
        #print(x, y)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if test_array[nx][ny] == 0:
                queue.append((nx, ny))
                zero_count_temp -= 1
                test_array[nx][ny] = 2
                #print(queue)
    return zero_count_temp           
    
    
def solve():
    answers = []
    nPzero_listed = list(combinations(zero_listed ,3))
    for i in range(len(nPzero_listed)):
        zero = nPzero_listed[i]
        zero0 = zero[0]
        zero1 = zero[1]
        zero2 = zero[2]
        zero_count_temp = zero_count - 3
        if zero_count_temp <= 0:
            zero_count_temp = 0
        test_array = copy.deepcopy(array)
        test_array[zero0[0]][zero0[1]] = 1
        test_array[zero1[0]][zero1[1]] = 1
        test_array[zero2[0]][zero2[1]] = 1
        zero_count_temp = bfs(test_array,two_listed, zero_count_temp)
        answers.append(zero_count_temp)
        
    
    
    print(max(answers))
        
        
solve()       
        
        