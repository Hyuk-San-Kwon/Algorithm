n , m =map(int,input().split())

result = 0
answer = []

for i in range(n):
    data = list(map(int, input().split()))
    
    answer.append(min(data))
    
print(max(answer))
    
    