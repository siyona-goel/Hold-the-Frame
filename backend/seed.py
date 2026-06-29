import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import engine, Base, AsyncSessionLocal
from app.models.models import Movie

async def seed():
    async with AsyncSessionLocal() as session:
        async with session.begin():
            # Check if already seeded
            from sqlalchemy import select
            result = await session.execute(select(Movie))
            existing = result.scalars().all()
            
            if existing:
                print("Database already has movies, skipping seed.")
                return

            movies = [
                Movie(
                    title="The Princess and the Frog",
                    year=2009,
                    studio="Walt Disney Animation Studios",
                    cover_image_url="https://res.cloudinary.com/dycmsdxhi/image/upload/v1782737801/the_princess_and_the_frog_xveljl.jpg",
                    slug="princess-and-the-frog",
                ),
            ]

            session.add_all(movies)
            print("Seeded 1 movie.")

asyncio.run(seed())