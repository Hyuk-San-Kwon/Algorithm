array = list(map(int, input()))

answer = 0

for i in range(len(array)):
    
    if answer == 0:
        answer += array[i]
    
    elif array[i] == 0 or array[i] == 1:
        answer += array[i] + 1
    
    else:
        answer *= array[i]

print(answer)