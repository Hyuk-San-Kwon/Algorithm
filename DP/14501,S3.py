days = int(input())

date = [99999] * 10000
money = [0] * 10000

answer = [0] * (days + 10)

for i in range(days):
    data = list(map(int, input().split()))
    date[i + 1] = data[0]
    money[i + 1] = data[1]

for today in range(days, 0, -1):
    end_date = today + date[today] - 1

    if end_date <= days:
        answer[today] = max(answer[today + 1] ,answer[today + date[today]] + money[today])
    else:
        answer[today] = answer[today + 1]

print(answer)