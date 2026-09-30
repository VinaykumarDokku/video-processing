
import type { Metadata } from "next";
import { Inter } from "next/font/google";
// import "./globals.css";
import NavBar from "./navbar/navbar"


const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Video Processing App",
  description: "App to process videos",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      {/* <link rel="icon" type="image/x-icon" href="./favicon.ico" /> */}
      <body className={inter.className}>
        <NavBar />
        {children}
      </body>
    </html>
  );
}
