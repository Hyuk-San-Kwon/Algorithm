from collections import deque


array = [[] for _ in range(300001)]
visited = [0] * 300001
N, M, K, X = map(int, input().split())
for i in range(M):
    src, des = map(int, input().split())
    array[src].append(des)
    
def bfs(src, K,N):
    queue = deque()
    queue.append(src)
    
    
    while queue:
        v = queue.popleft()
        
        for des in (array[v]):
            #print(array[v])
            
            #print(visited[des])
            if visited[des] == 0:
                queue.append(des)
                print(des)
                visited[des] += visited[v] + 1
                print(visited[des])
            else:
                continue
       
    print(visited[1],visited[2],visited[3],visited[4])   
                
    for i in range(N + 1):
        if visited[i] == K:
            print(N, end=' ') 
    
    
                     
    
bfs(X,K,N)