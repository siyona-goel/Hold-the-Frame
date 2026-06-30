import { getMovie, getFrames } from "@/lib/api";
import { Movie, Frame } from "@/types";
import FrameCarousel from "@/components/FrameCarousel";
import styles from "./page.module.css";

export default async function PickAFrame({
  params,
}: {
  params: Promise<{ slug: string }>;
}) {
  const { slug } = await params;
  const movie: Movie = await getMovie(slug);
  const frames: Frame[] = await getFrames(slug);

  return (
    <main className={styles.main}>
      <h1 className={styles.heading}>Pick a Frame</h1>
      <p className={styles.subheading}>{movie.title}</p>
      <FrameCarousel frames={frames} movieSlug={movie.slug} />
    </main>
  );
}