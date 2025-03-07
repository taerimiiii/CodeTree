def get_adjacency_matrix(m) :
    for i in range(m) :
        x, y = edges[i]
        matrix[x][y] = 1
        matrix[y][x] = 1

def dfs(vertex) :
    global vertex_cnt, n
    for curr_vet in range(1, n + 1) :
        if matrix[vertex][curr_vet] and not visited[curr_vet] :
            vertex_cnt += 1
            visited[curr_vet] = True
            dfs(curr_vet)

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]

matrix = [[0] * (n + 1) for _ in range(n + 1)]
get_adjacency_matrix(m)

visited = [False] * (n + 1)
visited[1] = True
vertex = 1

vertex_cnt = 0
dfs(vertex)

print(vertex_cnt)

'''
for i in range(n + 1) :
    for j in range(n + 1) :
        print(matrix[i][j], end = ' ')
    print()
'''