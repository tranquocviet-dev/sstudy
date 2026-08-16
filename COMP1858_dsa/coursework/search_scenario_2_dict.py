import pandas
import check_declaration_scenario_b as check
import tags_processing as tags_pro
hotel_to_search = "Hotel Arena"
max_degrees = 4

pd = pandas.read_csv("hotel_reviews.csv")
pd["Tags_Clean"] = pd['Tags'].apply(tags_pro.parse_tags)

df_tags_clean = pd.groupby('Hotel_Name')['Tags_Clean'].apply(tags_pro.combine_tags)

df = pd[["Hotel_Name", "Hotel_Address", "Average_Score", "lat", "lng"]]
df_unique = df.drop_duplicates(subset=["Hotel_Name"]).set_index("Hotel_Name")
df_clean = pandas.merge(df_unique, df_tags_clean, on='Hotel_Name')
df_clean = df_clean.rename(columns={'Tags_Clean': 'Tags'})
df_dict = df_clean.to_dict(orient="index")

hotel_graph = check.build_hotel_graph(df_dict)

results = check.find_hotels_within_n_degrees(hotel_graph, hotel_to_search, max_n=max_degrees)

print(f"Search Results for '{hotel_to_search}' up to {max_degrees} Degrees")
for degree, hotels in results.items():
    print(f"\nDegree {degree} ({len(hotels)} hotels found):")
    for h in sorted(hotels):
        print(f" - {h}")
