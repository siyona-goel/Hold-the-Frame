import Link from "next/link";
import { getMovies } from "@/lib/api";
import { Movie } from "@/types";
import styles from "./page.module.css";

export default async function PickAMovie() {
  const movies: Movie[] = await getMovies();

  return (
    <main className={styles.main}>
      <header className={styles.header}>
        <h1 className={styles.heading}>Pick a Movie</h1>
        <div className={styles.searchWrapper}>
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <circle cx="11" cy="11" r="8" />
            <path d="m21 21-4.35-4.35" />
          </svg>
          <input
            className={styles.searchInput}
            type="text"
            placeholder="Search"
          />
        </div>
      </header>

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
    </main>
  );
}
