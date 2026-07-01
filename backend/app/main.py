from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import selectinload
from app.database import AsyncSessionLocal
from app.models.models import Movie, Frame

app = FastAPI(title="Hold the Frame API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://*.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@app.get("/")
async def root():
    return {"message": "Hold the Frame API is running"}

@app.get("/movies")
async def get_movies(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Movie))
    movies = result.scalars().all()
    return [
        {
            "id": m.id,
            "title": m.title,
            "year": m.year,
            "studio": m.studio,
            "cover_image_url": m.cover_image_url,
            "slug": m.slug,
        }
        for m in movies
    ]

@app.get("/movies/{slug}")
async def get_movie(slug: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Movie).where(Movie.slug == slug))
    movie = result.scalar_one_or_none()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {
        "id": movie.id,
        "title": movie.title,
        "year": movie.year,
        "studio": movie.studio,
        "cover_image_url": movie.cover_image_url,
        "slug": movie.slug,
    }

@app.get("/movies/{slug}/frames")
async def get_frames(slug: str, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Movie).where(Movie.slug == slug))
    movie = result.scalar_one_or_none()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    result = await db.execute(
        select(Frame)
        .where(Frame.movie_id == movie.id)
        .order_by(Frame.display_order)
    )
    frames = result.scalars().all()
    return [
        {
            "id": f.id,
            "movie_id": f.movie_id,
            "image_url": f.image_url,
            "timestamp_label": f.timestamp_label,
            "description": f.description,
            "display_order": f.display_order,
        }
        for f in frames
    ]

@app.get("/frames/{frame_id}")
async def get_frame(frame_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(Frame)
        .where(Frame.id == frame_id)
        .options(
            selectinload(Frame.annotations),
            selectinload(Frame.palette_colors)
        )
    )
    frame = result.scalar_one_or_none()
    if not frame:
        raise HTTPException(status_code=404, detail="Frame not found")

    return {
        "id": frame.id,
        "movie_id": frame.movie_id,
        "image_url": frame.image_url,
        "timestamp_label": frame.timestamp_label,
        "description": frame.description,
        "display_order": frame.display_order,
        "annotations": [
            {
                "id": a.id,
                "frame_id": a.frame_id,
                "x_position": a.x_position,
                "y_position": a.y_position,
                "content": a.content,
                "category": a.category.value,
            }
            for a in sorted(frame.annotations, key=lambda a: a.id)
        ],
        "palette_colors": [
            {
                "id": c.id,
                "frame_id": c.frame_id,
                "hex_value": c.hex_value,
                "display_order": c.display_order,
            }
            for c in sorted(frame.palette_colors, key=lambda c: c.display_order)
        ],
    }
