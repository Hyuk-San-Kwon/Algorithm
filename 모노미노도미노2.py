import copy

red = [[0 for _ in range(4)] for _ in range(4)]
blue = [[0 for _ in range(6)] for _ in range(4)]
green = [[0 for _ in range(4)] for _ in range(6)]

score = 0
N = int(input())



#블루 움직이는 함수, 레드 움직이는 함수, 점수내는 함수, 칸 움직이는 함수

#blue --> x를 보존 블루 

def move_block(color ,x ,y, ):
    if color == 0: # blue
        if y == 5 or blue[x][y+1] == 1:
            return x, y, 0
        else:
            blue[x][y+1] = 1
            blue[x][y] = 0
            return x, y + 1, 1
    
    if color == 1: #green
        if x == 5 or green[x+1][y] == 1:
            return x, y, 0
        else:
            green[x+1][y] = 1
            green[x][y] = 0
            return x + 1, y, 1
def get_block_green(t, x, y):
    
    if t == 1:
        x = 0
        green[x][y] = 1
        while not (x == 5 or green[x+1][y] == 1):
            x, y, fail = move_block(1, x, y)  
   
    
    if t == 2:
        x = 0
        y_2 = y + 1
        green[x][y] = 1
        green[x][y_2] = 1

        move_a = 0
        move_b = 0
        while True:
            if move_a == 5:
                break
            if green[move_a + 1][y] == 1:
                break
            else:
                move_a += 1
        while True:
            if move_b == 5:
                break
            if green[move_b + 1][y_2] == 1:
                break
            else:
                move_b += 1
       
        for _ in range(min(move_a, move_b)):
            x, y, fail = move_block(1, x, y)
            x = x -1
            x, y_2, fail = move_block(1, x, y_2) 
            
  
    if t == 3:
        x = 0
        green[x][y] = 1
        while not (x == 5 or green[x+1][y] == 1):
            x, y, fail = move_block(1, x, y)  
        
        x = 0
        green[x][y] = 1
        while not (x == 5 or green[x+1][y] == 1):
            x, y, fail = move_block(1, x, y)  
                          
def get_block_blue(t, x, y):
    
    if t == 1:
        y = 0
        blue[x][y] = 1
        while not (y == 5 or blue[x][y+1] == 1):
            x, y, fail = move_block(0, x, y)
    
    if t == 2:
        y = 0
        blue[x][y] = 1
        while not (y == 5 or blue[x][y+1] == 1):
            x, y, fail = move_block(0, x, y)
        
        y = 0
        blue[x][y] = 1
        while not (y == 5 or blue[x][y+1] == 1):
            x, y, fail = move_block(0, x, y)

    if t == 3:
        y = 0
        x_2 = x + 1
        blue[x][y] = 1
        blue[x_2][y] = 1
        move_a = 0
        move_b = 0
        while True:
            if move_a == 5:
                break
            if blue[x][move_a+1] == 1:
                break
            else:
                move_a += 1
        
        while True:
            if move_b == 5:
                break
            if blue[x_2][move_b+1] == 1:
                break
            else:
                move_b += 1
                
        for _ in range(min(move_a, move_b)):
            x, y, fail = move_block(0, x, y)
            y = y - 1
            x_2, y, fail = move_block(0, x_2, y) 

def move_line_block(color ,line):
    
    if color == 0: #blue
        for i in range(4):
            blue[i][line] = 0
        
        while line > 0:
            blue[0][line] = blue[0][line-1]
            blue[1][line] = blue[1][line-1]      
            blue[2][line] = blue[2][line-1]  
            blue[3][line] = blue[3][line-1] 
            blue[0][line-1], blue[1][line-1], blue[2][line-1], blue[3][line-1] = 0,0,0,0
            line -= 1
    
    if color == 1: #green
        green[line] = [0,0,0,0]
        while line > 0:
            green[line] = copy.deepcopy(green[line - 1])
            green[line - 1] = [0,0,0,0] 
            line -= 1     
def get_score():
    # blue

    score = 0
    j = 5
    
    while j >= 2:
        
        total = 0
        for i in range(0, 4):
            total += blue[i][j]
        if total == 4:
            score += 1
            move_line_block(0,j)
        else:
            j -= 1
            
    
    # green
    k = 5
    while k >= 2:
        total = 0
        total = sum(green[k])
        if total == 4:
            score += 1
            move_line_block(1, k)
        else:
            k -= 1

            
    return score
    

for _ in range(N):
    t, x, y = map(int, input().split())
    get_block_blue(t, x ,y)
    get_block_green(t, x, y)
    score += get_score()
    if sum(green[0]) and sum(green[1]):
     
        move_line_block(1, 5)
        move_line_block(1, 5)
        
    elif sum(green[1]):

        move_line_block(1, 5) 
    if sum([blue[0][0], blue[1][0], blue[2][0], blue[3][0]]) and sum([blue[0][1], blue[1][1], blue[2][1], blue[3][1]]):
        move_line_block(0, 5)
        move_line_block(0, 5)
    elif sum([blue[0][1], blue[1][1], blue[2][1], blue[3][1]]):
        move_line_block(0, 5)   
    


    
print(score)
total_block  = 0
for i in range(4):
    total_block += sum(blue[i])
for i in range(6):
    total_block += sum(green[i])

print(total_block)
