from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
import os

router = APIRouter()

@router.get("/square/{champion_name}")
async def get_square(champion_name):
    img = Path(f'champions\\{champion_name}\\square.png')
    if not img.is_file():
        raise HTTPException(status_code=404, detail="item not found")
    return FileResponse(img)


@router.get("/splash/{champion_name}")
async def get_square(champion_name):
    img = Path(f'champions\\{champion_name}\\splash.png')
    if not img.is_file():
        raise HTTPException(status_code=404, detail="item not found")
    return FileResponse(img)

@router.get("/centered/{champion_name}")
async def get_square(champion_name):
    img = Path(f'champions\\{champion_name}\\centered.png')
    if not img.is_file():
        raise HTTPException(status_code=404, detail="item not found")
    return FileResponse(img)

@router.get("/portrait/{champion_name}")
async def get_square(champion_name):
    img = Path(f'champions\\{champion_name}\\portrait.png')
    if not img.is_file():
        raise HTTPException(status_code=404, detail="item not found")
    return FileResponse(img)

@router.get("/skill/p/{champion_name}")
async def get_square(champion_name):
    img = Path(f'champions\\{champion_name}\\p.png')
    if not img.is_file():
        raise HTTPException(status_code=404, detail="item not found")
    return FileResponse(img)

@router.get("/skill/q/{champion_name}")
async def get_square(champion_name):
    img = Path(f'champions\\{champion_name}\\q.png')
    if not img.is_file():
        raise HTTPException(status_code=404, detail="item not found")
    return FileResponse(img)

@router.get("/skill/w/{champion_name}")
async def get_square(champion_name):
    img = Path(f'champions\\{champion_name}\\w.png')
    if not img.is_file():
        raise HTTPException(status_code=404, detail="item not found")
    return FileResponse(img)

@router.get("/skill/e/{champion_name}")
async def get_square(champion_name):
    img = Path(f'champions\\{champion_name}\\e.png')
    if not img.is_file():
        raise HTTPException(status_code=404, detail="item not found")
    return FileResponse(img)

@router.get("/skill/r/{champion_name}")
async def get_square(champion_name):
    img = Path(f'champions\\{champion_name}\\r.png')
    if not img.is_file():
        raise HTTPException(status_code=404, detail="item not found")
    return FileResponse(img)
