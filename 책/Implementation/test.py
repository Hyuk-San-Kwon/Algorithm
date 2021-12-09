M = 3

rot1= []
key =[[0,0,0],[1,0,0],[0,1,1]]
for i in range(M):
    temp = []
    for j in range(M  - 1, -1, - 1):
        temp.append(key[j][i])
            
    rot1.append(temp)

print(rot1)   