"use client";

import { PaletteColor } from "@/types";
import styles from "./ColorPalettePopup.module.css";

interface Props {
  colors: PaletteColor[];
  frameImageUrl: string;
  onClose: () => void;
}

export default function ColorPalettePopup({ colors, frameImageUrl, onClose }: Props) {
  return (
    /*
      Backdrop: covers the whole screen, dims the page.
      Clicking the backdrop (not the popup itself) closes it.
    */
    <div className={styles.backdrop} onClick={onClose}>

      {/* Stop clicks inside the popup from closing it */}
      <div className={styles.popup} onClick={(e) => e.stopPropagation()}>

        {/* The dimmed frame image visible behind the palette */}
        <img
          src={frameImageUrl}
          alt="Frame"
          className={styles.backgroundImage}
        />

        {/* The frosted palette card, centered over the image */}
        <div className={styles.paletteCard}>
          <div className={styles.swatchRow}>
            {colors.map((color) => (
              <div key={color.id} className={styles.swatchGroup}>
                {/* Color circle — background is the actual hex value */}
                <div
                  className={styles.swatch}
                  style={{ background: color.hex_value }}
                />
                {/* Hex value label below the circle */}
                <span className={styles.hexLabel}>{color.hex_value}</span>
              </div>
            ))}
          </div>
        </div>

        {/* Close button top-right corner */}
        <button
          className={styles.closeButton}
          onClick={onClose}
          aria-label="Close palette"
        >
          ✕
        </button>
      </div>
    </div>
  );
}