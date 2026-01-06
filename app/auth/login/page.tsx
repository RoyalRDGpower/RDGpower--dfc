"use client";

import React, { useState } from "react";
import { signIn } from "next-auth/react";
import { useRouter } from "next/navigation";

export default function LoginPage() {
  const router = useRouter();
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const form = e.currentTarget;
    const formData = new FormData(form);
    const username = String(formData.get("username") || "");
    const password = String(formData.get("password") || "");

    const res = await signIn("credentials", { redirect: false, username, password });
    if (res?.error) {
      setError("Invalid credentials");
      return;
    }

    router.push("/admin");
  };

  return (
    <main className="min-h-screen bg-zinc-950 text-white flex items-center justify-center">
      <form onSubmit={handleSubmit} className="bg-zinc-800 p-6 rounded-md w-full max-w-sm">
        <h1 className="text-2xl font-bold">Login</h1>
        {error && <p className="text-red-400">{error}</p>}
        <div className="mt-4">
          <input name="username" type="text" placeholder="Username" className="w-full p-2 mb-4 rounded-md text-black" />
          <input name="password" type="password" placeholder="Password" className="w-full p-2 mb-4 rounded-md text-black" />
        </div>
        <button type="submit" className="w-full py-2 mt-4 bg-blue-600 text-white rounded-md">Sign In</button>
      </form>
    </main>
  );
}
