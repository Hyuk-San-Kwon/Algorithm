N, M = map(int, input().split())  #N은 떡 갯수, M은 원하는 길이
lengths = list(map(int, input().split()))

lengths.sort()

start = lengths[N - 1] // 2

while True:
    n = M
    sum = 0
    count = 0
    for length in lengths:
        
        if length <= start:
            count += 1
            continue
        sum += length - start
        n = N - count

    if sum == M:
        print(start, sum)
        break
      
    elif sum > M:
        if sum > M + n:
            print(start, sum)
            start = (start + lengths[N - 1]) // 2
            
            continue
        
        elif sum == M + n:
            print(start + 1, ' 끝')
            break
    
        else:
            print(start, sum, 1, n)
            break
    else:   
        print(start, sum)
        start = (start) // 2
        