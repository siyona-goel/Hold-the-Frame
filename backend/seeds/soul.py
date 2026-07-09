import asyncio
from sqlalchemy import select, delete
from app.database import AsyncSessionLocal
from app.models.models import Movie, Frame, Annotation, PaletteColor, AnnotationCategory, FrameImage

MOVIE = {
    "title": "Soul",
    "year": 2020,
    "studio": "Pixar Animation Studios",
    "cover_image_url": "https://res.cloudinary.com/dycmsdxhi/image/upload/v1783526851/soul_ppylly.jpg",
    "slug": "soul",
    "annotation_color": "#3d4968"
}

FRAMES = [
    {
        "display_order": 0,
        "image_url": "https://res.cloudinary.com/dycmsdxhi/image/upload/v1783526887/s1_vft6te.png",
        "timestamp_label": "10:09",
        "description": "Joe falling through the universe",
        "images": [],
        "annotations": [
            {
                "x_position": 12.6,
                "y_position": 25.3,
                "content": "I watched this scene with my brother, and he said, 'Oh, this isn't like Disney's usual style.' And the thing is, it's true. I think the visual arts and animation techniques used throughout this film are so different from classic Disney films, and it's refreshing. What interested me the most was the blend of 2D and 3D. In some scenes, the characters are 2D in a 3D space (like the Jerries and Terry), and in others, characters move between 3D and 2D spaces, with 2D animation techniques used during their movement, to signify transitions and moving between layers of the universe. The scene this frame is taken from is an example of the latter.",
                "category": AnnotationCategory.general,
            },
            {
                "x_position": 72.4,
                "y_position": 53.5,
                "content": "curious, confused, helplessness",
                "category": AnnotationCategory.emotion,
            },
            {
                "x_position": 82.0,
                "y_position": 3.9,
                "content": "Depersonalization, Existential dread and helplessness",
                "category": AnnotationCategory.theme,
            },
            {
                "x_position": 43.6,
                "y_position": 39.3,
                "content": "Chronophotography: Observe the trails of Joe's body and face. Chronophotography was a 19th century photographic technique that captured multiple phases of movement in a single frame. Pixar could have used the usual digital motion blur, but using this technique made it feel like time has slowed down, or that its notion doesn't even exist. It makes the viewers feel like Joe is trapped between dimensions, unable to move forward smoothly.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 24.0,
                "y_position": 55.7,
                "content": "Chiaroscuro: Pixar strips away texture, complex lighting, and volumetric atmospheres to leave only the high contrast white lines against an absolute black void. The lack of an environment creates an existential isolation that lets us experience the same weightlessness and loss of control that Joe feels.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 48.6,
                "y_position": 61.7,
                "content": "(Subverted) Squash & Stretch, and Appeal: Joe's forms lack organic flexibility here. Also, instead of making him look compelling, he looks distorted and kind of creepy. By using the opposite of these standard animation principles, the scene feels vulnerable and nightmare-ish. He's being controlled by a dimension he doesn't understand, and we're scared for him too.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 48.7,
                "y_position": 38.7,
                "content": "Timing: The spacing between Joe's trailing 'selves' is compressed and uneven, with a staccato style timing. This disrupts the viewers' visual expectations and makes the fall feel disorienting and induces a feeling of vertigo.",
                "category": AnnotationCategory.technique,
            },
        ],
        "palette_colors": [
            {"hex_value": "#010101ff", "display_order": 0},
            {"hex_value": "#090909ff", "display_order": 1},
            {"hex_value": "#272727ff", "display_order": 2},
            {"hex_value": "#3C3C3Cff", "display_order": 3},
            {"hex_value": "#F5F5F7ff", "display_order": 4},
        ],
    },
    {
        "display_order": 1,
        "image_url": "https://res.cloudinary.com/dycmsdxhi/image/upload/v1783526885/s2_spm91d.jpg",
        "timestamp_label": "18:14",
        "description": "Terry searching through the file cabinets",
        "images": [],
        "annotations": [
            {
                "x_position": 9.7,
                "y_position": 75.0,
                "content": "What caught my eye here was the contrast between Terry's flat, almost two-dimensional appearance and his ability to interact seamlessly with three-dimensional objects like the file cabinet. His design makes it seem like he shouldn't even be something 'solid' with a physical presence. I also appreciated the realism in the animation, particularly the way his fingers rapidly flick through the files. It adds a convincing sense of weight, speed, and dexterity that enhances the scene.",
                "category": AnnotationCategory.general,
            },
            {
                "x_position": 66.0,
                "y_position": 5.3,
                "content": "amusing, suspense",
                "category": AnnotationCategory.emotion,
            },
            {
                "x_position": 61.2,
                "y_position": 95.6,
                "content": "Bureaucracy of existence",
                "category": AnnotationCategory.theme,
            },
            {
                "x_position": 81.0,
                "y_position": 78.7,
                "content": "Dimensional Contrast: Terry is animated as a single, continuous 2D neon line, while the filing cabinets and folders are modeled with realistic 3D depth, texture, and volumetric shadows. Due to this, without them having to tell us explicitly, we know that Terry does not conform to the standard physical laws we are used to.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 34.9,
                "y_position": 65.7,
                "content": "Lighting: Terry emits a distinct neon glow. Observe how his light casts a soft illumination onto the edges of the individual file folders inside the drawer and on the cabinet at the back. Mixing 2D with 3D is not easy, and can easily result in the animation looking cheap. The interactive lighting here grounds Terry just enough to make the interaction feel tactile and real.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 86.6,
                "y_position": 45.3,
                "content": "Silhouette: Terry is literally just a line. He has no detail at all. Every pose of his must be readable from his outer line alone. The little adjustments in his silhouette, like the dent below his ear, creates the effect of a hunched sloping posture. (It's also interesting how little it takes for our brain to perceive and infer a full image.) The posture convey's Terry's intense focus and bureaucratic determination, and of course makes the scene all the more funny.",
                "category": AnnotationCategory.technique,
            },
        ],
        "palette_colors": [
            {"hex_value": "#09090Bff", "display_order": 0},
            {"hex_value": "#33405Aff", "display_order": 1},
            {"hex_value": "#5A7A96ff", "display_order": 2},
            {"hex_value": "#516174ff", "display_order": 3},
            {"hex_value": "#CABCCDff", "display_order": 4},
        ],
    },
    {
        "display_order": 2,
        "image_url": "https://res.cloudinary.com/dycmsdxhi/image/upload/v1783526886/s3_t26iug.png",
        "timestamp_label": "56:33",
        "description": "Terry accidently traps Paul",
        "images": [],
        "annotations": [
            {
                "x_position": 17.7,
                "y_position": 13.5,
                "content": "This is the only scene in the film where three entirely different visual languages coexist in a single frame. There's the human reality, with its anatomy and clothing (though stripped of color). There's the soul with its distinct style and soft glow, and then there's Terry, the abstract, higher-dimensional, mathematical reality. The cinematic experience of this scene literally gave me goosebumps.",
                "category": AnnotationCategory.general,
            },
            {
                "x_position": 39.9,
                "y_position": 25.8,
                "content": "vulnerable, tension, exposure",
                "category": AnnotationCategory.emotion,
            },
            {
                "x_position": 59.2,
                "y_position": 81.3,
                "content": "Depersonalization, Insignificance of the ego",
                "category": AnnotationCategory.theme,
            },
            {
                "x_position": 70.4,
                "y_position": 16.1,
                "content": "Dimensional Contrast: Terry is a flat continuous line as opposed to the other two. At the start it slightly confuses viewers because it messes up our sense of environment and space, but then evolves to be the main visual interest of the scene.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 28.8,
                "y_position": 40.9,
                "content": "Chiaroscuro and Color Desaturation: The color story in this frame is deliberate. Desaturating Paul visually communicates his loss of power. The bright, concentrated light of Terry and Paul's soul draws the audience's eyes instantly to the center of the conflict, using lighting to dictate the narrative focus.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 78.4,
                "y_position": 52.7,
                "content": "Dynamic Contrast in Posing: In animation, diagonal lines imply motion and instability, while vertical lines imply power and immobility. So Paul's tilted, diagonal angle, as opposed to Terry's perfectly upright and sharp stance emphasizes Terry's power over the situation.",
                "category": AnnotationCategory.technique,
            },
        ],
        "palette_colors": [
            {"hex_value": "#17181Bff", "display_order": 0},
            {"hex_value": "#515455ff", "display_order": 1},
            {"hex_value": "#333F5Dff", "display_order": 2},
            {"hex_value": "#A4B4D1ff", "display_order": 3},
            {"hex_value": "#73D0B8ff", "display_order": 4},
        ],
    },
    {
        "display_order": 3,
        "image_url": "https://res.cloudinary.com/dycmsdxhi/image/upload/v1783526885/s4_vlix5e.png",
        "timestamp_label": "1:24:57",
        "description": "Joe's soul versus monster Joe",
        "images": [],
        "annotations": [
            {
                "x_position": 85.3,
                "y_position": 77.8,
                "content": "This scene had me in an absolute chokehold. It was so heartbreaking. There's just something about animated movies touching upon deeper issues related to mental health. If you look at the scene carefully you'll realize that Joe's figure is much more defined and larger compared to the other figures that are taunting 22, telling us how much deeper his words cut her. Pixar did such a good job here using color and texture to depict what thoughts of self-doubt feel like in one's head. The climax of the flim, in my opinion.",
                "category": AnnotationCategory.general,
            },
            {
                "x_position": 12.7,
                "y_position": 56.0,
                "content": "fear, vulnerable, helplessness, guilt",
                "category": AnnotationCategory.emotion,
            },
            {
                "x_position": 78.1,
                "y_position": 11.3,
                "content": "The weaponization of words",
                "category": AnnotationCategory.theme,
            },
            {
                "x_position": 29.0,
                "y_position": 44.3,
                "content": "Monster uplighting and Chiaroscuro: The entire scene is bathed in an oppressive, ink-black darkness, with the only primary light source emanating from the tiny glowing soul of Joe below. This creates dramatic uplighting across monster Joe's face. It turns a familiar, friendly mentor figure into a horror villain, mimicking the terrifying distortion of a nightmare.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 46.8,
                "y_position": 71.5,
                "content": "Staging: The principles of staging and size contrast have been pushed to their extremities. It forces viewers to adopt 22's psychological perspective, emphasizing how a seemingly meaningless statement said by Joe fuelled her self-doubt and insecurity so much that it reduced Joe's memory to this kind of a monster.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 37.2,
                "y_position": 40.6,
                "content": "Textures: Giant Joe seems to be made of a dark, soot-like substance. This unstable texture makes his figure feel stagnant, corrupted, and almost dirty. It visually represents being stuck, like how obsession and anxiety pile up until they form a suffocating, rigid shell.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 58.4,
                "y_position": 38.5,
                "content": "Subverted character design: Joe's physical appearance is the same here, except his warm expressions were stripped away and his posture is this really weird predatory kind of bend. Keeping his recognizable silhouette but warping his body language makes this scene much more emotional and shows how a symbol of safety can instantly twist into a symbol of trauma in somebody's head.",
                "category": AnnotationCategory.technique,
            },
        ],
        "palette_colors": [
            {"hex_value": "#0D0D0D", "display_order": 0},
            {"hex_value": "#011526", "display_order": 1},
            {"hex_value": "#03318C", "display_order": 2},
            {"hex_value": "#064973", "display_order": 3},
            {"hex_value": "#44A4A4", "display_order": 4},
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
