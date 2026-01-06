import Link from "next/link";

export default function Home() {
  return (
    <main className="min-h-screen bg-zinc-950 text-white flex items-center justify-center px-6">
      <div className="max-w-xl text-center space-y-6">
        <h1 className="text-4xl md:text-5xl font-bold tracking-tight">
          SRDG Fintech Platform
        </h1>

        <p className="text-zinc-400 text-lg">
          Secure. Scalable. Admin-controlled digital finance infrastructure.
        </p>

        <div className="flex flex-col sm:flex-row gap-4 justify-center pt-4">
          <Link
            href="/admin"
            className="px-6 py-3 rounded-lg bg-white text-black font-medium hover:bg-zinc-200 transition"
          >
            Admin Dashboard
          </Link>

          <Link
            href="/portal"
            className="px-6 py-3 rounded-lg border border-zinc-700 text-white hover:bg-zinc-900 transition"
          >
            User Portal
          </Link>
        </div>

        <p className="text-xs text-zinc-500 pt-6">
          © {new Date().getFullYear()} SRDG • All rights reserved
        </p>
      </div>
    </main>
  );
}
