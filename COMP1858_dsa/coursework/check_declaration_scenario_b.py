from collections import deque
import check_declaration_scenario_a as check

# ==========================================
# STEP 1: Build the Graph (Adjacency List)
# ==========================================
def build_hotel_graph(df_dict):
    # Compares every pair of hotels and builds an Adjacency List.
    # graph = {
    #     'Hotel A': {'Hotel B', 'Hotel C'},
    #     'Hotel B': {'Hotel A'},
    #     ...
    # }
    graph = {hotel: set() for hotel in df_dict}
    hotel_names = list(df_dict.keys())
    
    # Compare all unique pairs to build edges
    for i in range(len(hotel_names)):
        name1 = hotel_names[i]
        hotel1 = df_dict[name1]
        
        for j in range(i + 1, len(hotel_names)):
            name2 = hotel_names[j]
            hotel2 = df_dict[name2]
            
            # Using the similarity function
            if check.are_hotels_similar(hotel1, hotel2):
                graph[name1].add(name2)
                graph[name2].add(name1)
                
    return graph


# ==========================================
# STEP 2: BFS Function for n Degrees
# ==========================================
def find_hotels_within_n_degrees(graph, start_hotel, max_n=4):
    # Performs BFS to find all hotels up to max_n degrees of separation.
    # Returns a dictionary mapping degree (1..max_n) to sets of hotel names.
    if start_hotel not in graph:
        print(f"Error: '{start_hotel}' not found in the graph.")
        return {}
    
    visited = {start_hotel}
    # Queue stores tuples of: (current_hotel_name, current_degree)
    queue = deque([(start_hotel, 0)])
    
    # Structure to hold results per degree: {1: set(), 2: set(), 3: set(), 4: set()}
    results_by_degree = {degree: set() for degree in range(1, max_n + 1)}
    
    while queue:
        current_hotel, current_degree = queue.popleft()
        
        # Stop expanding past max_n
        if current_degree >= max_n:
            continue
            
        next_degree = current_degree + 1
        
        # Explore immediate neighbors
        for neighbor in graph[current_hotel]:
            if neighbor not in visited:
                visited.add(neighbor)
                results_by_degree[next_degree].add(neighbor)
                queue.append((neighbor, next_degree))
                
    return results_by_degree
