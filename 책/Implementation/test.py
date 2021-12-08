line = str(input())
length = len(line)
print(line[0])

for i in range(1, length // 2 + 1):
    j = 0
    sorted_list = []
    while j < length:
        if j + i < length:
            k = ''.join(line[j :j + i])
            print(k)
            sorted_list.append(((k)))
        else:
            k = ''.join(line[j :])
            sorted_list.append((k))
        j += i
        
    print(sorted_list)    

            
            
    