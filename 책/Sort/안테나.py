N = int(input())

home_pos = list(map(int, input().split()))

home_pos.sort()
start = len(home_pos) // 2
length = len(home_pos)

def search_pos(start, length):
    distance = 0
    
    for i in range(length):
        distance += abs(home_pos[i] - home_pos[start])
    


