
N, M, x, y, time = map(int,(input().split()))

print(N , M  )

graph = []

for i in range(N):
    graph.append(list(map(int,(input().split()))))
    
order = list(map(int,(input().split())))

dx = [0,0, 0, -1, 1]
dy = [0,1,-1, 0,  0] #동서 북남

dice = [0,0,0,0,0,0,0]

dice_plate = 1 
list_a = [1,5,6,2]
list_b = [3,2,4,5]
list_c = [1,3,6,4]


a_pos, b_pos = 0, 0
print(graph)



for i in range((time)):
    print(x,y , order[i] , dice_plate)
     
    
    
    nx = x + dx[order[i]]
    ny = y + dy[order[i]]
    if not ((0 <= x < N) and (0 <= y < M)):
        continue
    x = nx
    y = ny # dice movement
    
    
    
print(dice)