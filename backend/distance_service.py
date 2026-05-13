from geopy.distance import geodesic

def calculate_distance(
    user_lat: float,
    user_long: float,
    store_lat: float,
    store_long: float,
):
    user_coords = (user_lat, user_long)
    store_coords = (store_lat, store_long)
    
    distance = geodesic(user_coords, store_coords).km
    
    return distance