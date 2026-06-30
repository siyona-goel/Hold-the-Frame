"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { Frame } from "@/types";
import styles from "./FrameCarousel.module.css";

export default function FrameCarousel({
  frames,
  movieSlug,
}: {
  frames: Frame[];
  movieSlug: string;
}) {
  const [activeIndex, setActiveIndex] = useState(0);
  const router = useRouter();

  const goPrev = () => {
    setActiveIndex((prev) => (prev === 0 ? frames.length - 1 : prev - 1));
  };

  const goNext = () => {
    setActiveIndex((prev) => (prev === frames.length - 1 ? 0 : prev + 1));
  };

  const handleCardClick = (index: number) => {
    if (index === activeIndex) {
      // Already centered — open it
      router.push(`/movies/${movieSlug}/frames/${frames[index].id}`);
    } else {
      setActiveIndex(index);
    }
  };

  if (frames.length === 0) {
    return <p className={styles.empty}>No frames yet for this movie.</p>;
  }

  return (
    <div className={styles.carouselWrapper}>
      <button className={styles.arrow} onClick={goPrev} aria-label="Previous frame">
        ‹
      </button>

      <div className={styles.stage}>
        {frames.map((frame, index) => {
          // Distance from active card, accounting for wraparound
          let offset = index - activeIndex;
          if (offset > frames.length / 2) offset -= frames.length;
          if (offset < -frames.length / 2) offset += frames.length;

          const isActive = offset === 0;
          const absOffset = Math.abs(offset);

          // Only render cards within 2 positions of center to keep it clean
          if (absOffset > 2) return null;

          const rotateY = offset * -35; // degrees
          const translateX = offset * 220; // px
          const translateZ = -absOffset * 150; // px, pushes side cards back
          const opacity = isActive ? 1 : absOffset === 1 ? 0.6 : 0.3;
          const scale = isActive ? 1 : 0.8;

          return (
            <div
              key={frame.id}
              className={styles.card}
              style={{
                transform: `translateX(${translateX}px) translateZ(${translateZ}px) rotateY(${rotateY}deg) scale(${scale})`,
                opacity,
                zIndex: 10 - absOffset,
              }}
              onClick={() => handleCardClick(index)}
            >
              <img
                src={frame.image_url}
                alt={frame.timestamp_label}
                className={styles.cardImage}
              />
            </div>
          );
        })}
      </div>

      <button className={styles.arrow} onClick={goNext} aria-label="Next frame">
        ›
      </button>
    </div>
  );
}
