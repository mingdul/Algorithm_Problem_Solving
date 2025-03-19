def tsp(start, current, visited, current_cost):
    global min_c, n, weight

    # 모든 도시를 방문했다면 출발 도시로 돌아가기
    if len(visited) == n:
        re = weight[current][start]
        if re > 0:  # 출발 도시로 돌아갈 수 있는 경로가 있는지 확인
            min_c = min(min_c, current_cost + re)
        return

    # 현재 도시에서 갈 수 있는 다른 도시 탐색
    for w in range(n):
        if w not in visited and weight[current][w] > 0:
            visited.add(w)
            tsp(start, w, visited, current_cost + weight[current][w])
            visited.remove(w)

def solve_tsp():
    global min_c, n, weight
    for start in range(n):
        visited = set([start])
        tsp(start, start, visited, 0)

# 입력 받기
n = int(input())
weight = [list(map(int, input().split())) for _ in range(n)]

min_c = float('inf')
solve_tsp()

print(min_c)
