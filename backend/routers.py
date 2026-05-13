from fastapi import FastAPI, HTTPException
from .services import get_cords_from_cep
from .store_service import get_nearby_stores


app = FastAPI()


@app.get("/stores-search/")
async def get_stores(cep: str):
    print(f"Buscando lojas próximas ao CEP: {cep}")
    coords = await get_cords_from_cep(cep)
    if not coords:
        raise HTTPException(status_code=404, detail="CEP não encontrado ou sem coodernadas.")
    return coords

@app.get("/stores/{cep}/{category}")
async def get_stores(cep: str, category: str):
    
    coords = await get_cords_from_cep(cep)
    
    
    if not coords:
        raise HTTPException(status_code=404, detail="CEP não encontrado ou sem coodernadas.")
    stores = await get_nearby_stores(
        coords.latitude,
        coords.longitude,
        category
    )
    
    return stores


