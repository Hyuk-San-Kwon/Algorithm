n = int(input())

for i in range(n):
    N , M = map(int, input().split())
    array = list(map(int, input().split()))
    
    dp = []
    index = 0
    for i in range(N):
        dp.append(array[index:index + M])
        index += M
        
    for j in range(1, M):
        for i in range(N):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            if i == n - 1:
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
            
    result = 0
    for i in range(N):
        result = max(result, dp[i][M-1])    
        
                 
    



gold_mount = [[] for _ in range(n)]