def is_safe(v, graph, color, c):
    
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True
def graph_coloring_util(graph, m, color, v):  
    num_vertices = len(graph)   
    if v == num_vertices:
        print("Solution exists with colors:", color)
        return True
    
    for c in range(1, m + 1):  
        if is_safe(v, graph, color, c):
            color[v] = c
            if graph_coloring_util(graph, m, color, v + 1):
                return True           
            color[v] = 0  
    return False
def solve_graph_coloring(graph, m):
    
    num_vertices = len(graph)
    color = [0] * num_vertices  
    if not graph_coloring_util(graph, m, color, 0):
        print("Solution does not exist with", m, "colors.")

if __name__ == "__main__":
    
    graph1 = [
        [0, 1, 1, 1],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [1, 1, 1, 0]
    ]
    max_colors1 = 3
    print(f"Graph 1 with {max_colors1} colors:")
    solve_graph_coloring(graph1, max_colors1)
    print("\n" + "="*30 + "\n") 
    graph2 = [
        [0, 1, 0, 1],
        [1, 0, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 1, 0]
    ]
    max_colors2 = 2
    print(f"Graph 2 with {max_colors2} colors:")
    solve_graph_coloring(graph2, max_colors2)
    print("\n" + "="*30 + "\n")   
    graph3 = [
        [0, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]
    max_colors3 = 2
    print(f"Graph 3 with {max_colors3} colors:")
    solve_graph_coloring(graph3, max_colors3)
