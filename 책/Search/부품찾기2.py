N = int(input())
array = set(map(int,input().split()))

m = int(input())
targets = list(map(int, input().split()))


for target in targets:
    if target in array:
        print(1)
    else:
        print(2)