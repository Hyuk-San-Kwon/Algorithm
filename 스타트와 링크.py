from itertools import combinations, permutations
N = int(input())

start = []
link = []

graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))
    
team = [i for i in range(N)]


team_list = list(combinations(team , N//2))

team = (combinations(team_list ,2))

team_final = []


for temp in (team):
    not_in = 1
    for j in range(N // 2):
        if temp[0][j] in temp[1]:
            not_in = 0
            continue
    if not_in == 1:
        team_final.append(temp)
  
       

answer = []
for i in range(len(team_final)):
    start_score = 0
    link_score = 0
  
    start_list = list(permutations(team_final[i][0],2))
    link_list = list(permutations(team_final[i][1],2))
      
    for j in range(len(start_list)):
        start_score += graph[start_list[j][0]][start_list[j][1]]
        link_score += graph[link_list[j][0]][link_list[j][1]]
    answer.append(abs(start_score - link_score))

print(min(answer))
    
    
    