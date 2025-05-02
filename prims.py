# import heapq
# from collections import defaultdict
# def prim(graph, start):
#     mst = []
#     visited = set([start])
#     edges = [(cost, start, to) for to, cost in graph[start]]
#     heapq.heapify(edges)

#     while edges:
#         cost, frm, to = heapq.heappop(edges)
#         if to not in visited:
#             visited.add(to)
#             mst.append((frm, to, cost))
#             for neighbor, weight in graph[to]:
#                 if neighbor not in visited:
#                     heapq.heappush(edges, (weight, to, neighbor))
#     return mst
# graph = {
#     'A': [('B', 2), ('C', 3)],
#     'B': [('A', 2), ('C', 1), ('D', 1)],
#     'C': [('A', 3), ('B', 1), ('D', 4)],
#     'D': [('B', 1), ('C', 4)]
# }
# mst = prim(graph, 'A')
# for frm, to, cost in mst:
#     print(f"{frm} - {to}: {cost}")

graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 1)],
    'C': [('A', 3), ('B', 1), ('D', 4)],
    'D': [('B', 1), ('C', 4)]
}
 
def prim(graph, start):
    visited = []
    edges = []
    total_cost = 0
 
    visited.append(start)
 
    while len(visited) < len(graph):
        min_edge = None
        min_weight = float('inf')
 
        for node in visited:
            for neighbour, weight in graph[node]:
                if neighbour not in visited and weight < min_weight:
                    min_edge = (node, neighbour)
                    min_weight = weight
        
        if min_edge:
            print(f"Edge selected: {min_edge[0]} - {min_edge[1]} with weight {min_weight}")
            visited.append(min_edge[1])
            total_cost += min_weight
 
    print("Total Minimum Cost:", total_cost)
 
prim(graph, 'A')