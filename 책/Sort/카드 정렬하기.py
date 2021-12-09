
n = int(input())

array = []
for i in range(n):
    array.append(int(input()))
    
count = 0


while True:
    
    array.sort()
    print(count)
    if len(array) == 1:
        break
    if len(array) == 2:
        array.insert(0, array[0] + array[1])
        count += array[1] + array[2]
        break
    if array[0] > array[1]:
        array.insert(3,array[1] + array[2])
        del array[1], array[2]
        continue
    else:
        array.insert(0, array[0] + array[1])
        del array[1]
        del array[1]
        count += array[0]

        
    
print(count)

