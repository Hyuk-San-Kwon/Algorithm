from itertools import combinations,permutations
N = int(input())

start = []
link = []

graph = []

for i in range(N):
    graph.append(list(map(int, input().split())))


team = [i+1 for i in range(N-1)]

first = combinations(team, N // 2 - 1)
answer = []
for temp in first:
    temp = list(temp)
    link_list = [x for x in team if x not in temp]

    
    temp.insert(0,0)
    temp_start = permutations(temp,2)
    temp_link = permutations(link_list , 2)
    start_score = 0
    link_score = 0
    for start in temp_start:
        start_score += graph[start[0]][start[1]]
    for link in temp_link:
        link_score += graph[link[0]][link[1]]
        
    answer.append(abs(start_score - link_score))
    
print(min(answer))
        
    
    
    