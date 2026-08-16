import pandas as pd

def print_unique_countries(df):
	"""
	Extracts and prints all distinct countries from the Hotel_Address column.
	
	Parameters:
		df (pd.DataFrame): DataFrame containing 'Hotel_Address' column.
		
	Returns:
		list: Sorted list of unique country names.
	"""
	# Extract country (handles multi-word countries like 'United Kingdom')
	def extract_country(address):
		if not isinstance(address, str):
			return "Unknown"
		address_clean = address.strip()
		if address_clean.endswith("United Kingdom"):
			return "United Kingdom"
		return address_clean.split()[-1]

	# Apply parsing across the dataset
	countries = df['Hotel_Address'].apply(extract_country).unique()
	
	# Filter out any malformed entries and sort alphabetically
	sorted_countries = sorted([c for c in countries if c != "Unknown"])
	
	# Display Summary
	print("=" * 50)
	print(f"TOTAL UNIQUE COUNTRIES FOUND: {len(sorted_countries)}")
	print("=" * 50)
	for i, country in enumerate(sorted_countries, 1):
		print(f"\t{i}. {country}")
	print("=" * 50)
	
	return sorted_countries

# Example usage:
df_raw = pd.read_csv("hotel_reviews.csv")
unique_countries = print_unique_countries(df_raw)
