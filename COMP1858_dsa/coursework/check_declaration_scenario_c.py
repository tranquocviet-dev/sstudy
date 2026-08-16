def find_4_cliques_optimal(graph):
	# Finds cliques of size 4 by intersecting neighbor sets of connected edges.
	# graph: dict mapping hotel_name -> set of similar hotel names
	cliques = set()
	
	# Iterate over all edges (u, v)
	for u in graph:
		for v in graph[u]:
			if u < v:  
				common_neighbors = list(graph[u].intersection(graph[v]))
				
				# Check all pairs in the common neighbors set
				n_len = len(common_neighbors)
				for i in range(n_len):
					for j in range(i + 1, n_len):
						w = common_neighbors[i]
						z = common_neighbors[j]
						
						# Check if w and z are connected
						if z in graph[w]:
							clique = tuple(sorted([u, v, w, z]))
							cliques.add(clique)
							
	return list(cliques)
