
# class DisjointSet:
#     def __init__(self, vertices):
#         self.parent = {v: v for v in vertices}

#     def find(self, v):
#         if self.parent[v] != v:
#             self.parent[v] = self.find(self.parent[v])  # Path compression
#         return self.parent[v]

#     def union(self, u, v):
#         root_u = self.find(u)
#         root_v = self.find(v)
#         if root_u != root_v:
#             self.parent[root_v] = root_u
#             return True
#         return False

# def kruskal(vertices, edges):
#     ds = DisjointSet(vertices)
#     mst = []

#     edges.sort(key=lambda x: x[2])
#     for u, v, weight in edges:
#         if ds.union(u, v):
#             mst.append((u, v, weight))
#     return mst

# vertices = ['A', 'B', 'C', 'D']
# edges = [
#     ('A', 'B', 2),
#     ('A', 'C', 3),
#     ('B', 'C', 1),
#     ('B', 'D', 1),
#     ('C', 'D', 4)
# ]
# mst = kruskal(vertices, edges)
# for u, v, weight in mst:
#     print(f"{u} - {v}: {weight}")






edges = [
    (2, 'A', 'B'),
    (3, 'A', 'C'),
    (1, 'B', 'C'),
    (1, 'B', 'D'),
    (4, 'C', 'D')
]
 
parent = {}
 
def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]
 
def union(u, v):
    parent[find(u)] = find(v)
 
def kruskal(edges):
    for node in ['A', 'B', 'C', 'D']:
        parent[node] = node
 
    edges.sort()
    total_cost = 0
 
    for weight, u, v in edges:
        if find(u) != find(v):
            print(f"Edge selected: {u} - {v} with weight {weight}")
            union(u, v)
            total_cost += weight
 
    print("Total Minimum Cost:", total_cost)
 
kruskal(edges)