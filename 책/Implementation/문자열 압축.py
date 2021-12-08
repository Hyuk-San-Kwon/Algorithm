def solution():
    line = str(input())
    length = len(line)
    answer_list = []
    for i in range(1, length // 2 + 1):
        j = 0
        answer = 0
        sum = 0
        sorted_list = []
        while j < length:
            if j + i < length:
                k = ''.join(line[j :j + i])

                sorted_list.append(((k)))
            else:
                k = ''.join(line[j :])
                sorted_list.append((k))
            j += i
        
        for k in range(len(sorted_list)):  #마지막 루프 고려
            if k == len(sorted_list) - 1:
                if sum > 0:
                    answer += i + 1
                    print(answer)
                    break
                else:
                    answer += len(sorted_list[-1])
                    print(answer)
                    break
            if sorted_list[k] == sorted_list[k + 1]:
                sum += 1
                continue
            if sum > 0:
                answer += i + 1
                print(answer)
                sum = 0

            else:
                answer += i
                sum = 0

                
        answer_list.append(answer)
    print(answer_list)        
        
        
    
    answer = min(answer_list)
    return answer


answer = solution()
print(answer)