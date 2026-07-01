import { getFrame, getMovie } from "@/lib/api";
import { FrameDetail, Movie } from "@/types";
import FrameDetailClient from "./FrameDetailClient";

export default async function FrameDetailPage({
  params,
}: {
  params: Promise<{ slug: string; frameId: string }>;
}) {
  const { slug, frameId } = await params;
  const frame: FrameDetail = await getFrame(Number(frameId));
  const movie: Movie = await getMovie(slug);

  // Pass data down to the client component which handles all interactivity
  return <FrameDetailClient frame={frame} movie={movie} />;
}
