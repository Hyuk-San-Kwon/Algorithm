N = int(input())


d = [0] * 13
answers = [0] * 13
soldiers = list(map(int, input().split()))
soldiers.insert(0,0)
soldiers.append(0)
print(soldiers)

force = 0
length = len(soldiers)


for i in range(length):
    if i ==  length - 1:
        break
    if soldiers[i+ 1] < soldiers[i]:
        d[i + 1] += d[i] + soldiers[i + 1]
        answers[i + 1] = answers[i]
    else:
        force = 0
        temp_count = 0
        pos = 0
        for j in range(1, i + 1):
            if soldiers[i + 1] > soldiers[i - j + 1]:
                force += soldiers[i - j + 1]
                temp_count += 1
                pos = i - j + 1
            
        
        if force > soldiers[i + 1]:
            d[i + 1] = d[i]

            answers[i+1] = answers[i] + 1
        else:
            d[i + 1] = d[pos -1] + soldiers[i+1]
            answers[i + 1] = answers[pos - 1] + temp_count

        
print( answers)






