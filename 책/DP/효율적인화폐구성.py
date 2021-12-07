n, m = map(int, input().split())

money_list = []

for i in range(n):
    money_list.append(int(input())) 
    
d = [10001] * 10001

for i in range(1 , m + 1):
    for j in range(n):
        money = money_list[j]
        if i == money:
            d[i] = 1
            continue
        elif money == money_list[0] and i % money == 0:
            d[i] = i // money
            continue
        d[i] = min(d[i], d[i-money] + 1)
        
        
        
print(d[m])
             
    
    
    