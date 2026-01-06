import Link from "next/link";

export default function AdminPage() {
  return (
    <main className="min-h-screen bg-zinc-950 text-white flex flex-col items-center justify-center gap-4">
      <h1 className="text-3xl font-bold">
        Admin Dashboard (Coming Soon)
      </h1>

      <Link href="/" className="text-zinc-400 hover:underline">
        ← Back to Home
      </Link>
    </main>
  );
}
