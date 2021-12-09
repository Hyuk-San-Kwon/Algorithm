



def solution(N ,stages):
    
    temp = []
    max_stage = max(stages)
    
    
    for i in range(1, max_stage):
        temp.append([i, 0, 0])
    
    for i in range(len(stages)):
        stage_num = stages[i]
        for j in range(stage_num- 1):
            temp[j][1] += 1
        for j in range(stage_num):
            if j == max_stage - 1:
                continue
            temp[j][2] += 1
    answers = []
    print(temp)
    for i in range(max_stage - 1):
        
        answers.append([i+1, (temp[i][2] - temp[i][1]) / temp[i][2] ])
    print(answers)
    
    answers.sort(key= lambda x: -(x[1]))
    print(answers)
    answer = []
    for i in range(max_stage - 1):
        answer.append(answers[i][0])
        
    return print(answer)
            
    
 


N = 4
stages = [4,4,4,4,4]   

solution(N,stages) 