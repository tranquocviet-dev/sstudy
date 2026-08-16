import math
def extract_country(address):
    # Extracts the country from a full address string.
    # In the Booking.com dataset, the country is located at the end of the address.
    if not isinstance(address, str) or not address.strip():
        return "Unknown"
    
    # Cleaning up whitespace
    address = address.strip()
    
    # Common multi-word countries in the dataset
    if address.endswith("United Kingdom"):
        return "United Kingdom"
    
    # Default: extract the last word (e.g., "France", "Netherlands", "Spain", "Austria", "Italy")
    return address.split()[-1]


def haversine_distance(lat1, lng1, lat2, lng2):
    # Calculates geographical distance in kilometers between two lat/lng pairs.
    # Check for missing/null coordinates
    if None in (lat1, lng1, lat2, lng2):
        return float('inf')
        
    R = 6371.0  # Earth's radius in kilometers
    dlat = math.radians(lat2 - lat1)
    dlng = math.radians(lng2 - lng1)
    
    a = (math.sin(dlat / 2) ** 2 + 
         math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlng / 2) ** 2)
    return R * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def jaccard_similarity(tags1, tags2):
    # Calculates Jaccard overlap ratio between two lists/sets of tags.
    set1, set2 = set(tags1), set(tags2)
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    return intersection / union if union > 0 else 0.0

