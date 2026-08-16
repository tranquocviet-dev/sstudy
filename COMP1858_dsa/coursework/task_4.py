import math
import pandas as pd
import ast
import random
from collections import deque

# =========================================================
# 1. OPTIMIZED DATA PREPARATION
# =========================================================
def load_and_preprocess_data(csv_path):
	df_raw = pd.read_csv(csv_path)

	# Fast tag string cleaning
	def clean_tags(tag_input):
		if not isinstance(tag_input, str) or not tag_input.strip():
			return set()
		try:
			parsed = ast.literal_eval(tag_input.strip())
			if isinstance(parsed, list):
				return {str(t).strip() for t in parsed if str(t).strip()}
		except Exception:
			pass
		clean_str = tag_input.replace("[", "").replace("]", "").replace("'", "").replace('"', '')
		return {t.strip() for t in clean_str.split(",") if t.strip()}

	df_raw['Tags_Set'] = df_raw['Tags'].apply(clean_tags)

	# Combine tags per hotel
	hotel_tags = df_raw.groupby('Hotel_Name')['Tags_Set'].apply(
		lambda series: set().union(*series)
	).reset_index()

	# Get static info
	df_unique = df_raw[["Hotel_Name", "Hotel_Address", "Average_Score", "lat", "lng"]].drop_duplicates(subset=["Hotel_Name"])
	df_clean = pd.merge(df_unique, hotel_tags, on='Hotel_Name')

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
	# Keys will contain 'Tags_Set' as actual Python sets
	df_dict = df_clean.set_index("Hotel_Name", drop=False).to_dict(orient="index")
	return df_dict, df_clean

# =========================================================
# 2. FAST SIMILARITY FUNCTION
# =========================================================
def haversine_distance(lat1, lon1, lat2, lon2):
	R = 6371.0
	dlat = math.radians(lat2 - lat1)
	dlon = math.radians(lon2 - lon1)
	a = (math.sin(dlat / 2) ** 2 + 
		 math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2) ** 2)
	return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def are_hotels_similar_fast(h1, h2, max_dist_km=5.0, max_score_diff=0.5, min_tag_sim=0.3):
	# Check 1: Country Match (Instant String Check)
	if h1['Country'] != h2['Country']:
		return False

	# Check 2: Score Difference (Instant Float Check)
	if abs(h1['Average_Score'] - h2['Average_Score']) > max_score_diff:
		return False

	# Check 3: Bounding Box Filter (Fast Float Math)
	# 0.05 degrees is approximately ~5.5 km.
	if abs(h1['lat'] - h2['lat']) > 0.05 or abs(h1['lng'] - h2['lng']) > 0.05:
		return False

	# Check 4: Haversine Distance (Only executed if Bounding Box passed)
	dist = haversine_distance(h1['lat'], h1['lng'], h2['lat'], h2['lng'])
	if dist > max_dist_km:
		return False

	# Check 5: Jaccard Similarity (Sets are ALREADY built!)
	s1 = h1['Tags_Set']
	s2 = h2['Tags_Set']
	intersection_len = len(s1.intersection(s2))
	if intersection_len == 0:
		return False

	union_len = len(s1.union(s2))
	return True if (intersection_len / union_len) >= min_tag_sim else False
	# Time complexity: O(n) (n is the number of hotels) due to every hotel going through the check once


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

# Scenario A already comes in Scenario B's answer

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

# Miscalaneous functions

def find_unique_clique_hotels(graph, target_hotel):
	"""
	Finds all unique hotels that form 4-cliques with the target_hotel.

	Parameters:
		graph (dict): Adjacency list mapping hotel names to sets of similar hotel names.
		target_hotel (str): The hotel to analyze.

	Returns:
		set: A set of unique hotel names connected in 4-cliques with target_hotel.
	"""
	if target_hotel not in graph:
		print(f"Error: '{target_hotel}' not found in the graph.")
		return set()

	u = target_hotel
	neighbors_u = graph[u]

	if len(neighbors_u) < 3:
		print(f"'{target_hotel}' has fewer than 3 neighbors ({len(neighbors_u)} found). Cannot form a 4-clique.")
		return set()

	unique_clique_hotels = set()
	neighbors_list = list(neighbors_u)
	n = len(neighbors_list)

	# Search for valid 4-cliques anchored at target_hotel
	for i in range(n):
		v = neighbors_list[i]
		neighbors_v = graph[v]

		for j in range(i + 1, n):
			w = neighbors_list[j]

			# Check if v and w are connected
			if w in neighbors_v:
				# Find candidate z connected to u, v, AND w
				candidates = neighbors_u.intersection(neighbors_v).intersection(graph[w])

				# If there are any candidates z, then u, v, w, and z form 4-cliques
				if candidates:
					unique_clique_hotels.add(v)
					unique_clique_hotels.add(w)
					unique_clique_hotels.update(candidates)

	# Remove the target hotel itself if it got added to the set
	unique_clique_hotels.discard(u)

	return unique_clique_hotels

# =========================================================
# SCENARIO C: HOTELS WITHIN N DEGREES
# =========================================================
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
	print(len(df_clean))
	# Select a hotel to search
	target_hotel = "Hotel Arena"

	# Find hotels within n degrees to a hotel: scenario a and b
	# Scenario a is the first degree
	n_degrees = 3

	results = find_hotels_within_n_degrees(hotel_graph, target_hotel, max_n=n_degrees)

	print(f"=== Search Results for '{target_hotel}' up to {n_degrees} Degrees ===")
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

	# Find 5-cliques
	cliques_5 = find_k_cliques_for_hotel(hotel_graph, target_hotel, k=5)
	print(f"Total 5-Cliques for '{target_hotel}': {len(cliques_5)}")
