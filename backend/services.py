from .schemas import CoordsUser
from typing import Optional
import httpx
from .category import CATEGORY_MAP
async def get_cords_from_cep(cep: str) -> Optional[CoordsUser]:
    
    cep_url = f"https://viacep.com.br/ws/{cep}/json/"
    
    async with httpx.AsyncClient() as cliente:
        anddress = await cliente.get(cep_url)
        anddress = anddress.json()
        
    
    if anddress.get("erro"):
        raise ValueError(f"CEP {cep} não encontrado.")
    
    street = anddress.get('logradouro')
    city = anddress.get('localidade')
    state = anddress.get('uf')
    
    full_andress = f"{street}, {city}, {state}, Brasil"
    
    geo_url = "https://nominatim.openstreetmap.org/search"
    
    params = {
        "q" : full_andress,
        "format": "json",
        "limit": 1
    }
    
    headers = {
        "User-Agent": "buscador-lojas"
    }
    
    async with httpx.AsyncClient() as cliente:
        response = await cliente.get(
            geo_url,
            params = params,
            headers = headers
        )
    
    data = response.json()
    
    if not data:
        return None
    
    
    return CoordsUser(
        latitude=data[0]["lat"],
        longitude=data[0]["lon"]
    )
    


async def search_nearby_stores(
    latitude: float,
    longitude: float,
    category: str,
    radius: int = 5000,
):
    
    overpass_url = "https://overpass-api.de/api/interpreter"
    
    category_data = CATEGORY_MAP.get(category)
    if not category_data:
        raise ValueError(f"Categoria '{category}' não encontrada.")
    
    key = category_data["key"]
    value = category_data["value"]
    
    query = f"""
    [out:json];
    (
        node ["{key}" = "{value}"]
        (around:{radius}, {latitude}, {longitude});
    );
    
    out body;
    """
    async with httpx.AsyncClient() as cliente:
        response = await cliente.post(
            overpass_url,
            data=query,
            headers= {"User-Agent": "buscador-lojas"}
        )
    
    data = response.json()
    
    stores = []
    
    for item in data["elements"]:
        tags = item.get("tags", {})
        stores.append({
            "id": item.get("id"),
            "name": tags.get("name", "Loja sem nome"),
            "latitude": item.get("lat"),
            "longitude": item.get("lon")
        })
        
    return stores
    