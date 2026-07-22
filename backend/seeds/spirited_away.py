import asyncio
from sqlalchemy import select, delete
from app.database import AsyncSessionLocal
from app.models.models import Movie, Frame, Annotation, PaletteColor, AnnotationCategory, FrameImage

MOVIE = {
    "title": "Spirited Away",
    "year": 2001,
    "studio": "Studio Ghibli",
    "cover_image_url": "https://res.cloudinary.com/dycmsdxhi/image/upload/v1784566353/spirited_away_yf4vy1.jpg",
    "slug": "spirited-away",
    "annotation_color": "#8a362d"
}

FRAMES = [
    {
        "display_order": 0,
        "image_url": "https://res.cloudinary.com/dycmsdxhi/image/upload/v1784566088/sa1_hmh66t.png",
        "timestamp_label": "12:00",
        "description": "Chihiro discovers the spirit world",
        "images": [],
        "annotations": [
            {
                "x_position": 72.4,
                "y_position": 62.8,
                "content": "This scene serves as an 'enlightenment' scene for the viewers, finally giving them an idea of the situation and space Chihiro has plunged herself into. The artistic choice of displaying the spirits here as these see-through, shadowy figures, with just 2 soft white dots for eyes, emphasizes their lack of visual identity.",
                "category": AnnotationCategory.general,
            },
            {
                "x_position": 44.2,
                "y_position": 15.3,
                "content": "fear, confusion",
                "category": AnnotationCategory.emotion,
            },
            {
                "x_position": 11.8,
                "y_position": 15.1,
                "content": "Entering the Unknown, Fear of the Unseen, Loss of Control, Crossing Between Worlds",
                "category": AnnotationCategory.theme,
            },
            {
                "x_position": 31.8,
                "y_position": 37.6,
                "content": "The colors of the environment in this frame - the glowing reds, the warm yellows, the wooden browns - create a typically inviting setting. But we know that Chihiro is terrified. This emotional contradiction is powerful because the setting looks welcoming while feeling deeply unsettling. For example, if the background was lit in cold blue or gray tones, the scene would feel like a horror film, and the spirits would seem threatening instead of mysterious. Chihiro's fear would feel validated by its environment.",
                "category": AnnotationCategory.color,
            },
            {
                "x_position": 49.9,
                "y_position": 79.8,
                "content": "Perspective: Every architectural line converges toward the center of the frame. The one-point perspective here creates a strong sense of depth and pulls the viewer's attention toward Chihiro.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 75.2,
                "y_position": 15.9,
                "content": "Staging: The market stalls on both sides act as natural frames. Instead of placing Chihiro in an empty street, the architecture encloses her, making it feel like the world is closing in around her.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 59.0,
                "y_position": 47.3,
                "content": "Layered Composition: It makes the marketplace setting feel expansive and lived-in by these spirits.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 53.8,
                "y_position": 72.5,
                "content": "Appeal: Chihiro's running pose clearly communicates fear. Even as a still frame, her silhouette conveys urgency and uncertainty.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 85.6,
                "y_position": 38.5,
                "content": "Lighting: The lighting here isn't dramatic. But the soft glow of the red lanterns makes the spirit world feel vibrant rather than overtly sinister. This way, Miyazaki does away with horror aesthetics and presents the supernatural as beautiful, lived-in, and mysterious.",
                "category": AnnotationCategory.technique,
            },            
        ],
        "palette_colors": [
            {"hex_value": "#201A13ff", "display_order": 0},
            {"hex_value": "#413B21ff", "display_order": 1},
            {"hex_value": "#5B452Cff", "display_order": 2},
            {"hex_value": "#583427ff", "display_order": 3},
            {"hex_value": "#D8524Cff", "display_order": 4},
        ],
    },
    {
        "display_order": 1,
        "image_url": "https://res.cloudinary.com/dycmsdxhi/image/upload/v1784566088/sa2_wsw8jt.png",
        "timestamp_label": "35:28",
        "description": "Chihiro is pulled by Yubaba",
        "images": [],
        "annotations": [
            {
                "x_position": 96.1,
                "y_position": 46.5,
                "content": "I found this scene very visually appealing. The smooth animation of Chihiro sliding across magnificent hallways, with such body language, implying how little (technically zero) control she has over her own body in the current situation. It creates this tense feeling, because nothing inherently dangerous happens to her before this scene, so it's as if we are suddenly reminded of how she is solely at the mercy of these powerful beings that she is now surrounded by.",
                "category": AnnotationCategory.general,
            },
            {
                "x_position": 33.5,
                "y_position": 2.8,
                "content": "fear, surprise, confusion, anticipation",
                "category": AnnotationCategory.emotion,
            },
            {
                "x_position": 10.7,
                "y_position": 70.7,
                "content": "Loss of Agency, Vulnerability",
                "category": AnnotationCategory.theme,
            },
            {
                "x_position": 58.8,
                "y_position": 40.1,
                "content": "I like how this film uses shadows to evoke uncertainty. The audience doesn't fear what they see—they fear what they can't see.",
                "category": AnnotationCategory.composition,
            },
            {
                "x_position": 49.6,
                "y_position": 76.9,
                "content": "Perspective: The whole frame leads to a central vanishing point. The walls, the carpet, the ceiling, all converge into darkness ahead. This creates a powerful sense of inevitability. There is visually only one direction to travel. So even if Chihiro weren't present, the viewer's eye would naturally be pulled forward.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 57.4,
                "y_position": 59.5,
                "content": "Staging and Exaggeration: Chihiro's expressive pose is enough to tell the story here. Her limbs are stretched backwards, while her body leans towards the force pulling her. Thus her pose alone is enough to understand the action taking place.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 30.7,
                "y_position": 30.3,
                "content": "Chiaroscuro: The bright highlights on the ornate walls frame the much darker center of the corridor, naturally directing the viewer's attention toward Chihiro and the path ahead. It helps the audience feel the same uncertainty as Chihiro, building anticipation for her first encounter with Yubaba.",
                "category": AnnotationCategory.technique,
            },
        ],
        "palette_colors": [
            {"hex_value": "#19100Cff", "display_order": 0},
            {"hex_value": "#5B2F1Cff", "display_order": 1},
            {"hex_value": "#935721ff", "display_order": 2},
            {"hex_value": "#D3A15Cff", "display_order": 3},
            {"hex_value": "#62581Fff", "display_order": 4},
        ],
    },
    {
        "display_order": 2,
        "image_url": "https://res.cloudinary.com/dycmsdxhi/image/upload/v1784566088/sa3_x2932n.png",
        "timestamp_label": "53:26",
        "description": "No Face enters the bathhouse",
        "images": [],
        "annotations": [
            {
                "x_position": 10.8,
                "y_position": 40.8,
                "content": "This scene gave me goosebumps. Before this scene, Chihiro has essentially no interaction with No Face. The sudden jump from that, to her inviting No Face into the bathhouse, felt like a largely intimate jump. Plus No Face's visual appearance is what one would call 'creepy', so the visual contrast between it and the warm nature of the bathhouse is enough to get the audience feeling like something bad is going to happen.",
                "category": AnnotationCategory.general,
            },
            {
                "x_position": 56.4,
                "y_position": 7.4,
                "content": "dread, anticipation",
                "category": AnnotationCategory.emotion,
            },
            {
                "x_position": 90.4,
                "y_position": 63.4,
                "content": "Compassion without Judgement",
                "category": AnnotationCategory.theme,
            },
            {
                "x_position": 14.3,
                "y_position": 92.0,
                "content": "Negative Space: Most of this frame is an empty hallway. It helps emphasize No Face's solitude, creates anticipation, and makes his quiet entrance feel significant rather than dramatic. Due to the lack of visual clutter, we are able to focus on this one single action.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 35.0,
                "y_position": 23.6,
                "content": "Vertical Contrast and Grid Composition: Most of the architecture is composed of horizontal and vertical lines. No-Face, however, is almost a single uninterrupted black column. His silhouette immediately stands out, breaking the visual rhythm and immediately drawing the viewer's eyes towards him.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 59.0,
                "y_position": 35.0,
                "content": "Minimal Character Design: No Face's simplicity makes him visually iconic. Because there are so few details, the viewer projects emotion onto his posture and mask rather than expressive facial features.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 83.4,
                "y_position": 22.3,
                "content": "Staging: No Face could have been placed in the center of the frame, but he is deliberately placed towards the right, while the long corridor stretches empty to the left. This imbalance is meant to create a feeling of something foreign entering the scene, rather than already belonging within it.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 48.4,
                "y_position": 80.4,
                "content": "Layered Composition: The image contains multiple visual layers: the hallway in the foreground, the sliding doors, No-Face in the doorway, and the garden outside. These layers create depth while reinforcing the act of crossing boundaries.",
                "category": AnnotationCategory.technique,
            },
        ],
        "palette_colors": [
            {"hex_value": "#010302ff", "display_order": 0},
            {"hex_value": "#281E17ff", "display_order": 1},
            {"hex_value": "#564738ff", "display_order": 2},
            {"hex_value": "#735630ff", "display_order": 3},
            {"hex_value": "#CDBDA6ff", "display_order": 4},
        ],
    },
    {
        "display_order": 3,
        "image_url": "https://res.cloudinary.com/dycmsdxhi/image/upload/v1784566087/sa4_copkjk.png",
        "timestamp_label": "01:09:16",
        "description": "No Face eats a frog",
        "images": [],
        "annotations": [
            {
                "x_position": 18.8,
                "y_position": 45.0,
                "content": "This caught me SO off guard. Before this, the viewers are exposed to only a single kind, yet confusing interaction between Chihiro and No Face, so naturally we are led to believe that No Face is a good, 'harmless' spirit. This scene was so unexpected that I screamed, and felt quite betrayed. In fact, my face looked exactly like that of the frog's in this screenshot.",
                "category": AnnotationCategory.general,
            },
            {
                "x_position": 92.6,
                "y_position": 42.0,
                "content": "About No Face: Unlike the other spirits in the film, No Face isn't based on an existing Japanese figure, and was Miyazaki's creation. I was quite confused as to what exactly he was, because I didn't grasp why he was good, then bad, and then good again through the course of the film. Turns out it was never about good and bad. He simply just 'is'. No Face is a reflection of the environment he absorbs. When interacting with Chihiro, he absorbed her kindness and gave it back. Similarly, when exposed to greed and consumerism in the bathhouse, he reflected that back as well.",
                "category": AnnotationCategory.general,
            },
            {
                "x_position": 35.3,
                "y_position": 79.8,
                "content": "surprise, fear",
                "category": AnnotationCategory.emotion,
            },
            {
                "x_position": 23.1,
                "y_position": 21.9,
                "content": "Corruption through Greed, Consumption, Loss of Identity, Innocence vs. Predation",
                "category": AnnotationCategory.theme,
            },
            {
                "x_position": 64.0,
                "y_position": 57.0,
                "content": "Black traditionally represents emptiness, mystery, corruption. A white mask represents false innocence or emotional blankness. While the mouth's deep red color emphasizes violence, flesh, and appetite. The restrained use of this red color makes the mouth immediately unsettling.",
                "category": AnnotationCategory.color,
            },
            {
                "x_position": 51.8,
                "y_position": 58.3,
                "content": "Everything points toward the open mouth. The frog is angled toward it. No-Face's hand guides the frog inward. The mouth itself forms the visual destination. The audience's eye follows the exact path the frog is about to take, thus predicting what will happen next.",
                "category": AnnotationCategory.composition,
            },
            {
                "x_position": 8.1,
                "y_position": 42.3,
                "content": "Staging: The frog occupies only a tiny fraction of the frame while No-Face dominates nearly the entire right side. This extreme contrast in scale emphasizes power and helplessness without dialogue. The empty space on the left allows the frog's small figure to stand out even more, increasing its sense of vulnerability.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 50.0,
                "y_position": 24.0,
                "content": "Contrast of the Mask and the Mouth: While the mask is symmetrical and emotionless, the mouth is huge and filled with asymmetrical teeth and fleshy reds. The visual contradiction is disturbing because these two designs don't seem like they should belong to the same character.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 74.6,
                "y_position": 70.1,
                "content": "Negative Space: No Face's body doesn't really have any details, it's just a featureless black silhouette. Miyazaki lets the viewer's imagination fill in the darkness, making No Face seem even more unknowable and eccentric.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 32.2,
                "y_position": 63.0,
                "content": "Freezing the Moment Before Action: The frog hasn't been eaten yet. The frame captures the split second before the inevitable. That anticipation is often more unsettling than showing the action itself because the viewer mentally completes what comes next.",
                "category": AnnotationCategory.technique,
            },
        ],
        "palette_colors": [
            {"hex_value": "#060606ff", "display_order": 0},
            {"hex_value": "#1A1D32ff", "display_order": 1},
            {"hex_value": "#33362Aff", "display_order": 2},
            {"hex_value": "#61663Aff", "display_order": 3},
            {"hex_value": "#6B90A5ff", "display_order": 4},
        ],
    },
    {
        "display_order": 4,
        "image_url": "https://res.cloudinary.com/dycmsdxhi/image/upload/v1784566088/sa5_i2z4dc.png",
        "timestamp_label": "1:40:42",
        "description": "No Face and Chihiro in the train",
        "images": [],
        "annotations": [
            {
                "x_position": 20.3,
                "y_position": 72.9,
                "content": "This is probably one of the best scenes that has ever been animated. It is a prime example of one of Miyazaki's talents: to be able to create a deep emotional effect through composition and atmosphere, without any dialogue involved. Notice how much empty space surrounds Chihiro and No Face in this train. All this negative space creates a feeling that's difficult to describe: not loneliness exactly, but quiet emotional distance. This scene gave its audience permission to simply exist with the characters for a moment.",
                "category": AnnotationCategory.general,
            },
            {
                "x_position": 32.5,
                "y_position": 51.1,
                "content": "One thing I love about Studio Ghibli films is that they give the environment space to breathe. Modern animated movies often cut every few seconds. That's why I often pause them to be able to look at the details of frames closely. In Studio Ghibli films, no pausing is required, because my brain is actually given the time to absorb details like the floor's texture, the reflections in the windows, the way the light shines on the metal poles of the train.",
                "category": AnnotationCategory.general,
            },
            {
                "x_position": 11.6,
                "y_position": 28.6,
                "content": "solitude, safety, momentary peace",
                "category": AnnotationCategory.emotion,
            },
            {
                "x_position": 61.8,
                "y_position": 63.9,
                "content": "Quiet Companionship, Reflection, Liminality",
                "category": AnnotationCategory.theme,
            },
            {
                "x_position": 69.3,
                "y_position": 71.1,
                "content": "The train seats occupy a large amount of the frame. Because the rest of the palette is muted, those deep red cushions pull the audience's attention toward the only occupied area.",
                "category": AnnotationCategory.color,
            },
            {
                "x_position": 67.8,
                "y_position": 23.4,
                "content": "The background is very detailed, but it is not cluttered. The vertical poles create a rhythm, the windows repeat at even intervals, nothing overlaps confusingly. This lets our eyes wander across the frame without getting lost. Good composition comes from organizing detail well.",
                "category": AnnotationCategory.composition,
            },
            {
                "x_position": 52.2,
                "y_position": 77.3,
                "content": "Negative Space: The first noticeable feature of this frame is how much empty space surrounds Chihiro and No Face. It creates a silent feeling of emotional distance between the 2 characters, even though they are seated right next to each other.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 36.5,
                "y_position": 52.1,
                "content": "Perspective: The train is drawn in almost perfect one-point perspective. This guides the viewers eyes through the entire carriage before landing on Chihiro and No-Face. Since the characters are not centered, we first get to appreciate the environment before noticing the people (or spirits) in it.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 11.8,
                "y_position": 10.4,
                "content": "Color Contrast: The train is built on warm oranges and wooden browns, while the outside world is made up of blues and purples. This makes the train feel like a tiny pocket of warmth floating through the chaotic and dangerous world outside. A temporary, safe haven for Chihiro before she has to face her struggles again.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 51.2,
                "y_position": 52.9,
                "content": "Staging: The train itself is nearly perfectly symmetrical. Then Miyazaki breaks that balance with the characters. Instead of sitting in the center, Chihiro and No-Face occupy only the right side. That tiny imbalance makes the frame feel more natural and subtly more interesting. They are also facing forward, neither of them making eye contact or even moving. This is a genius way of implying that they're sharing a journey rather than a conversation.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 42.1,
                "y_position": 3.9,
                "content": "Lighting: The ceiling lamps provide soft ambient warmth while the cool evening light enters through the windows. There aren't any dramatic spotlights or shadows. Because the lighting feels ordinary, the emotional moments feel more believable.",
                "category": AnnotationCategory.technique,
            },
            {
                "x_position": 25.4,
                "y_position": 34.4,
                "content": "Visual Storytelling: Without ever having watched the movie before, a viewer could guess that these are 2 people travelling somewhere important, that they are not in danger, and that they are reflecting.",
                "category": AnnotationCategory.technique,
            },
        ],
        "palette_colors": [
            {"hex_value": "#2B3359ff", "display_order": 0},
            {"hex_value": "#53321Fff", "display_order": 1},
            {"hex_value": "#8D2E26ff", "display_order": 2},
            {"hex_value": "#A46A3Eff", "display_order": 3},
            {"hex_value": "#E6B489ff", "display_order": 4},
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
