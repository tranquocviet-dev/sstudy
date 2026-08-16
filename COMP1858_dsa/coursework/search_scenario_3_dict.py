import pandas
import check_declaration_scenario_b as check_graph
import check_declaration_scenario_c as check
import tags_processing as tags_pro
hotel_to_search = "Hotel Arena"

pd = pandas.read_csv("hotel_reviews.csv")
pd["Tags_Clean"] = pd['Tags'].apply(tags_pro.parse_tags)

df_tags_clean = pd.groupby('Hotel_Name')['Tags_Clean'].apply(tags_pro.combine_tags)

df = pd[["Hotel_Name", "Hotel_Address", "Average_Score", "lat", "lng"]]
df_unique = df.drop_duplicates(subset=["Hotel_Name"]).set_index("Hotel_Name")
df_clean = pandas.merge(df_unique, df_tags_clean, on='Hotel_Name')
df_clean = df_clean.rename(columns={'Tags_Clean': 'Tags'})
df_dict = df_clean.to_dict(orient="index")

hotel_graph = check_graph.build_hotel_graph(df_dict)

cliques = check.find_4_cliques_optimal(hotel_graph)
print(cliques)
