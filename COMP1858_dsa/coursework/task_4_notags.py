import math
import pandas as pd
import ast
import random
from collections import deque
from itertools import combinations

# =========================================================
# 1. OPTIMIZED DATA PREPARATION
# =========================================================
def load_and_preprocess_data(csv_path):
	df_raw = pd.read_csv(csv_path)

	# Get static info
	df_unique = df_raw[["Hotel_Name", "Hotel_Address", "Average_Score", "lat", "lng"]].drop_duplicates(subset=["Hotel_Name"])
	df_clean = df_unique.dropna(subset=["lat", "lng"]).reset_index(drop=True)

	# Parse Country once during data prep
	def extract_country(address):
		if not isinstance(address, str) or not address.strip():
			return "Unknown"
		address = address.strip()
		if address.endswith("United Kingdom"):
			return "United Kingdom"
		return address.split()[-1]

	df_clean['Country'] = df_clean['Hotel_Address'].apply(extract_country)

	# Store pre-processed data as dictionary
	df_dict = df_clean.set_index("Hotel_Name", drop=False).to_dict(orient="index")
	return df_dict, df_clean

# =========================================================
# 2. FAST SIMILARITY FUNCTION
# =========================================================
def are_hotels_similar_fast(h1, h2, max_dist=5.0, max_score_diff=0.5):
	# Check 1: Country Match (Instant String Check)
	if h1['Country'] != h2['Country']:
		return False

	# Check 2: Score Difference (Instant Float Check)
	if abs(h1['Average_Score'] - h2['Average_Score']) > max_score_diff:
		return False

	# Check 3: Bounding Box Filter (Fast Float Math)
	# 0.05 degrees is approximately ~5.5 km.
	if abs(h1['lat'] - h2['lat']) > (max_dist / 100) or abs(h1['lng'] - h2['lng']) > (max_dist / 100):
		return False

	return True

# =========================================================
# 3. FAST GRAPH CONSTRUCTION (BY COUNTRY BUCKETS)
# =========================================================
def build_hotel_graph_fast(df_clean, df_dict):
	"""Group hotels by country so we only evaluate pairs within the same country."""
	graph = {hotel: set() for hotel in df_dict}

	# Bucket hotel names by country
	country_groups = df_clean.groupby('Country')['Hotel_Name'].apply(list).to_dict()

	for country, hotel_names in country_groups.items():
		n = len(hotel_names)
		for i in range(n):
			name1 = hotel_names[i]
			h1 = df_dict[name1]

			for j in range(i + 1, n):
				name2 = hotel_names[j]
				h2 = df_dict[name2]

				if are_hotels_similar_fast(h1, h2):
					graph[name1].add(name2)
					graph[name2].add(name1)

	return graph
	# Time complexity: O(n^2) (n is the number of hotels) in the worst possible case, due to the function running through 2 nested O(n) loops, with time saves coming from the Country filter

# =========================================================
# SCENARIO A: DIRECTLY SIMILAR HOTELS
# =========================================================
def find_directly_similar_hotels(graph, target_hotel):
	"""
	Finds all hotels directly similar (1 degree of separation) to a specific target hotel.
	
	Parameters:
		graph (dict): Adjacency list graph returned by build_hotel_graph_fast.
		target_hotel (str): Name of the starting hotel.
		
	Returns:
		list: Alphabetically sorted list of directly similar hotel names.
	"""
	# Check if the target hotel exists in the graph dictionary
	if target_hotel not in graph:
		print(f"Error: '{target_hotel}' not found in the graph.")
		return []
	
	# Direct neighbors are stored as a set in the adjacency list graph
	similar_hotels = list(graph[target_hotel])
	
	return sorted(similar_hotels)
# =========================================================
# SCENARIO B: HOTELS WITHIN N DEGREES
# =========================================================
def find_hotels_within_n_degrees(graph, start_hotel, max_n=4):
	"""
	Finds all hotels within n degrees of separation from a starting hotel using BFS.

	Parameters:
		graph (dict): Adjacency list mapping hotel names to sets of similar hotel names.
		start_hotel (str): The hotel name to start searching from.
		max_n (int): Maximum degree of separation (default = 4).

	Returns:
		dict: A dictionary mapping degree levels (1..max_n) to sets of hotel names.
	"""
	# 1. Validation check
	if start_hotel not in graph:
		print(f"Error: '{start_hotel}' was not found in the dataset graph.")
		return {}

	# 2. Track visited hotels to prevent infinite loops / cycles
	visited = {start_hotel}

	# 3. Queue stores tuples of (current_hotel, current_degree)
	queue = deque([(start_hotel, 0)])

	# 4. Results grouped by degree level: {1: set(), 2: set(), 3: set(), 4: set()}
	results_by_degree = {degree: set() for degree in range(1, max_n + 1)}

	# 5. Execute BFS traversal
	while queue:
		current_hotel, current_degree = queue.popleft()

		# Stop expanding neighbors if max_n degree threshold is reached
		if current_degree >= max_n:
			continue

		next_degree = current_degree + 1

		# Explore direct neighbors
		for neighbor in graph[current_hotel]:
			if neighbor not in visited:
				visited.add(neighbor)
				results_by_degree[next_degree].add(neighbor)
				queue.append((neighbor, next_degree))

	return results_by_degree

# =========================================================
# SCENARIO C: HOTELS WITHIN N DEGREES
# =========================================================

# AI VERSION
def find_k_cliques_for_hotel_ai(graph, target_hotel, k=4):
	"""
	Finds all k-cliques containing target_hotel by generating ALL combinations 
	of its neighbors and checking every pairwise edge manually.
	
	Parameters:
		graph (dict): Adjacency list mapping hotel names to sets/lists of similar hotels.
		target_hotel (str): Starting hotel name.
		k (int): Target clique size (default = 4).
		
	Returns:
		list: List of sorted k-tuples representing cliques containing target_hotel.
	"""
	# 1. Validation check
	if target_hotel not in graph:
		print(f"Error: '{target_hotel}' not found in graph.")
		return []
		
	# Target hotel needs at least (k - 1) neighbors to form a k-clique
	neighbors = list(graph[target_hotel])
	if len(neighbors) < (k - 1):
		print(f"'{target_hotel}' has fewer than {k - 1} neighbors. Cannot form a {k}-clique.")
		return []

	cliques = set()

	# 2. BRUTE-FORCE STEP: Generate ALL possible combinations of (k - 1) neighbors
	# Time Complexity: O(C(d, k-1) * k^2), where d is the degree of target_hotel
	neighbor_combinations = combinations(neighbors, k - 1)

	for combo in neighbor_combinations:
		# Check if every hotel in this combination is connected to every other hotel in it
		is_clique = True
		combo_len = len(combo)
		
		for i in range(combo_len):
			for j in range(i + 1, combo_len):
				hotel1 = combo[i]
				hotel2 = combo[j]
				
				# Unoptimized edge lookup check
				if hotel2 not in graph[hotel1]:
					is_clique = False
					break
			if not is_clique:
				break
				
		# 3. If all pairwise connections exist, it forms a valid k-clique with target_hotel
		if is_clique:
			full_clique = tuple(sorted([target_hotel] + list(combo)))
			cliques.add(full_clique)

	return list(cliques)

# IMPROVED VERSION

def find_k_cliques_for_hotel(graph, target_hotel, k=4):
	"""
	Finds all unique cliques of size k that include the target_hotel.

	Parameters:
		graph (dict): Adjacency list mapping hotel names to sets of similar hotel names.
		target_hotel (str): Starting hotel name.
		k (int): Target clique size (e.g., k=3, 4, 5, etc.).

	Returns:
		list: List of sorted k-tuples representing all k-cliques containing target_hotel.
	"""
	# 1. Input Validation
	if target_hotel not in graph:
		print(f"Error: '{target_hotel}' not found in the graph.")
		return []

	# Need at least (k - 1) neighbors to form a k-clique
	if len(graph[target_hotel]) < (k - 1):
		print(f"'{target_hotel}' has fewer than {k - 1} neighbors. Cannot form a clique of size {k}.")
		return []

	cliques = set()

	def backtrack(current_clique, candidate_set):
		# Base Case: Found a valid clique of size k
		if len(current_clique) == k:
			cliques.add(tuple(sorted(current_clique)))
			return

		# Pruning: Not enough candidates left to reach size k
		if len(current_clique) + len(candidate_set) < k:
			return

		# Recursive Step
		candidate_list = sorted(list(candidate_set))
		for i, candidate in enumerate(candidate_list):
			# Form next set of candidates: must be connected to the new candidate
			next_candidates = candidate_set.intersection(graph[candidate])

			# Recurse deeper
			backtrack(current_clique + [candidate], next_candidates)

	# Initial call: Start with target_hotel in clique, candidates are its direct neighbors
	initial_clique = [target_hotel]
	initial_candidates = set(graph[target_hotel])

	backtrack(initial_clique, initial_candidates)

	return list(cliques)

if __name__ == "__main__":
	# 1. Load data and build fast graph (from previous  step)
	df_dict, df_clean = load_and_preprocess_data("hotel_reviews.csv")
	hotel_graph = build_hotel_graph_fast(df_clean, df_dict)
	# Select a hotel to search
	target_hotel = "Hotel Arena"

	# Scenario a
	directly_similar = find_directly_similar_hotels(hotel_graph, target_hotel)
	print(f"=== Directly Similar Hotels for '{target_hotel}' ({len(directly_similar)} found) ===")
	for idx, hotel in enumerate(directly_similar, 1):
		print(f"{idx:2d}. {hotel}")

	# Scenario b
	n_degrees = 4

	results = find_hotels_within_n_degrees(hotel_graph, target_hotel, max_n=n_degrees)

	print(f"\n=== Search Results for '{target_hotel}' up to {n_degrees} Degrees ===")
	for degree in range(1, n_degrees + 1):
		hotels_at_degree = results[degree]
		print(f"\nDegree {degree} ({len(hotels_at_degree)} hotels found):")
		for hotel in sorted(hotels_at_degree):
			print(f"  - {hotel}")

	print("\n== Scenario c: find n-cliques for a hotel ==\n")
	# Find 3-cliques (triangles)
	cliques_3 = find_k_cliques_for_hotel(hotel_graph, target_hotel, k=3)
	print(f"Total 3-Cliques for '{target_hotel}': {len(cliques_3)}")

	# Find 4-cliques (as required by the spec)
	cliques_4 = find_k_cliques_for_hotel(hotel_graph, target_hotel, k=4)
	print(f"Total 4-Cliques for '{target_hotel}': {len(cliques_4)}")

	cliques_5 = find_k_cliques_for_hotel(hotel_graph, target_hotel, k=4)

	# Find 5-cliques
	# cliques_5 = find_k_cliques_for_hotel(hotel_graph, target_hotel, k=5)
	# print(f"Total 5-Cliques for '{target_hotel}': {len(cliques_5)}")
