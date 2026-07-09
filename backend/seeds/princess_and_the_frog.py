import asyncio
from sqlalchemy import select, delete
from app.database import AsyncSessionLocal
from app.models.models import Movie, Frame, Annotation, PaletteColor, AnnotationCategory, FrameImage

# ══════════════════════════════════════════════════════════════════════════════
# THE PRINCESS AND THE FROG — full seed
# Run this file any time you update anything about this movie.
# It is safe to rerun — it upserts the movie and frames, and fully
# replaces all annotations and palette colors on each run.
# ══════════════════════════════════════════════════════════════════════════════

MOVIE = {
    "title": "The Princess and the Frog",
    "year": 2009,
    "studio": "Walt Disney Animation Studios",
    "cover_image_url": "https://res.cloudinary.com/dycmsdxhi/image/upload/v1782737801/the_princess_and_the_frog_xveljl.jpg",
    "slug": "princess-and-the-frog",
    "annotation_color": "#C17F24",
}

FRAMES = [
    {
        "display_order": 0,
        "image_url": "https://res.cloudinary.com/dycmsdxhi/image/upload/v1782799409/frame-1_gpviz1.png",
        "timestamp_label": "04:45",
        "description": "Community eating gumbo scene",
        "images": [],
        "annotations": [
            {
                "x_position": 6.9,
                "y_position": 10.0,
                "content": "happy, nostalgic",
                "category": AnnotationCategory.emotion,
            },
            {
                "x_position": 69.8,
                "y_position": 25.0,
                "content": "Community, comfort, simplicity & contentment",
                "category": AnnotationCategory.theme,
            },
            {
                "x_position": 47.9,
                "y_position": 21.6,
                "content": "Backlighting: The halo effect around the family draws the viewer's eye immediately to the focal point of the shot.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 26.9,
                "y_position": 19.8,
                "content": "Chiaroscuro: The idea of a warm loving home comes from the cozy frame created by the contrast between the muted blue-gray tones of the night and the golden-yellow interior light.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 50.0,
                "y_position": 68.9,
                "content": "Layered Composition: Closely mimics the depth achieved by a physical multiplane camera. Gives a 2D animation scene a sense of 3D space.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 16.4,
                "y_position": 41.9,
                "content": "Tapering: Gives the characters an organic, fluid feel",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 29.1,
                "y_position": 81.7,
                "content": "This is the first scene in the movie (although there are many more to come) that gives viewers a warm, fuzzy feeling inside. I spent some time observing the differences between the people, but the one thing that's the same is their smile. That seriously must be some delicious gumbo. The scene perfectly portrays the intended 'united by food' idea they want to convey to their viewers. ",
                "category": AnnotationCategory.general,
            },
        ],
        "palette_colors": [
            {"hex_value": "#140D09ff", "display_order": 0},
            {"hex_value": "#3C251Dff", "display_order": 1},
            {"hex_value": "#9A5B05ff", "display_order": 2},
            {"hex_value": "#F5A51Eff", "display_order": 3},
            {"hex_value": "#F2F826ff", "display_order": 4},
        ],
    },
    {
        "display_order": 1,
        "image_url": "https://res.cloudinary.com/dycmsdxhi/image/upload/v1782799409/frame-2_takrtp.png",
        "timestamp_label": "13:02",
        "description": "Tiana in her restaurant",
        "images": [],
        "annotations": [
            {
                "x_position": 50.0,
                "y_position": 48.0,
                "content": "I think the artistry of this clip is genius. An embodiment of the phrase, 'A ray of hope'. Tiana looks so small amidst the shambles of her to-be restaurant, but it's as if her spirit fills the room. The sunlight on her, with the white birds flying off into the sun (traditionally a symbol of hope and transcendence) really makes viewers feel like she's about to get a new beginning (I guess clichés work sometimes).",
                "category": AnnotationCategory.general,
            },
            {
                "x_position": 19.0,
                "y_position": 93.2,
                "content": "hopeful",
                "category": AnnotationCategory.emotion,
            },
            {
                "x_position": 73.6,
                "y_position": 52.5,
                "content": "Potential in the broken, the scale of ambition",
                "category": AnnotationCategory.theme,
            },   
            {
                "x_position": 39.6,
                "y_position": 27.1,
                "content": "God Rays: The heavy rays act as a spotlight that seem to validate Tiana's dreams",
                "category": AnnotationCategory.technique,
            },  
            {
                "x_position": 54.5,
                "y_position": 71.1,
                "content": "Chiaroscuro: Dramatic contrast immediately anchors the viewer's eye right onto Tiana",
                "category": AnnotationCategory.technique,
            },       
            {
                "x_position": 47.3,
                "y_position": 85.2,
                "content": "Extreme Wide Shot: The extreme wide angle with sharp, deep perspective lines draw focus directly to Tiana, making her the epicenter of the environment.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 21.3,
                "y_position": 52.3,
                "content": "Hand Painted Textures: The grit, grain, and weathered texture of the wood remains visible. This keeps the scene grounded in reality. If the background were too slick or perfectly digital, the emotional weight of Tiana's hard work and gritty reality would be lost.",
                "category": AnnotationCategory.technique,
            },
        ],
        "palette_colors": [
            {"hex_value": "#1C0E02ff", "display_order": 0},
            {"hex_value": "#331800ff", "display_order": 1},
            {"hex_value": "#4D2B0Eff", "display_order": 2},
            {"hex_value": "#764416ff", "display_order": 3},
            {"hex_value": "#F2AB70ff", "display_order": 4},
        ],
    },
    {
        "display_order": 2,
        "image_url": "https://res.cloudinary.com/dycmsdxhi/image/upload/v1782799408/frame-3_lcmkpg.png",
        "timestamp_label": "19:03",
        "description": "Naveen and the voodoo room",
        "images": [],
        "annotations": [
            {
                "x_position": 26.5,
                "y_position": 59.8,
                "content": "I guess I'm a sucker for high-contrast frames that are in the one-point perspective, but it's also rare that an animated scene gives me (the scared kind of) goosebumps. What amazes me is that this frame lets viewers see the insides of a dark room with such detail even from the corners of their eyes, while their focus remains at the center. Stared at the detailing of this frame for at least 10 mins.",
                "category": AnnotationCategory.general,
            },
            {
                "x_position": 70.4,
                "y_position": 18.2,
                "content": "fear, anticipation",
                "category": AnnotationCategory.emotion,
            },
            {
                "x_position": 56.6,
                "y_position": 79.9,
                "content": "Deception, intrusion, vulnerability",
                "category": AnnotationCategory.theme,
            },
            {
                "x_position": 53.1,
                "y_position": 53.5,
                "content": "Backlighting: Turning the two characters mostly into silhouettes forces viewers to focus on their posture and body language instead of their facial expressions.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 30.5,
                "y_position": 21.1,
                "content": "Staging: The animators use the low-hanging, jagged fabrics at the top of the screen and the dark furniture on the left and right to form a heavy, constricting 'frame' around the lit up doorway. It helps direct our eye, but also makes us feel like we're the one hiding in the corners of the room.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 44.1,
                "y_position": 56.0,
                "content": "Chiaroscuro: Purple and magenta are used throughout the film to depict dark voodoo magic. Using this effect between those colors and the soft sunset orange creates an eerie atmosphere that makes viewers feel nervous, just as the characters feel.",
                "category": AnnotationCategory.technique,
            },
        ],
        "palette_colors": [
            {"hex_value": "#170E09ff", "display_order": 0},
            {"hex_value": "#3D1F26ff", "display_order": 1},
            {"hex_value": "#AF6687ff", "display_order": 2},
            {"hex_value": "#AF715Bff", "display_order": 3},
            {"hex_value": "#FEB369ff", "display_order": 4},
        ],
    },
    {
        "display_order": 3,
        "image_url": "https://res.cloudinary.com/dycmsdxhi/image/upload/v1782799409/frame-4_tzmwtj.png",
        "timestamp_label": "48:00",
        "description": "Nighttime fireflies in the bayou scene",
        "images": [],
        "annotations": [
            {
                "x_position": 84.4,
                "y_position": 11.6,
                "content": "When I first watched this part as a child, Disney convinced me to turn into a frog and live in a swamp. Despite obviously being magical looking, this scene felt deeper for me because it convinced me there's beauty in everything. Even in the darkest of situations, you remain grounded through beauty. Another scene causing the warm, fuzzy feeling inside. Also, some aspects of it resemble the lanterns scene from Tangled.",
                "category": AnnotationCategory.general,
            },
            {
                "x_position": 87.9,
                "y_position": 78.5,
                "content": "in awe, excitement, warm",
                "category": AnnotationCategory.emotion,
            },
            {
                "x_position": 57.8,
                "y_position": 74.9,
                "content": "Community, the magic within the mundane",
                "category": AnnotationCategory.theme,
            },
            {
                "x_position": 10.4,
                "y_position": 49.1,
                "content": "Staging: The trees on the left and right act as natural curtains that force the viewers' eyes towards the center. The fireflies act as a visual arrows. It's like their reflection in the water purposely points us towards the frog couple.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 42.2,
                "y_position": 59.2,
                "content": "Arcs: A large part of the magic is owed to the organic, sweeping arcs of the animated fireflies. Their collective movement mimics that of the wind and enhances the magic of the bayou.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 31.6,
                "y_position": 85.1,
                "content": "Secondary Action: The real intention of this scene was probably to depict the budding romance between Tiana and Naveen. The secondary action of the glowing fireflies around them is what actually leads to this emotional gravity.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 58.9,
                "y_position": 28.9,
                "content": "Appeal: The extreme contrast between the tiny frogs and the immensity of the swamp gives this frame its sense of scale and charm.",
                "category": AnnotationCategory.technique,
            },
        ],
        "palette_colors": [
            {"hex_value": "#0E120Aff", "display_order": 0},
            {"hex_value": "#43370Aff", "display_order": 1},
            {"hex_value": "#86680Fff", "display_order": 2},            
            {"hex_value": "#FFE061ff", "display_order": 4},
            {"hex_value": "#787500ff", "display_order": 3},            
        ],
    },
    {
        "display_order": 4,
        "image_url": "https://res.cloudinary.com/dycmsdxhi/image/upload/v1782805459/frame-5_b_a20nqu.png",
        "timestamp_label": "1:00:35",
        "description": "Mama Odie's entrance",
        "images": [
            {"image_url": "https://res.cloudinary.com/dycmsdxhi/image/upload/v1782805459/frame-5_b_a20nqu.png", "is_primary": True, "display_order": 0},
            {"image_url": "https://res.cloudinary.com/dycmsdxhi/image/upload/v1782799409/frame-5_a_camz3z.png", "is_primary": False, "display_order": 1},
        ],
        "annotations": [
            {
                "x_position": 59.7,
                "y_position": 7.1,
                "content": "I think the buildup on seeing what Mama Odie looks like is so real. She's described so many times in such a scary manner before this scene, so Disney obviously had to apply the classical bait-and-switch. Her cute little waddle coupled with the flaming torch gives fairy godmother - without the fairy I guess.",
                "category": AnnotationCategory.general,
            },
            {
                "x_position": 9.6,
                "y_position": 88.5,
                "content": "suspense, excitement",
                "category": AnnotationCategory.emotion,
            },{
                "x_position": 92.9,
                "y_position": 48.5,
                "content": "Appearance vs. Reality, Wisdom in Eccentricity",
                "category": AnnotationCategory.theme,
            },
            {
                "x_position": 42.4,
                "y_position": 67.1,
                "content": "Exaggeration: The wild distortion between the huge, beastly shadow and its corresponding tiny, round woman creates the scene's comedic punchline.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 6.9,
                "y_position": 27.1,
                "content": "Staging: The massive shadow is placed dead-center and fills up such a large part of the frame which causes the sense of intimidation and focus. When the light cuts through, the staging draws viewers' eyes straight to Mama Odie.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 67.6,
                "y_position": 73.7,
                "content": "Arcs, and Ease-in, Ease-out: The golden light trail of Mama Odie's magical staff is animated along a prefect fluid arc, and the trail continues to move for a bit when the staff stops moving. The movement feels graceful and organic, rather than rigid or mechanical.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 82.9,
                "y_position": 75.3,
                "content": "Timing: The comedic timing of this reveal is immaculate. The slow, heavy, menacing movement of the giant silhouette builds suspense, which is instantly broken by a fast, energetic burst of movement and light as Mama Odie pops into view.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 31.5,
                "y_position": 69.5,
                "content": "Atmospheric Scale Trickery: Mama Odie's silhouette is completely dark and blurred by the mist. Our brain lacks the spatial cues needed to judge distance. By placing a tiny character close to the light source in the fog, her shadow appears monstrous.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 79.5,
                "y_position": 62.5,
                "content": "High Contrast: The color palette explodes with warm golden-yellow and white amidst the eerie blue when Mama Odie pops out. A large part of us being able to gauge her personality is owing to this color contrast.",
                "category": AnnotationCategory.technique,
            },
        ],
        "palette_colors": [
            {"hex_value": "#212E54ff", "display_order": 0},
            {"hex_value": "#062E54ff", "display_order": 1},
            {"hex_value": "#444D96ff", "display_order": 2},
            {"hex_value": "#788DE8ff", "display_order": 3},
            {"hex_value": "#0194EDff", "display_order": 4},
        ],
    },
    {
        "display_order": 5,
        "image_url": "https://res.cloudinary.com/dycmsdxhi/image/upload/v1782895429/frame-6_kqdg9d.jpg",
        "timestamp_label": "1:05:39",
        "description": "Dig a little deeper",
        "images": [],
        "annotations": [
            {
                "x_position": 21.2,
                "y_position": 71.1,
                "content": "I love the transformation of boat treehouse to concert arena. The music, the lighting, the art, all contribute so perfectly to create a dramatic shift in the vibe. For a brief minute, I as a viewer too forgot about the little frogs's problems (and some of mine too).",
                "category": AnnotationCategory.general,
            },
            {
                "x_position": 52.1,
                "y_position": 76.2,
                "content": "happy, hopeful, energized",
                "category": AnnotationCategory.emotion,
            },
            {
                "x_position": 71.8,
                "y_position": 21.4,
                "content": "Wisdom in eccentricity, community, the magic within the mundane",
                "category": AnnotationCategory.theme,
            },
            {
                "x_position": 48.2,
                "y_position": 61.0,
                "content": "Backlighting: The severity of this technique in this frame creates a rim light around Mama Odie, making her stand out as the magic's orchestrator.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 78.2,
                "y_position": 28.6,
                "content": "Staging: The frame utilizes a symmetrical composition, with Mama Odie placed at the lower-center apex. The lines of flamingos pointing inwards act like arrows, telling viewers exactly where to look.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 30.4,
                "y_position": 16.2,
                "content": "Chiaroscuro & Appeal: The scene is able to mimic the real-world optical effect of an overexposed camera lens tracking intense light. We must appreciate the level of detail here. Notice the color changes in the rays of light as they pass through the colored bottles.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 73.6,
                "y_position": 58.7,
                "content": "Graphic shape language: The bottles, the stylized ripples of light, and the exaggerated curves of the branches makes the place feel less like a swamp and more like a place of enlightenment and emotion.",
                "category": AnnotationCategory.technique,
            },
        ],
        "palette_colors": [
            {"hex_value": "#4E241Dff", "display_order": 0},
            {"hex_value": "#803830ff", "display_order": 1},
            {"hex_value": "#A67176ff", "display_order": 2},
            {"hex_value": "#EFDAA7ff", "display_order": 3},
            {"hex_value": "#F5F5F3ff", "display_order": 4},
        ],
    },
]


async def seed():
    async with AsyncSessionLocal() as session:
        async with session.begin():

            # ── Upsert movie ──────────────────────────────────────────────────
            result = await session.execute(
                select(Movie).where(Movie.slug == MOVIE["slug"])
            )
            movie = result.scalar_one_or_none()

            if movie:
                # Update existing movie fields in case anything changed
                movie.title = MOVIE["title"]
                movie.year = MOVIE["year"]
                movie.studio = MOVIE["studio"]
                movie.cover_image_url = MOVIE["cover_image_url"]
                movie.annotation_color = MOVIE["annotation_color"]
                print(f"Updated movie: {movie.title}")
            else:
                movie = Movie(**MOVIE)
                session.add(movie)
                await session.flush()  # get movie.id before using it
                print(f"Created movie: {movie.title}")

            # ── Upsert frames + replace annotations and palette colors ─────────
            for frame_data in FRAMES:
                result = await session.execute(
                    select(Frame).where(
                        Frame.movie_id == movie.id,
                        Frame.display_order == frame_data["display_order"]
                    )
                )
                frame = result.scalar_one_or_none()

                if frame:
                    # Update existing frame fields
                    frame.image_url = frame_data["image_url"]
                    frame.timestamp_label = frame_data["timestamp_label"]
                    frame.description = frame_data["description"]
                else:
                    frame = Frame(
                        movie_id=movie.id,
                        image_url=frame_data["image_url"],
                        timestamp_label=frame_data["timestamp_label"],
                        description=frame_data["description"],
                        display_order=frame_data["display_order"],
                    )
                    session.add(frame)
                    await session.flush()  # get frame.id before using it

                # Always wipe and reinsert annotations and palette colors
                await session.execute(
                    delete(Annotation).where(Annotation.frame_id == frame.id)
                )
                await session.execute(
                    delete(PaletteColor).where(PaletteColor.frame_id == frame.id)
                )

                session.add_all([
                    Annotation(
                        frame_id=frame.id,
                        x_position=a["x_position"],
                        y_position=a["y_position"],
                        content=a["content"],
                        category=a["category"],
                    )
                    for a in frame_data["annotations"]
                ])

                session.add_all([
                    PaletteColor(
                        frame_id=frame.id,
                        hex_value=c["hex_value"],
                        display_order=c["display_order"],
                    )
                    for c in frame_data["palette_colors"]
                ])

                # Wipe and reinsert frame images
                await session.execute(
                    delete(FrameImage).where(FrameImage.frame_id == frame.id)
                )

                session.add_all([
                    FrameImage(
                        frame_id=frame.id,
                        image_url=img["image_url"],
                        is_primary=img["is_primary"],
                        display_order=img["display_order"],
                    )
                    for img in frame_data.get("images", [])
                ])

                print(f"  Frame {frame_data['display_order']}: "
                      f"{len(frame_data['annotations'])} annotations, "
                      f"{len(frame_data['palette_colors'])} colors")

            print("Done.")

asyncio.run(seed())
