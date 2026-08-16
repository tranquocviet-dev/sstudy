import pandas
import check_declaration_scenario_a as check
hotel_to_search = "Hotel Arena" 

pd = pandas.read_csv("hotel_reviews.csv")
df = pd[["Hotel_Name", "Hotel_Address", "Average_Score", "lat", "lng", "Tags"]]
df_clean = df.drop_duplicates(subset=["Hotel_Name"]).set_index("Hotel_Name")
df_dict = df_clean.to_dict(orient="index")

for hotel_compare in df_dict:
	hotel1 = df_dict[hotel_to_search]
	hotel2 = df_dict[hotel_compare]
	if check.are_hotels_similar(hotel1, hotel2):
		print(hotel_compare)
