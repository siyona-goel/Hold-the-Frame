import type { Metadata } from "next";
import { League_Gothic, Libre_Franklin } from "next/font/google";
import "./globals.css";

const leagueGothic = League_Gothic({
  subsets: ["latin"],
  variable: "--font-display",
  display: "swap",
});

const libreFranklin = Libre_Franklin({
  subsets: ["latin"],
  variable: "--font-body",
  weight: ["400", "500", "600"],
  display: "swap",
});

export const metadata: Metadata = {
  title: "Hold the Frame",
  description: "A curated gallery of animated film frames.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={`${leagueGothic.variable} ${libreFranklin.variable}`}>
      <body>{children}</body>
    </html>
  );
}
