import pandas

hotel_to_compare = "The Ampersand Hotel"
# hotel_to_compare = "Hotel Arena"
margin_of_error = 0.1

pd = pandas.read_csv("hotel_reviews.csv")
df = pd[["Hotel_Name", "Hotel_Address", "Average_Score"]]
df_clean = df.drop_duplicates()
df_reset = df_clean.reset_index(drop=True)

index_of_hotel = df_reset.loc[df_reset["Hotel_Name"] == hotel_to_compare].index[0]
location_of_hotel = df_clean["Hotel_Address"].iloc[index_of_hotel]
score_of_hotel = df_clean["Average_Score"].iloc[index_of_hotel]

if "United Kingdom" in location_of_hotel:
	country_of_hotel = location_of_hotel.split()[-2]
else:
	country_of_hotel = location_of_hotel.split()[-1]

new_df = df_clean.set_index("Hotel_Name")

filter = new_df[new_df['Hotel_Address'].str.contains(country_of_hotel, na=False)]
filtered = filter.query(f'{score_of_hotel - margin_of_error} <= Average_Score <= {score_of_hotel + margin_of_error}')

print(filtered)
