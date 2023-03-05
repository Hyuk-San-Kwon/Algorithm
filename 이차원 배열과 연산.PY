r, c, k = map(int, input().split())  # A[r+][c+]
r = r - 1
c = c - 1

t = 100
time = -1
graph = [[0 for _ in range(t)] for _ in range(t)]
 # 숫자가 행열안에 몇개 있는지 count

row = 3
column = 3 

for i in range(3):
    a, b, d = map(int, input().split())
    graph[i][0], graph[i][1], graph[i][2] = a, b, d
    
def R_change(max_row):
    max_column = 0
    length = max_row
   
        
    for i in range(length):
        max_count = 0
        count = [1000 for _ in range(101)]
        for j in range(100):
            if graph[i][j] != 0:
                if count[graph[i][j]] == 1000:
                    count[graph[i][j]] = 1
                else:
                    count[graph[i][j]] += 1
                max_count = max(max_count, graph[i][j])
           

        j = 1
        for j in range(1, 101):
            min_num = min(count)
            if min_num == 1000:
                
                for k in range(2*j - 2, 100):
                    graph[i][k] = 0
                break
            small_num_pos = count.index(min_num)
            graph[i][2*j-2], graph[i][2*j - 1] = small_num_pos, min_num
            count[small_num_pos] = 1000
            max_column = max(max_column,2*j)

        
        
    return max_column


while True:
    time += 1

 
    
    if graph[r][c] == k:
        print(time)
        break
    if time == 100:
        print(-1)
        break
    if row >= column:
        column = R_change(row)
    else:
        graph_2 = [[0 for _ in range(t)] for _ in range(t)]
        for i in range(t):
            for j in range(t):
                graph_2[j][i] = graph[i][j]
        
        graph = graph_2
        
        row = R_change(column)
        
      
        graph_2 = [[0 for _ in range(t)] for _ in range(t)]
        for i in range(t):
            for j in range(t):
                graph_2[i][j] = graph[j][i]
        graph = graph_2
                
    

        
    

