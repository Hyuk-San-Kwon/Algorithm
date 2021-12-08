n , m = map(int, input().split())

weights = list(map(int, input().split()))

weights.sort()

count = 0
j = 0
for weight in weights:
    j += 1
    for i in range(j ,n):
        if weight == weights[i]:
            continue
        else:
            count += 1
            
            
print(count)
    
    


