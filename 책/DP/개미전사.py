n = int(input())

base = list(map(int, input().split()))

d = [0] * 101


for i in range(n):

    if i == 0:
        d[i] = base[0]
        continue
    if i == 1:
        d[i] = max(base[1], base[0])
        continue
    d[i] = max((d[i-2] + base[i]) , (d[i-1]))
    
    
print(max(d[i] , d[i-1]))
        
    
    

