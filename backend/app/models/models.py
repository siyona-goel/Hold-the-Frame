from sqlalchemy import (
    Column, Integer, String, Text, Float,
    ForeignKey, DateTime, Boolean, Enum
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from pgvector.sqlalchemy import Vector
from app.database import Base
import enum

# ---------------------------------------------------------------------------
# Enum for annotation categories
# You're storing the category on every annotation right now even though you
# don't filter by it yet. This is what enables "find by mood/technique" later
# without touching the schema.
# ---------------------------------------------------------------------------

class AnnotationCategory(enum.Enum):
    emotion = "emotion"
    theme = "theme"
    technique = "technique"
    color = "color"
    composition = "composition"
    general = "general"


# ---------------------------------------------------------------------------
# Movies
# One row per film. slug is used in URLs e.g. /movies/princess-and-the-frog
# ---------------------------------------------------------------------------

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    studio = Column(String, nullable=False)
    cover_image_url = Column(String, nullable=False)   # Cloudinary URL
    slug = Column(String, unique=True, nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationship: one movie has many frames
    frames = relationship("Frame", back_populates="movie", cascade="all, delete-orphan")


# ---------------------------------------------------------------------------
# Frames
# One row per still/screenshot from a movie.
# display_order controls the order they appear in the carousel.
# embedding is a 384-dimension vector — this matches the output size of
# all-MiniLM-L6-v2. Leave it null for
# now. When you're ready to add the AI search feature, you run a script
# that populates this column from each frame's annotations.
# x_position and y_position on annotations (below) are percentages, not
# pixels, so markers stay correctly placed at any screen size.
# ---------------------------------------------------------------------------

class Frame(Base):
    __tablename__ = "frames"

    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey("movies.id"), nullable=False)
    image_url = Column(String, nullable=False)         # Cloudinary URL
    timestamp_label = Column(String, nullable=False)   # e.g. "04:45"
    description = Column(Text, nullable=True)          # short curator note
    display_order = Column(Integer, nullable=False, default=0)
    embedding = Column(Vector(384), nullable=True)     # populated later
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    movie = relationship("Movie", back_populates="frames")
    annotations = relationship("Annotation", back_populates="frame", cascade="all, delete-orphan")
    palette_colors = relationship("PaletteColor", back_populates="frame", cascade="all, delete-orphan")
    images = relationship("FrameImage", back_populates="frame", cascade="all, delete-orphan")


# ---------------------------------------------------------------------------
# Annotations
# Each annotation is one marker on the frame image.
# x_position and y_position are 0.0–100.0, representing percentage of the
# image width/height from the top-left corner. So a marker at (50.0, 50.0)
# is dead center regardless of how large the image renders on screen.
# ---------------------------------------------------------------------------

class Annotation(Base):
    __tablename__ = "annotations"

    id = Column(Integer, primary_key=True, index=True)
    frame_id = Column(Integer, ForeignKey("frames.id"), nullable=False)
    x_position = Column(Float, nullable=False)  # 0.0 to 100.0
    y_position = Column(Float, nullable=False)  # 0.0 to 100.0
    content = Column(Text, nullable=False)       # the text you've written
    category = Column(
        Enum(AnnotationCategory),
        nullable=False,
        default=AnnotationCategory.general
    )
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    frame = relationship("Frame", back_populates="annotations")


# ---------------------------------------------------------------------------
# PaletteColors
# Each row is one color swatch in a frame's color palette.
# display_order controls left-to-right order in the palette popup.
# ---------------------------------------------------------------------------

class PaletteColor(Base):
    __tablename__ = "palette_colors"

    id = Column(Integer, primary_key=True, index=True)
    frame_id = Column(Integer, ForeignKey("frames.id"), nullable=False)
    hex_value = Column(String(9), nullable=False)  # e.g. "#1C0E02ff"
    display_order = Column(Integer, nullable=False, default=0)

    frame = relationship("Frame", back_populates="palette_colors")

# ---------------------------------------------------------------------------
# FrameImages
# Allows a frame to have multiple images displayed side by side on the
# detail page. is_primary=True is the image shown in the carousel.
# display_order controls left-to-right order on the detail page.
# ---------------------------------------------------------------------------

class FrameImage(Base):
    __tablename__ = "frame_images"

    id = Column(Integer, primary_key=True, index=True)
    frame_id = Column(Integer, ForeignKey("frames.id"), nullable=False)
    image_url = Column(String, nullable=False)        # Cloudinary URL
    is_primary = Column(Boolean, nullable=False, default=False)
    display_order = Column(Integer, nullable=False, default=0)

    frame = relationship("Frame", back_populates="images")
