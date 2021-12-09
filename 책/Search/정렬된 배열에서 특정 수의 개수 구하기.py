N ,x  = map(int,(input().split()))


num = list(map(int, input().split()))

first = 0
start = len(num) // 2
end = len(num) - 1

two_start = -1
two_end = len(num) - 1

if x not in num:
    print(-1)
else:
    while start != 0:
        
        if num[start] == x and num[start] > num[start- 1]:
            two_start = start - 1
            break
        if first == end:
            break
        elif num[start] == x and num[start - 1] == x:
            end = start - 1
            start = (first + end) // 2
            
        elif num[start] < x:
            first = start + 1
            start = (first + end) // 2
            
        elif num[start] > x:
            end = start - 1
            start = (first + end) // 2
            
    first = 0
    start = len(num) // 2
    end = len(num) - 1       
    while start != len(num) - 1:
        #print(first, end)
        if num[start] == x and num[start] < num[start + 1]:
            two_end = start
            print(two_end)
            break
        if first == end:
            break
        elif num[start] == x and num[start + 1] == x:
            first = start + 1
            start = (first + end) // 2
            
        elif num[start] > x:
            end = start - 1
            start = (first + end) // 2
            
        elif num[start] < x:
            first = start + 1
            start = (first + end) // 2
            
            
print(two_end , two_start)            
        
        