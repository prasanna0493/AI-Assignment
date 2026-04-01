from queue import PriorityQueue

def best_first_search(graph, start, goal, heuristic):
    visited = []
    pq = PriorityQueue()
    
    
    pq.put((heuristic[start], start))
    
    while not pq.empty():
        (h, current) = pq.get()
        
        if current not in visited:
            print("Visited:", current)
            visited.append(current)
            
            if current == goal:
                print("Goal Reached!")
                return
            
            for neighbor in graph[current]:
                if neighbor not in visited:
                    pq.put((heuristic[neighbor], neighbor))


graph = {
    'S': ['A', 'B'],
    'A': ['C', 'D'],
    'B': ['E'],
    'C': [],
    'D': [],
    'E': []
}


heuristic = {
    'S': 5,
    'A': 3,
    'B': 4,
    'C': 2,
    'D': 6,
    'E': 1
}


best_first_search(graph, 'S', 'E', heuristic)