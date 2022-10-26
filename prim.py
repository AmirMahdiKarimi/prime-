import sys


def prim(edges, visited_vertices, n):
    mst = {i: [] for i in range(n)}
    for i in range(n - 1):
        min_edge = sys.maxsize
        vertex1 = 0
        vertex2 = 0
        for ver in visited_vertices:
            for edge in edges[ver]:
                if edge[0] not in visited_vertices:
                    if edge[1] < min_edge:
                        vertex1 = ver
                        vertex2 = edge[0]
                        min_edge = edge[1]
        visited_vertices.append(vertex2)
        mst[vertex1].append((vertex2, min_edge))
        mst[vertex2].append((vertex1, min_edge))
    return mst


print("Enter the number of vertices : ")
n = int(input())
print("Enter the number of edges : ")
e = int(input())
print(f"Notic: The name of vertices is 0 to {n - 1}.")
print("Enter edges like this format : first vertex-second vertex-weight edges\nsample : 0-4-17 ")
edges = {i: [] for i in range(n)}
for i in range(e):
    edge = input().split("-")
    edges[(int(edge[0]))].append((int(edge[1]), int(edge[2])))
    edges[(int(edge[1]))].append((int(edge[0]), int(edge[2])))
visited_vertices = [0]

res_mst = prim(edges, visited_vertices, n)
cost = 0
for i in res_mst.values():
    for j in i:
        cost += j[1]

print("This is linked list of mst (key is first vertex and first value is second veertex and second value is weight edge):")
print(res_mst)
print(f"Cost of mst is: {int(cost / 2)}")
