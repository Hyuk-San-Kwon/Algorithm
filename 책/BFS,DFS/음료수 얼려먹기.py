n , m = map(int, input().split())


array = []
for i in range(n):
    array.append(list(map(int, input())))
    
def dfs(x,y):
    if x < 0 or y < 0 or x >= n or y >=m:
        return False
    
    elif array[x][y] == 0:
        array[x][y] = 1
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
        return True
    
    return False
    
    
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
            
print(array)
print(result)