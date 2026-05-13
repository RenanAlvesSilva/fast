from .distance_service import calculate_distance
from .cep_service import search_nearby_stores


async def get_nearby_stores(
    user_lat: float,
    user_long: float,
    category: str,
):
   
    
    stores = await search_nearby_stores(
        user_lat,
        user_long,
        category
    )
    
    processed_stores = []
    
    for _store in stores:
        
        distance = calculate_distance(
            user_lat,
            user_long,
            _store["latitude"],
            _store["longitude"]
        )
        _store["distance_km"] = distance
        processed_stores.append(_store)
        
    processed_stores.sort(key=lambda store: store["distance_km"])
    
    return processed_stores
