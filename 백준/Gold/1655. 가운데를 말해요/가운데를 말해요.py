import heapq
import sys
input = sys.stdin.readline

n = int(input())
max_heap = []  # 최대 힙
min_heap = []  # 최소 힙

for _ in range(n):
    num = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -num)  # 최대 힙은 음수로 저장하여 최대값이 최상단에 오도록 함
    else:
        heapq.heappush(min_heap, num)

    # 최대 힙의 최대값이 최소 힙의 최소값보다 큰 경우, 두 힙의 최상단 요소를 교환
    if min_heap and -max_heap[0] > min_heap[0]:
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
        heapq.heappush(min_heap, -heapq.heappop(max_heap))

    # 최대 힙의 최상단 요소는 항상 전체 요소 중 중간값 (또는 중간값보다 작은 최대값)
    print(-max_heap[0])
