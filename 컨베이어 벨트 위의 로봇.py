
from shutil import move


N, K = map(int, input().split())

belt = [[0 for _  in range(N)] for _ in range(2)]
armor = [[0 for _  in range(N)] for _ in range(2)]

armor_list = list(map(int, input().split()))

armor[0] = armor_list[:N]
armor[1] = list(reversed(armor_list[N:]))

def move_belt():
    temp_0 = belt[0][N - 1]
    temp_1 = belt[1][0]
    armor_temp_0 = armor[0][N - 1]
    armor_temp_1 = armor[1][0]
    i = N - 1
    while True:
        i -= 1
        belt[0][i + 1] = belt[0][i]
        armor[0][i + 1] = armor[0][i]
        if i == 0:
            break
    belt[0][0] = temp_1
    armor[0][0] = armor_temp_1
    
    i = 0
    while True:
        i += 1
        belt[1][i-1] = belt[1][i]
        armor[1][i-1] = armor[1][i]
        if i == N-1:
            break
    belt[1][N-1] = temp_0
    armor[1][N-1] = armor_temp_0

def get_robot():
    if armor[0][0] != 0:
        armor[0][0] -= 1
        belt[0][0] += 1
def exit():
    
    sum_zero = 0
    for i in range(N):
        if armor[0][i] == 0:
            sum_zero += 1
        if armor[1][i] == 0:
            sum_zero += 1
            
    return sum_zero
def move_robot():
    
    i = N - 2
    while True:
        if belt[0][i]:
            if armor[0][i+1] != 0 and belt[0][i+1] == 0:
                armor[0][i+1] -= 1
                belt[0][i] -= 1
                belt[0][i+1] += 1
        i -= 1
        if i == -1:
            break
def get_off_robot():
    if belt[0][N-1]:
        belt[0][N-1] -= 1    

time = 0

while True:
    move_belt()
    get_off_robot()
    move_robot()
    get_off_robot()
    get_robot()
    sum_zero = exit()
    time += 1

    
    if sum_zero >= K:
        break
   
    
    
print(time)


