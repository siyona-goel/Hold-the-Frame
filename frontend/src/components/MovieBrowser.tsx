"use client";

import { useState } from "react";
import { Movie } from "@/types";
import SearchBar from "@/components/SearchBar";
import MovieGrid from "@/components/MovieGrid";
import styles from "./MovieBrowser.module.css";

export default function MovieBrowser({ movies }: { movies: Movie[] }) {
  const [query, setQuery] = useState("");

  const filteredMovies = movies.filter((movie) =>
    movie.title.toLowerCase().includes(query.toLowerCase())
  );

  return (
    <>
      <div className={styles.header}>
        <h1 className={styles.heading}>Pick a Movie</h1>
        <SearchBar query={query} setQuery={setQuery} />
      </div>

      {filteredMovies.length === 0 ? (
        <p className={styles.empty}>No movies found for "{query}"</p>
      ) : (
        <MovieGrid movies={filteredMovies} />
      )}
    </>
  );
}
