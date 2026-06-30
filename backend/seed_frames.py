import asyncio
from sqlalchemy import select
from app.database import AsyncSessionLocal
from app.models.models import Movie, Frame

async def seed_frames():
    async with AsyncSessionLocal() as session:
        async with session.begin():
            result = await session.execute(
                select(Movie).where(Movie.slug == "princess-and-the-frog")
            )
            movie = result.scalar_one_or_none()
            if not movie:
                print("Movie not found, seed the movie first.")
                return

            frames = [
                Frame(
                    movie_id=movie.id,
                    image_url="https://res.cloudinary.com/dycmsdxhi/image/upload/v1782799409/frame-1_gpviz1.png",
                    timestamp_label="04:45",
                    description="Community eating gumbo scene",
                    display_order=0,
                ),
                Frame(
                    movie_id=movie.id,
                    image_url="https://res.cloudinary.com/dycmsdxhi/image/upload/v1782799409/frame-2_takrtp.png",
                    timestamp_label="13:02",
                    description="Tiana in her restaurant",
                    display_order=1,
                ),
                Frame(
                    movie_id=movie.id,
                    image_url="https://res.cloudinary.com/dycmsdxhi/image/upload/v1782799408/frame-3_lcmkpg.png",
                    timestamp_label="19:03",
                    description="Naveen and the voodoo room",
                    display_order=2,
                ),
                Frame(
                    movie_id=movie.id,
                    image_url="https://res.cloudinary.com/dycmsdxhi/image/upload/v1782799409/frame-4_tzmwtj.png",
                    timestamp_label="48:00",
                    description="Nighttime fireflies in the bayou scene",
                    display_order=3,
                ),
                Frame(
                    movie_id=movie.id,
                    image_url="https://res.cloudinary.com/dycmsdxhi/image/upload/v1782805459/frame-5_b_a20nqu.png",
                    timestamp_label="1:00:35",
                    description="Mama Odie's entrance",
                    display_order=4,
                ),
            ]
            session.add_all(frames)
            print("Seeded 5 frames.")

asyncio.run(seed_frames())