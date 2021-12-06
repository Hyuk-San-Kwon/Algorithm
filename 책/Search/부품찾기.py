N = int(input())
array = list(map(int,input().split()))

m = int(input())
targets = list(map(int, input().split()))


def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    
    if array[mid] == target:
        return mid
    elif target < array[mid]:
        return binary_search(array, target, start , mid - 1)
        
    else:
        return binary_search(array, target, mid + 1, end)
'''     
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid +1 , end)
      '''      
        
array.sort()
for target in targets:
    print(binary_search(array, target, 0, len(array) - 1))
   
    
    
    
    
    
    
    