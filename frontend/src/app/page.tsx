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
      <p>Movies returned from API: {movies.length}</p>
      <pre>{JSON.stringify(movies, null, 2)}</pre>
    </main>
  );
}
