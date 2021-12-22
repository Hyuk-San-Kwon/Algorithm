import heapq

n  = int(input())

heap = []

for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)
    
print(heap[3])