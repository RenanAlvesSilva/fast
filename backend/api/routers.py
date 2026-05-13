from fastapi import FastAPI, HTTPException
from ..services.cep_service import get_cords_from_cep
from ..services.store_service import get_nearby_stores


app = FastAPI(
    title="Buscador de Lojas",
    description="API para busca de locais próximos com base no CEP e categoria.",
    version="1.0.0"
)


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
    try:
        stores = await get_nearby_stores(
            coords.latitude,
            coords.longitude,
            category
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return stores
