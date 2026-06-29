async function getMovies() {
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/movies`, {
    cache: "no-store",
  });

  if (!res.ok) {
    throw new Error("Failed to fetch movies");
  }

  return res.json();
}

export default async function Home() {
  const movies = await getMovies();

  return (
    <main style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <h1>Hold the Frame</h1>
      {movies.map((movie: any) => (
        <div key={movie.id} style={{ marginBottom: "2rem" }}>
          <h2>{movie.title} ({movie.year})</h2>
          <p>{movie.studio}</p>
          <img
            src={movie.cover_image_url}
            alt={movie.title}
            style={{ width: "300px", borderRadius: "8px" }}
          />
        </div>
      ))}
    </main>
  );
}
