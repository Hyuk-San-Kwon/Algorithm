def move(home_list, up_num, left_num, M):
    K = len(home_list)
    answer_list = []
    for k in range(K):
        i = home_list[k][0]
        j = home_list[k][1]
        if i + up_num < 0 or i + up_num >= M or j + left_num < 0 or j + left_num >= M:
            continue
        else:
            answer_list.append([i + up_num, j + left_num])
            
            
    return answer_list






def solution(key, lock):
    M = len(key)
    rot1 = []
    rot2 = []
    rot3 = []
    rot4 = []
    
    for i in range(M):
        temp = []
        for j in range(M  - 1, -1, - 1):
            temp.append(key[j][i])
            
        rot1.append(temp) 
      
    for i in range(M):
        temp = []
        for j in range(M  - 1, -1, - 1):
            temp.append(rot1[j][i])
            
        rot2.append(temp)   
        
    for i in range(M):
        temp = []
        for j in range(M  - 1, -1, - 1):
            temp.append(rot2[j][i])
            
        rot3.append(temp)   
        
    for i in range(M):
        temp = []
        for j in range(M  - 1, -1, - 1):
            temp.append(rot3[j][i])
            
        rot4.append(temp)   
            
    rot = [rot1, rot2, rot3, rot4]        
    
    
    lock_list = []
    for i in range(M):
        for j in range(M):
            if lock[i][j] == 0:
                lock_list.append([i,j])
   
    for k in range(4):
        home_list = []
        for i in range(M):
            for j in range(M):
                if rot[k][i][j] == 1:
                    home_list.append([i,j])  #k 0~3
                
        print(home_list)
                
        for i in range(-M + 1, M):
            for j in range(-M+1, M):
                
                answer_list = move(home_list, i, j,M)
                if lock_list == answer_list:
                    return print(1)
                
    
    
    return print(0)


key =[[0,1,0],[1,1,0],[0,0,0]]
lock=[[1,1,1],[1,1,0],[1,0,1]]

solution(key,lock)