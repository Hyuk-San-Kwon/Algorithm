n = int(input())

array = list(map(int, input().split()))
array.sort()
array.reverse()

count = 0

i = 0


while True:
    if i >= n:
        
        break
    
    i = i + array[i]
    if i <= n:
        count += 1
    else:
        i += 1
    
    
print(count)


