edges = [
    ("A", "B", 10),
    ("B", "C", 35),
    ("C", "D", 30),
    ("D", "A", 20),
    ("B", "D", 15)
]
print("Cost of individual edges:")
for start_node, end_node, cost in edges:
    print(f"Edge from {start_node} to {end_node}: Cost = {cost}")
total_cost = 0
for start_node, end_node, cost in edges:
    total_cost += cost
    print(f"\nTotal cost of all edges: {total_cost}")

    
