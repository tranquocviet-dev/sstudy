import check_declaration_scenario_c_optimized as optimized
import random
# 1. Load data and build fast graph (from previous optimized step)
df_dict, df_clean = optimized.load_and_preprocess_data("hotel_reviews.csv")
hotel_graph = optimized.build_hotel_graph_fast(df_clean, df_dict)
print(len(df_clean))
# Select a hotel to search
target_hotel = "Hotel Arena"

# Find cliques for that single hotel
target_cliques = optimized.find_4_cliques_for_hotel(hotel_graph, target_hotel)

# Display the results
print(f"\n==================================================")
print(f" 4-Cliques Containing: '{target_hotel}'")
print(f" Total Cliques Found: {len(target_cliques)}")
print(f"==================================================\n")

if target_cliques:
	for idx, clique in enumerate(target_cliques, 1):
		# Format the clique output, highlighting the target hotel
		other_hotels = [h for h in clique if h != target_hotel]
		print(f"Clique #{idx}:")
		print(f"  • Main Hotel : {target_hotel}")
		print(f"  • Connected  : {other_hotels[0]}")
		print(f"                 {other_hotels[1]}")
		print(f"                 {other_hotels[2]}")
		print("-" * 50)
else:
	print(f"No 4-cliques found containing '{target_hotel}'.")

# Get set of unique hotels involved in 4-cliques with target_hotel
unique_hotels = optimized.find_unique_clique_hotels(hotel_graph, target_hotel)

# Display formatted output
print("\n" + "="*55)
print(f" Unique Clique Partners for: '{target_hotel}'")
print(f" Total Unique Connected Hotels: {len(unique_hotels)}")
print("="*55 + "\n")

if unique_hotels:
	for idx, hotel in enumerate(sorted(unique_hotels), 1):
		print(f"  {idx:2d}. {hotel}")
	print("\n" + "-"*55)
else:
	print(f"No clique partners found for '{target_hotel}'.")
