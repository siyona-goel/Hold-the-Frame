export interface Movie {
  id: number;
  title: string;
  year: number;
  studio: string;
  cover_image_url: string;
  slug: string;
}

export interface Frame {
  id: number;
  movie_id: number;
  image_url: string;
  timestamp_label: string;
  description: string | null;
  display_order: number;
}

export interface Annotation {
  id: number;
  frame_id: number;
  x_position: number;
  y_position: number;
  content: string;
  category: "emotion" | "theme" | "technique" | "color" | "composition" | "general";
}

export interface PaletteColor {
  id: number;
  frame_id: number;
  hex_value: string;
  display_order: number;
}

export interface FrameImage {
  id: number;
  image_url: string;
  is_primary: boolean;
  display_order: number;
}

export interface FrameDetail {
  id: number;
  movie_id: number;
  image_url: string;           // primary image, used for carousel
  timestamp_label: string;
  description: string | null;
  display_order: number;
  images: FrameImage[];        // all images, used for detail page
  annotations: Annotation[];
  palette_colors: PaletteColor[];
}
