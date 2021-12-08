array = list(map(int, input()))


count1 = 0   # 1 ->0
count2 = 0   # 0 ->1

start = array[0]

for i in range(len(array)):
    
    if i == (len(array)) - 1 and start != array[i]:
        count1 += 1
        count2 += 1
        break
    
    elif start == 1 and start == array[i]:
        continue
    elif start == 1  and start != array[i]:
        count1 += 1
        start = 0
        continue
    elif start == 0 and start == array[i]:
        continue
    elif start == 0  and start != array[i]:
        count2 += 1
        start = 1
        continue
if count1 == 0 or count2 == 0:
    print(max(count1, count2))
else:
    print(min(count1, count2))