N, M  = map(int , input().split())
answer = []
graph = []
for i in range(N):
   graph.append(list(map(int, input().split())))
   
   
# case3

for i in range(N):
    for j in range(M):
        sum = 0
        success = 1
        for k in range(4):
            x, y = i, j #세로 부터
            y += k 
            if x < 0 or y < 0 or x >= N or y >= M:
                success = 0
                break
            sum += graph[x][y]
        if success == 1:
            answer.append(sum)
        sum = 0
        success = 1
        for k in range(4):
            x, y = i, j #가로 부터
            x += k 
            if x < 0 or y < 0 or x >= N or y >= M:
                success = 0
                break
            sum += graph[x][y]
        if success == 1:
            answer.append(sum)

        sum = 0
        success = 1
        for k in range(4):
            
            x, y = i, j 
            if k == 1:
                y += 1
            elif k == 2:
              
                x += 1
            elif k == 3:
                x += 1
                y += 1
            
            if x < 0 or y < 0 or x >= N or y >= M:
                success = 0
                break
            sum += graph[x][y]
        if success == 1:
            answer.append(sum)

        sum = 0
        success = 1
        for k in range(4):
            
            x, y = i, j 
            if k == 1:
                x += 1
            elif k == 2:
              
                x += 2
            elif k == 3:
                x += 2
                y += 1
            
            if x < 0 or y < 0 or x >= N or y >= M:
                success = 0
                break
            sum += graph[x][y]
        if success == 1:
            answer.append(sum)
        
        sum = 0
        success = 1
        for k in range(4):
            x, y = i, j #ㄱ반대
            if k == 3:
                x += 1
            else:
                y  += k
            if x < 0 or y < 0 or x >= N or y >= M:
                success = 0
                break
            sum += graph[x][y]
        if success == 1:
            answer.append(sum)

        sum = 0
        success = 1
        for k in range(4):
            x, y = i, j #ㄱ
            
            
            if k >= 1:
                y += 1
                x += k - 1
            
            
            if x < 0 or y < 0 or x >= N or y >= M:
                success = 0
                break
            sum += graph[x][y]
        if success == 1:
            answer.append(sum)
        
        sum = 0
        success = 1
        for k in range(4):
            x, y = i, j #ㄱ
            
            if k <= 2:
                y += k
            elif k == 3:
                x -= 1
                y += 2
            
            if x < 0 or y < 0 or x >= N or y >= M:
                success = 0
                break
            sum += graph[x][y]
        if success == 1:
            answer.append(sum)

        
        sum = 0
        success = 1
        for k in range(4):
            
            x, y = i, j 
            if k == 1:
                y += 1
            elif k == 2:
                x -= 1
                y += 1
            elif k == 3:
                x -= 2
                y += 1
            
            if x < 0 or y < 0 or x >= N or y >= M:
                success = 0
                break
            sum += graph[x][y]
        if success == 1:
            answer.append(sum)
        
        sum = 0
        success = 1
        for k in range(4):
            
            x, y = i, j 
            if k == 1:
                y += 1
            elif k == 2:
              
                y += 2
            elif k == 3:
                x += 1
                y += 2
            
            if x < 0 or y < 0 or x >= N or y >= M:
                success = 0
                break
            sum += graph[x][y]
        if success == 1:
            answer.append(sum)
        
        sum = 0
        success = 1
        for k in range(4):
            
            x, y = i, j 
            if k == 1:
                y += 1
            elif k == 2:
                x += 1
        
            elif k == 3:
                x += 2
             
            
            if x < 0 or y < 0 or x >= N or y >= M:
                success = 0
                break
            sum += graph[x][y]
        if success == 1:
            answer.append(sum)
        
        
        sum = 0
        success = 1
        for k in range(4):
            
            x, y = i, j 
            if k == 1:
                x += 1
            elif k == 2:
                x += 1
                y += 1
            elif k == 3:
                x += 1
                y += 2
            
            if x < 0 or y < 0 or x >= N or y >= M:
                success = 0
                break
            sum += graph[x][y]
        if success == 1:
            answer.append(sum)
            
        
        sum = 0
        success = 1
        for k in range(4):
            
            x, y = i, j 
            if k == 1:
                x += 1
            elif k == 2:
                x += 1
                y += 1
            elif k == 3:
                x += 2
                y += 1
            
            if x < 0 or y < 0 or x >= N or y >= M:
                success = 0
                break
            sum += graph[x][y]
        if success == 1:
            answer.append(sum)
        
        sum = 0
        success = 1
        for k in range(4):
            x, y = i, j
            if k == 1:
                y += 1
            elif k == 2:
                x -= 1
                y += 1
            elif k == 3:
                x -= 1
                y += 2
            
            if x < 0 or y < 0 or x >= N or y >= M:
                success = 0
                break
            sum += graph[x][y]
        if success == 1:
            answer.append(sum)
        
        sum = 0
        success = 1
        for k in range(4):
            x, y = i, j
            if k == 1:
                y += 1
            elif k == 2:
                x += 1
                y += 1
            elif k == 3:
                x += 1
                y += 2
            
            if x < 0 or y < 0 or x >= N or y >= M:
                success = 0
                break
            sum += graph[x][y]
        if success == 1:
            answer.append(sum)
        
        sum = 0
        success = 1
        for k in range(4):
            
            x, y = i, j 
            if k == 1:
                x += 1
            elif k == 2:
                x += 1
                y -= 1
            elif k == 3:
                x += 2
                y -= 1
            
            if x < 0 or y < 0 or x >= N or y >= M:
                success = 0
                break
            sum += graph[x][y]
        if success == 1:
            answer.append(sum)
        
        sum = 0
        success = 1
        for k in range(4): #ㅜ
            
            x, y = i, j 
            if k == 1:
                y += 1
            elif k == 2:
                x += 1
                y += 1
            elif k == 3:
                y += 2
                
            
            if x < 0 or y < 0 or x >= N or y >= M:
                success = 0
                break
            sum += graph[x][y]
        if success == 1:
            answer.append(sum)
        
        sum = 0
        success = 1
        for k in range(4): # ㅓ
            x, y = i, j
            if k == 1:
                x += 1
            elif k == 2:
                x += 1
                y -= 1
            elif k == 3:
                x += 2
                
            
            if x < 0 or y < 0 or x >= N or y >= M:
                success = 0
                break
            sum += graph[x][y]
        if success == 1:
            answer.append(sum)
        
        sum = 0
        success = 1
        for k in range(4): # ㅗ
            
            x, y = i, j 
            if k == 1:
                y += 1
            elif k == 2:
                x -= 1
                y += 1
            elif k == 3:
                y += 2
                
            
            if x < 0 or y < 0 or x >= N or y >= M:
                success = 0
                break
            sum += graph[x][y]
        if success == 1:
            answer.append(sum)
        
        sum = 0
        success = 1
        for k in range(4): # ㅏ
            x, y = i, j
            if k == 1:
                x += 1
            elif k == 2:
                x += 1
                y += 1
            elif k == 3:
                x += 2
                
            
            if x < 0 or y < 0 or x >= N or y >= M:
                success = 0
                break
            sum += graph[x][y]
        if success == 1:            
            answer.append(sum)

        
      
print(max(answer))