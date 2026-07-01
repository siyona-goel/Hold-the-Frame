"use client";

import { Annotation } from "@/types";
import styles from "./AnnotationMarker.module.css";

interface Props {
  annotation: Annotation;
  isHovered: boolean;  // cursor is over the marker
  isActive: boolean;   // user has clicked and pinned it open
  onHoverEnter: () => void;
  onHoverLeave: () => void;
  onClick: (e: React.MouseEvent) => void;
}

export default function AnnotationMarker({
  annotation,
  isHovered,
  isActive,
  onHoverEnter,
  onHoverLeave,
  onClick,
}: Props) {
  // The box is visible if hovered (preview) or active (pinned)
  const boxVisible = isHovered || isActive;

  // Decide which side the annotation box appears on.
  // If the marker is in the right half of the image (x > 50%), 
  // place the box to the left to keep it on screen. Otherwise place right.
  const boxOnLeft = annotation.x_position > 50;

  return (
    /*
      The marker container is absolutely positioned as a percentage of the
      frame image. We use transform: translate(-50%, -50%) to center the
      marker circle on the exact coordinate, not offset from it.
    */
    <div
      className={styles.markerContainer}
      style={{
        left: `${annotation.x_position}%`,
        top: `${annotation.y_position}%`,
      }}
      onClick={(e) => {
        e.stopPropagation(); // prevent click from bubbling to the frame image
        onClick(e);
      }}
      onMouseEnter={onHoverEnter}
      onMouseLeave={onHoverLeave}
    >
      {/* ── The circular marker dot ──
          White fill, gold border — matching your mockup detail */}
      <div className={`${styles.dot} ${isActive ? styles.dotActive : ""}`} />

      {/* ── SVG connecting line ──
          Drawn as an SVG absolutely positioned relative to the marker.
          The line curves from the dot to the annotation box.
          Dimensions and curve direction flip based on boxOnLeft. */}
      {boxVisible && (
        <svg
          className={styles.connectorSvg}
          style={{
            /* Position SVG so it bridges from the dot to the box */
            left: boxOnLeft ? "auto" : "12px",
            right: boxOnLeft ? "12px" : "auto",
          }}
          width="120"
          height="80"
          viewBox="0 0 120 80"
          fill="none"
          /* Flip horizontally when box is on the left */
          transform={boxOnLeft ? "scale(-1,1)" : undefined}
        >
          {/*
            Curved path: starts at the dot (left edge of SVG),
            curves up and out to the box (right edge).
            Change the control points (Q) to adjust the curve shape.
          */}
          <path
            d="M 0 40 Q 40 40 80 10 L 120 10"
            stroke="#C17F24"   /* gold line color — change this to adjust */
            strokeWidth="2"
            strokeLinecap="round"
          />
        </svg>
      )}

      {/* ── Annotation box ──
          Positioned to the left or right of the marker based on boxOnLeft.
          Opacity transitions for hover preview vs click pin. */}
      <div
        className={`
          ${styles.annotationBox}
          ${boxOnLeft ? styles.boxLeft : styles.boxRight}
          ${isActive ? styles.boxActive : ""}
          ${boxVisible ? styles.boxVisible : ""}
        `}
      >
        {/* Category label — small text above the annotation content */}
        <span className={styles.category}>
          {annotation.category}
        </span>
        <p className={styles.content}>{annotation.content}</p>
      </div>
    </div>
  );
}
