n = int(input())


d = [0] * 1001


for i in range(1, n + 1):
    if i == 1:
        d[i] = 1
        continue
    if i == 2:
        d[i] = 3
        continue
    d[i] = d[i-1] + 2 * d[i - 2]
    
print(d[n])

