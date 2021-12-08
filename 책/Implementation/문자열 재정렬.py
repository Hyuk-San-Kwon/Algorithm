from collections import deque


n1 = list(map(str, input()))
n1.sort()
n = deque()
for i in range(len(n1)):
    n.append(n1[i])
num = 0
i = 0

while True:
    print(ord(n[i]))
    if ord(n[i]) <= 59 and ord(n[i]) >= 48:
        num+= int(n[i])
        n.popleft()
    else:
        break


    
    

for i in range(len(n)):
    print(n[i], end= '')
    
print(num)
