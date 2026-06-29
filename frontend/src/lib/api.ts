const API_URL = process.env.NEXT_PUBLIC_API_URL;

export async function getMovies() {
  const res = await fetch(`${API_URL}/movies`, { cache: "no-store" });
  if (!res.ok) throw new Error("Failed to fetch movies");
  return res.json();
}

export async function getMovie(slug: string) {
  const res = await fetch(`${API_URL}/movies/${slug}`, { cache: "no-store" });
  if (!res.ok) throw new Error("Failed to fetch movie");
  return res.json();
}

export async function getFrames(movieSlug: string) {
  const res = await fetch(`${API_URL}/movies/${movieSlug}/frames`, { cache: "no-store" });
  if (!res.ok) throw new Error("Failed to fetch frames");
  return res.json();
}

export async function getFrame(frameId: number) {
  const res = await fetch(`${API_URL}/frames/${frameId}`, { cache: "no-store" });
  if (!res.ok) throw new Error("Failed to fetch frame");
  return res.json();
}