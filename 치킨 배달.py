from itertools import combinations

N, M = map(int , (input().split()))

graph = []

for i in range(N):
    graph.append(list(map (int, input().split())))
    
home_list  = []
chick_list = []    

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            home_list.append((i,j))
        if graph[i][j] == 2:
            chick_list.append((i,j))
            
            
answer = []

chosen_chick = combinations(chick_list, M)

for temp_chick in chosen_chick:
    distance = 0

    temp_dis = [10e9 for _  in range(len(home_list))]
    for i in range(len(temp_chick)):
        for j in range(len(home_list)):
           
            distance = abs(  temp_chick[i][0] - home_list[j][0] ) + abs(  temp_chick[i][1] - home_list[j][1] )
            if distance < temp_dis[j]:
                temp_dis[j] = distance
                
            
    
    answer.append(sum(temp_dis)) 
        
print(min(answer))
            
            
