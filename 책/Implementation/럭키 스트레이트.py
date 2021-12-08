num = list(map(int,(input())))
print(num)
front_num = len(num) // 2
end_num = len(num)
print(front_num, end_num)
front = 0
end = 0

for i in range(front_num):
    front += num[i]
    
for i in range(front_num, end_num):
    end += num[i]
    
if front == end:
    print('LUCKY')
else:
    print('READY')
    
      