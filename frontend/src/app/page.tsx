import { getMovies } from "@/lib/api";
import { Movie } from "@/types";
import MovieBrowser from "@/components/MovieBrowser";
import styles from "./page.module.css";

export default async function PickAMovie() {
  const movies: Movie[] = await getMovies();

  return (
    <main className={styles.main}>
      <MovieBrowser movies={movies} />
    </main>
  );
}
