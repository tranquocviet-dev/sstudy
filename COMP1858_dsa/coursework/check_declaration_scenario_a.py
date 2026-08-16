from base_functions import extract_country, haversine_distance, jaccard_similarity

def are_hotels_similar(h1, h2, max_dist_km=5.0, max_score_diff=0.5, min_tag_sim=0.3):
    """
    Determines if two hotels are 1-degree similar using multi-criteria matching.
    """
    # 1. COUNTRY FILTER (Fast Check using parsed full address)
    country1 = extract_country(h1['Hotel_Address'])
    country2 = extract_country(h2['Hotel_Address'])
    
    if country1 != country2:
        return False  # Skip calculation if hotels are in different countries
        
    # 2. GEOGRAPHIC DISTANCE FILTER (Haversine)
    dist = haversine_distance(h1['lat'], h1['lng'], h2['lat'], h2['lng'])
    if dist > max_dist_km:
        return False
        
    # 3. AVERAGE SCORE DIFFERENCE FILTER
    if abs(h1['Average_Score'] - h2['Average_Score']) > max_score_diff:
        return False
        
    # 4. TAG SIMILARITY FILTER (Jaccard Index)
    tag_sim = jaccard_similarity(h1['Tags'], h2['Tags'])
    if tag_sim < min_tag_sim:
        return False
        
    return True
