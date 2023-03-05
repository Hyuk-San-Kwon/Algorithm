import sys

input = sys.stdin.readline
dice = list(map(int,input().split()))

board = [0]*100
for i in range(21):
    board[i] = i*2


board[31],board[32],board[33] = 13,16,19
board[34],board[35],board[36],board[37] = 25,30,35,40

board[51],board[52], = 22,24,
board[53],board[54],board[55],board[56] = 25,30,35,40

board[71],board[72],board[73] = 28,27,26
board[74],board[75],board[76],board[77] = 25,30,35,40

most=0

horse = [0]*4


def move(start,dist):
    if start == 5 : start = 30
    elif start == 10 : start = 50
    elif start == 15 : start = 70

    return start+dist


def dfs(index,sum):
    global most

    if index == 10:
        most = max(sum,most)
        return

    for i in range(4):
        if horse[i] < 0: continue           # reached the end

        nxt = move(horse[i],dice[index])
       
        if board[nxt] == 25:
            nxt = 34
        if board[nxt] == 30 and nxt != 15:
            nxt = 35
        if board[nxt] == 35:
            nxt = 36
        if board[nxt] == 40:
            nxt = 37
        if nxt in horse: 
            continue           # 도착지점에 이미 존

        tmp = horse[i]

        if board[nxt] == 0:                 # 도착지점 도착시 -1
            horse[i] = -1
        else:
            horse[i] = nxt
     
        check = horse[:]
      
        dfs(index+1,sum+board[nxt])
        horse[i] = tmp

dfs(0,0)
print(most)