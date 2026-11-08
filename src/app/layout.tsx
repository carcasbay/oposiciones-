import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Test Oposiciones — Técnico/a Medio Educación Social (Utrera)",
  description: "Plataforma de simulacros y test de examen con fórmula oficial de penalización, control de tiempo y estadísticas en local.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="es" className="h-full">
      <body className="min-h-full flex flex-col bg-slate-50 text-slate-900 antialiased selection:bg-blue-500 selection:text-white">
        {children}
      </body>
    </html>
  );
}
