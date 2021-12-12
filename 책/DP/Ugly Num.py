d = [0] * 10001

d[2] = 1
d[3] = 1
d[4] = 1
d[5] = 1

for i in range(6, 10001):
    if i % 2 == 0 and d[i // 2] == 1:
        d[i] = 1
    elif i % 3 == 0 and d[i // 3] == 1:
        d[i] = 1
    elif i % 5 == 0 and d[i // 5] == 1:
        d[i] = 1
    

for i in range(10001):
    if d[i] == 1:
        print(i, end=' ')
 
