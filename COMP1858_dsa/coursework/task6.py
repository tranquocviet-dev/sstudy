import pandas as pd

def get_top_popular_and_good_hotels(df_clean, top_k=10, weight_score=0.60, weight_engagement=0.40):
	"""
	Ranks hotels based on a combination of popularity and quality (goodness)
	using 3 columns: Average_Score, Total_Number_of_Reviews, and Additional_Number_of_Scores.
	Returns a DataFrame sorted by Composite_Score in descending order.
	"""
	# Step 1: Aggregate per hotel (if working with raw review rows)
	hotel_stats = df_clean.groupby("Hotel_Name").agg({
		"Average_Score": "first",
		"Total_Number_of_Reviews": "first",
		"Additional_Number_of_Scoring": "first"
	}).reset_index()

	# Combine the 2 review volume columns into total customer engagement
	hotel_stats["Total_Engagement"] = (
		hotel_stats["Total_Number_of_Reviews"] + hotel_stats["Additional_Number_of_Scoring"]
	)

	# Step 2: Min-Max Normalization helper function
	def normalize_column(series):
		min_val = series.min()
		max_val = series.max()
		if max_val == min_val:
			return series * 0.0
		return (series - min_val) / (max_val - min_val)

	# Step 3: Compute Normalized Columns (scaled from 0.0 to 1.0)
	norm_score = normalize_column(hotel_stats["Average_Score"])
	norm_engagement = normalize_column(hotel_stats["Total_Engagement"])

	# Step 4: Calculate Weighted Composite Score
	hotel_stats["Composite_Score"] = (
		(weight_score * norm_score) +
		(weight_engagement * norm_engagement)
	)

	# Step 5: Sort using Timsort (O(N log N)) and return top k results
	ranked_hotels = hotel_stats.sort_values(
		by="Composite_Score", 
		ascending=False
	).head(top_k)

	return ranked_hotels

if __name__ == "__main__":
	df_raw = pd.read_csv("hotel_reviews.csv")
	top_hotels = get_top_popular_and_good_hotels(df_raw)
	print(top_hotels[["Hotel_Name", "Average_Score", "Total_Engagement", "Composite_Score"]])
