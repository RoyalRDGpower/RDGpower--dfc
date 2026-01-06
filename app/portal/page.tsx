import Link from "next/link";

export default function UserPortal() {
  return (
    <main className="min-h-screen bg-zinc-950 text-white flex flex-col items-center justify-center gap-4">
      <h1 className="text-3xl font-bold">
        User Portal (Coming Soon)
      </h1>

      <Link href="/" className="text-zinc-400 hover:underline">
        ← Back to Home
      </Link>
    </main>
  );
}
