from contextlib import asynccontextmanager
from typing import AsyncGenerator, Annotated

from fastapi import Body, FastAPI, HTTPException, Depends
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import engine, new_sessison
from src.database.models import Base

from src.exception import NoLongUrlFoundError, SlugAlreadyExists

from src.service import generate_short_url, get_url_by_slug

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(lifespan=lifespan)

# During development it's convenient to allow local origins. For production restrict origins.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500", "http://localhost:8000", "http://127.0.0.1:8000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with new_sessison() as session:
        yield session

@app.post("/short_url")
async def generate_slug(
    long_url: Annotated[str, Body(embed=True)],
    session: Annotated[AsyncSession, Depends(get_session)]):
    try:
        new_slug = await generate_short_url(long_url, session)
    except SlugAlreadyExists:
        raise HTTPException(status_code=500)
    return {"data": new_slug}

@app.get("/{slug}")
async def redirect_to_url(
    slug:str,
    session: Annotated[AsyncSession, Depends(get_session)]):
    try: 
        long_url = await get_url_by_slug(slug, session)
    except NoLongUrlFoundError:
        raise HTTPException(status_code=404)
    return RedirectResponse(url=long_url, status_code=302)

