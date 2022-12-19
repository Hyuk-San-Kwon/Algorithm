
test_num = int(input())

test_list = [] #시험장 리스트

test_list = (list(map(int, input().split())))

temp = list(map(int , (input().split())))
a, b = temp[0], temp[1]

answer = 0

for i in range(len(test_list)):
    test_list[i] -= a
    answer += 1
    if test_list[i] <= 0:
        continue
    if test_list[i] <= b:
        answer+= 1
        continue
    temp = test_list[i] // b
    answer += temp
    if test_list[i] % b != 0:
        answer += 1

print(int(answer))
        

