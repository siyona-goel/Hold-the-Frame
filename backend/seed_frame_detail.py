import asyncio
from sqlalchemy import select
from app.database import AsyncSessionLocal
from app.models.models import Frame, Annotation, PaletteColor, AnnotationCategory

async def seed():
    async with AsyncSessionLocal() as session:
        async with session.begin():
            # Get the first frame
            result = await session.execute(select(Frame).order_by(Frame.id).limit(1))
            frame = result.scalar_one_or_none()
            if not frame:
                print("No frames found.")
                return

            annotations = [
                Annotation(
                    frame_id=frame.id,
                    x_position=25.0,
                    y_position=60.0,
                    content="happy, nostalgic",
                    category=AnnotationCategory.emotion,
                ),
                Annotation(
                    frame_id=frame.id,
                    x_position=70.0,
                    y_position=35.0,
                    content="Chiaroscuro: The idea of a warm loving home comes from the cozy frame created by the contrast between the muted blue-gray tones of the night and the golden-yellow interior light.",
                    category=AnnotationCategory.technique,
                ),
            ]

            palette_colors = [
                PaletteColor(frame_id=frame.id, hex_value="#140D09ff", display_order=0),
                PaletteColor(frame_id=frame.id, hex_value="#3C251Dff", display_order=1),
                PaletteColor(frame_id=frame.id, hex_value="#9A5B05ff", display_order=2),
                PaletteColor(frame_id=frame.id, hex_value="#F5A51Eff", display_order=3),
                PaletteColor(frame_id=frame.id, hex_value="#F2F826ff", display_order=4),
            ]

            session.add_all(annotations)
            session.add_all(palette_colors)
            print(f"Seeded 2 annotations and 5 palette colors for frame {frame.id}.")

asyncio.run(seed())
