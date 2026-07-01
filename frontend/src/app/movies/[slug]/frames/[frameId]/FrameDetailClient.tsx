"use client";

import { useState } from "react";
import Link from "next/link";
import { FrameDetail, Movie } from "@/types";
import AnnotationMarker from "@/components/AnnotationMarker";
import ColorPalettePopup from "@/components/ColorPalettePopup";
import styles from "./page.module.css";

export default function FrameDetailClient({
  frame,
  movie,
}: {
  frame: FrameDetail;
  movie: Movie;
}) {
  // Which annotation is currently pinned open (-1 means none)
  const [activeAnnotationId, setActiveAnnotationId] = useState<number | null>(null);

  // Whether the color palette popup is visible
  const [paletteOpen, setPaletteOpen] = useState(false);

  // Clicking a marker: if it's already active, close it; otherwise open it
  const handleMarkerClick = (id: number) => {
    setActiveAnnotationId((prev) => (prev === id ? null : id));
  };

  // Hovering a marker shows a preview — we track hovered id separately
  const [hoveredAnnotationId, setHoveredAnnotationId] = useState<number | null>(null);

  return (
    <main className={styles.main}>

      {/* ── Top bar ── */}
      <div className={styles.topBar}>
        <Link href={`/movies/${movie.slug}`} className={styles.backLink}>
          {/* Left arrow */}
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none"
            stroke="currentColor" strokeWidth="2.5" strokeLinecap="round">
            <path d="M19 12H5M5 12l7-7M5 12l7 7" />
          </svg>
          Back to Gallery
        </Link>

        {/* Timestamp shown top-right, pulled from the frame's data */}
        <span className={styles.timestamp}>
          Timestamp: {frame.timestamp_label}
        </span>
      </div>

      {/* ── Frame image + annotation markers ──
          The wrapper is position:relative so markers can be absolutely
          positioned as percentages of the image dimensions. */}
      <div className={styles.frameWrapper}>
        <img
          src={frame.image_url}
          alt={`Frame at ${frame.timestamp_label}`}
          className={styles.frameImage}
          /* Clicking anywhere on the image that isn't a marker clears the active annotation */
          onClick={() => setActiveAnnotationId(null)}
        />

        {/* Render one marker per annotation */}
        {frame.annotations.map((annotation) => (
          <AnnotationMarker
            key={annotation.id}
            annotation={annotation}
            isHovered={hoveredAnnotationId === annotation.id}
            isActive={activeAnnotationId === annotation.id}
            onHoverEnter={() => setHoveredAnnotationId(annotation.id)}
            onHoverLeave={() => setHoveredAnnotationId(null)}
            onClick={() => handleMarkerClick(annotation.id)}
          />
        ))}
      </div>

      {/* ── Bottom bar ──
          Three elements: More scenes (centered), View Color Palette (right) */}
      <div className={styles.bottomBar}>

        {/* Spacer on the left to let the center item sit truly centered */}
        <div className={styles.bottomSpacer} />

        {/* More scenes like this — no functionality yet, just a visual prompt */}
        <div className={styles.moreScenesGroup}>
          <span className={styles.moreScenesLabel}>More scenes like this</span>
          {/* Downward arrow */}
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none">
            <path d="M12 4v12m0 0l-4-4m4 4l4-4" stroke="#ffffff8c"
              strokeWidth="2" strokeLinecap="round" fill="none"/>
            {/* <polygon points="7,14 12,20 17,14" fill="white" /> */}
          </svg>
        </div>

        {/* View Color Palette button — opens the popup */}
        <button
          className={styles.paletteButton}
          onClick={() => setPaletteOpen(true)}
          aria-label="View color palette"
        >
          {/* Palette icon */}
          <svg width="22" height="22" viewBox="0 0 24 24" fill="currentColor">
            <path d="M12 2C6.48 2 2 6.48 2 12c0 5.52 4.48 10 10 10 
              1.1 0 2-.9 2-2 0-.54-.21-1.03-.55-1.4-.32-.36-.52-.84-.52-1.36 
              0-1.1.9-2 2-2h2.35C19.87 15.24 22 13.76 22 12c0-5.52-4.48-10-10-10z"/>
            <circle cx="6.5" cy="11.5" r="1.5" fill="var(--bg)"/>
            <circle cx="9.5" cy="7.5" r="1.5" fill="var(--bg)"/>
            <circle cx="14.5" cy="7.5" r="1.5" fill="var(--bg)"/>
            <circle cx="17.5" cy="11.5" r="1.5" fill="var(--bg)"/>
          </svg>
          View Color Palette
        </button>
      </div>

      {/* ── Color Palette Popup ──
          Rendered here so it can overlay the whole page.
          Only mounts/shows when paletteOpen is true. */}
      {paletteOpen && (
        <ColorPalettePopup
          colors={frame.palette_colors}
          frameImageUrl={frame.image_url}
          onClose={() => setPaletteOpen(false)}
        />
      )}
    </main>
  );
}