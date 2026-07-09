"use client";

import { Annotation } from "@/types";
import styles from "./AnnotationMarker.module.css";

interface Props {
  annotation: Annotation;
  color: string;
  isHovered: boolean;
  isActive: boolean;
  onHoverEnter: () => void;
  onHoverLeave: () => void;
  onClick: (e: React.MouseEvent) => void;
}

export default function AnnotationMarker({
  annotation,
  color,
  isHovered,
  isActive,
  onHoverEnter,
  onHoverLeave,
  onClick,
}: Props) {
  const boxVisible = isHovered || isActive;

  // Left half of image → box extends left. Right half → box extends right.
  // const boxOnLeft = annotation.x_position < 50;
  // Edge proximity thresholds — if the marker is within this % of an edge,
  // force the box to the opposite side to prevent overflow.
  // Adjust these values if boxes still clip at your screen size.
  const LEFT_EDGE_THRESHOLD = 15;   // if x < 25%, force box to the RIGHT
  const RIGHT_EDGE_THRESHOLD = 85;  // if x > 75%, force box to the LEFT

  const boxOnLeft =
    annotation.x_position > RIGHT_EDGE_THRESHOLD
      ? true                                    // too close to right edge → force left
      : annotation.x_position < LEFT_EDGE_THRESHOLD
      ? false                                   // too close to left edge → force right
      : annotation.x_position < 50;            // middle zone → extend toward nearest edge

  // Below 65% down the image → connector goes up. Above → goes down.
  const boxAbove = annotation.y_position > 65;

  return (
    <div
      className={styles.markerContainer}
      style={{
        left: `${annotation.x_position}%`,
        top: `${annotation.y_position}%`,
        "--annotation-color": color,
      }}
      onClick={(e) => {
        e.stopPropagation();
        onClick(e);
      }}
      onMouseEnter={onHoverEnter}
      onMouseLeave={onHoverLeave}
    >
      {/* ── Dot ── */}
      <div className={`${styles.dot} ${isActive ? styles.dotActive : ""}`} />

      {boxVisible && (
        /*
          The connector is a single div styled as an L-shape using
          width, height, border-left, and border-bottom (or border-top).
          One element = guaranteed join at the corner, no alignment issues.
          
          We position it using inline styles to handle the four quadrant
          combinations (left/right × above/below).
        */
        <div
          className={`
            ${styles.connector}
            ${boxOnLeft ? styles.connectorLeft : styles.connectorRight}
            ${boxAbove ? styles.connectorAbove : styles.connectorBelow}
          `}
        >
          {/* ── Annotation box ──
              Positioned at the end of the horizontal arm of the L.
              CSS positions it at the correct corner automatically. */}
          <div
            className={`
              ${styles.annotationBox}
              ${boxOnLeft ? styles.boxLeft : styles.boxRight}
              ${boxAbove ? styles.boxAbove : styles.boxBelow}
              ${isActive ? styles.boxActive : ""}
            `}
          >
            <span className={styles.category}>{annotation.category}</span>
            <p className={styles.content}>{annotation.content}</p>
          </div>
        </div>
      )}
    </div>
  );
}
