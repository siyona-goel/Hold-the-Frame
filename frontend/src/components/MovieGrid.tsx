import Link from "next/link";
import { Movie } from "@/types";
import styles from "./MovieGrid.module.css";

export default function MovieGrid({ movies }: { movies: Movie[] }) {
  return (
    <div className={styles.grid}>
      {movies.map((movie) => (
        <Link
          key={movie.id}
          href={`/movies/${movie.slug}`}
          className={styles.card}
        >
          <img
            src={movie.cover_image_url}
            alt={movie.title}
            className={styles.cardImage}
          />
          <div className={styles.cardOverlay}>
            <span className={styles.cardTitle}>{movie.title}</span>
            <span className={styles.cardYear}>{movie.year}</span>
          </div>
        </Link>
      ))}
    </div>
  );
}
