array =  [5,7,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end:
        return
    
    pivot = start
    
    left = start + 1
    right = end
    while left <= right:
        # left는 pivot보다 큰거 선택 right는 pivot보다 작은거 선택
        while left <= end and array[left] <= array[pivot]:
            left += 1
            
        while right > start and array[right] >= array[pivot]:
            right -= 1
        
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]
    #바꾼건 원래위치
    quick_sort(array, start, right-1)
    quick_sort(array, right+1,end)
    
quick_sort(array, 0 ,len(array) -1 )
print(array)


def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]
    
    left_side = [x for x in tail if x<= pivot] # x가 pivot 보다 작은 놈들
    right_side = [x for x in tail if x > pivot] # x가 pivot 보다 큰놈들
    
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
a = [1]
b = [2]
print(a+b)

result = sorted(array)
print(array)

array.sort()
print(array)