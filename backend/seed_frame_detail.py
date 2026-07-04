import asyncio
from sqlalchemy import select, delete
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
            
            # Delete all existing annotations for this frame before reinserting
            await session.execute(
                delete(Annotation).where(Annotation.frame_id == frame.id)
            )
            # Delete all existing palette colors for this frame before reinserting
            await session.execute(
                delete(PaletteColor).where(PaletteColor.frame_id == frame.id)
            )

            annotations = [
                Annotation(
                    frame_id=frame.id,
                    x_position=6.9,
                    y_position=10.0,
                    content="happy, nostalgic",
                    category=AnnotationCategory.emotion,
                ),
                Annotation(
                    frame_id=frame.id,
                    x_position=69.8,
                    y_position=25.0,
                    content="Community, comfort, simplicity & contentment",
                    category=AnnotationCategory.theme,
                ),
                Annotation(
                    frame_id=frame.id,
                    x_position=47.9,
                    y_position=21.6,
                    content="Backlighting: The halo effect around the family draws the viewer's eye immediately to the focal point of the shot.",
                    category=AnnotationCategory.technique,
                ),
                Annotation(
                    frame_id=frame.id,
                    x_position=26.9,
                    y_position=19.8,
                    content="Chiaroscuro: The idea of a warm loving home comes from the cozy frame created by the contrast between the muted blue-gray tones of the night and the golden-yellow interior light.",
                    category=AnnotationCategory.technique,
                ),
                Annotation(
                    frame_id=frame.id,
                    x_position=50,
                    y_position=68.9,
                    content="Layered Composition: Closely mimics the depth achieved by a physical multiplane camera. Gives a 2D animation scene a sense of 3D space.",
                    category=AnnotationCategory.technique,
                ),
                Annotation(
                    frame_id=frame.id,
                    x_position=16.4,
                    y_position=41.9,
                    content="Tapering: Gives the characters an organic, fluid feel",
                    category=AnnotationCategory.technique,
                ),
                Annotation(
                    frame_id=frame.id,
                    x_position=29.1,
                    y_position=81.7,
                    content="This is the first scene in the movie (although there are many more to come) that gives viewers a warm, fuzzy feeling inside. I spent some time observing the differences between the people, but the one thing that's the same is their smile. That seriously must be some delicious gumbo. The scene perfectly portrays the intended 'united by food' idea they want to convey to their viewers.",
                    category=AnnotationCategory.general,
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
            print(f"Reseeded {len(annotations)} annotations for frame {frame.id}.")

asyncio.run(seed())
