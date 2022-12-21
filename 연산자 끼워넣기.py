from itertools import permutations

N = int(input())

numbers = list(map(int , input().split()))


ops = list(map(int,  input().split()))
ops_list = []

for i in range(4):
    if i == 0:
        for j in range(ops[i]):
            ops_list.append('+')
    
    if i == 1:
        for j in range(ops[i]):
            ops_list.append('-')
            
    if i == 2:
        for j in range(ops[i]):
            ops_list.append('*')
            
    if i == 3:
        for j in range(ops[i]):
            ops_list.append('/')

ops_order = list(permutations(ops_list, N-1)    )
answer = []
for ops in (ops_order):
    sum = numbers[0]
    for i in range(len(ops)):

        if ops[i] == '+':
            sum = sum + numbers[i+1]
        if ops[i] == '-':
            sum = sum - numbers[i+1]
        if ops[i] == '*':
            sum = sum * numbers[i+1]
        if ops[i] == '/':
            if sum < 0:
                temp = (-sum) // numbers[i+1]
                sum = - temp
            else:
                sum = sum // numbers[i+1]

    answer.append(sum)
    


print(max(answer))
print(min(answer))
