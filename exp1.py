visited = []
queue = []

graph = {"A": ["B", "C"], "B": ["D"], "C": ["E"], "D": [], "E": []}
start_node = "A"

queue.append(start_node)
visited.append(start_node)

while queue:
    current_node = queue.pop(0)
    print(current_node)

    for neighbor in graph[current_node]:
        if neighbor not in visited:
            visited.append(neighbor)
            queue.append(neighbor)
