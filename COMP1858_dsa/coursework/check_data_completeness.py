import pandas as pd
import matplotlib.pyplot as plt

def check_single_column(df, column_name):
	"""
	Checks the number of filled vs empty rows for a specific column in a DataFrame.
	
	Parameters:
		df (pd.DataFrame): Your loaded hotel dataset.
		column_name (str): The specific column name you want to inspect.
	"""
	if column_name not in df.columns:
		print(f"Error: Column '{column_name}' does not exist in the DataFrame.")
		return

	total_rows = len(df)
	
	# Identify empty entries (handles standard NaN/nulls, empty strings, and empty list '[]' strings)
	is_empty_series = (
		df[column_name].isna() | 
		df[column_name].astype(str).str.strip().isin(['', '[]', 'nan', 'None'])
	)
	
	empty_count = is_empty_series.sum()
	filled_count = total_rows - empty_count
	
	filled_pct = (filled_count / total_rows) * 100
	empty_pct = (empty_count / total_rows) * 100

	# Display results
	print(f"\n" + "="*45)
	print(f" Column Inspection: '{column_name}'")
	print("="*45)
	print(f" Total Rows  : {total_rows:,}")
	print(f" Filled	  : {filled_count:,} ({filled_pct:.2f}%)")
	print(f" Empty	   : {empty_count:,} ({empty_pct:.2f}%)")
	print("="*45 + "\n")

	return {"filled": filled_count, "empty": empty_count}

def plot_data_completeness(df, save_fig=False):
	"""
	Calculates the percentage of filled (non-null) values for each attribute 
	in the dataset and displays a horizontal bar chart.
	"""
	# 1. Calculate percentage of non-null values per attribute
	completeness = df.notnull().mean() * 100
	
	# 2. Sort results for a cleaner graph layout
	completeness_df = pd.DataFrame({
		'Attribute': completeness.index,
		'Percent_Filled': completeness.values
	}).sort_values(by='Percent_Filled', ascending=True)

	# 3. Create the plot
	plt.figure(figsize=(10, 6))
	bars = plt.barh(completeness_df['Attribute'], completeness_df['Percent_Filled'], color='#2b5c8f', edgecolor='black')

	# Add labels and titles
	plt.xlabel('Percentage Filled (%)', fontsize=12, fontweight='bold')
	plt.ylabel('Dataset Attributes', fontsize=12, fontweight='bold')
	plt.title('Data Completeness per Attribute (Booking.com Dataset)', fontsize=14, fontweight='bold', pad=15)
	plt.xlim(0, 110)  # Extend X-axis to fit percentage labels cleanly
	
	# Add exact percentage values at the end of each bar
	for bar in bars:
		width = bar.get_width()
		plt.text(
			width + 1.5,					  # X position
			bar.get_y() + bar.get_height()/2, # Y position
			f"{width:.1f}%",				  # Text label
			va='center', 
			ha='left', 
			fontsize=10, 
			fontweight='bold'
		)

	# Add background grid lines on X axis
	plt.grid(axis='x', linestyle='--', alpha=0.5)
	plt.tight_layout()

	# Save figure for report if requested
	if save_fig:
		plt.savefig('data_completeness.png', dpi=300)
		print("Graph saved as 'data_completeness.png'")

	plt.show()

if __name__ == "__main__":
	df_raw = pd.read_csv("hotel_reviews.csv")
	check_single_column(df_raw, "Tags")
	check_single_column(df_raw, "lng")
	check_single_column(df_raw, "lat")
	plot_data_completeness(df_raw)
