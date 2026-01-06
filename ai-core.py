#!/usr/bin/env python3

import os
import platform
import datetime

class RDGCoreAI:
    def __init__(self):
        self.start_time = datetime.datetime.now()
        self.commands = {
            "status": self.status,
            "defend": self.firewall_sync,
            "clear": self.clear_screen,
            "exit": self.shutdown,
        }

    def boot(self):
        print("🧠 RDG Ethical AI Core Activated")
        print("🔐 Supreme Protocol Ready | Version 1.0\n")
        while True:
            cmd = input("🔻 RDG > ").strip().lower()
            if cmd in self.commands:
                self.commands[cmd]()
            else:
                print("⚠️ Unknown command. Type: status, defend, clear, exit")

    def status(self):
        print(f"🕒 Uptime: {datetime.datetime.now() - self.start_time}")
        print(f"💻 OS: {platform.system()} {platform.release()}")
        print("🛡️  AI Mode: Ethical Defense")
        print("📁 Repo: RDGpower--dfc")

    def firewall_sync(self):
        print("⚔️ Engaging local firewall sync...")
        if os.path.exists("ethical_firewall.sh"):
            os.system("bash ethical_firewall.sh")
        elif os.path.exists("ethical_firewall_android.sh"):
            os.system("bash ethical_firewall_android.sh")
        else:
            print("❌ No firewall script found in local directory.")

    def clear_screen(self):
        os.system("cls" if os.name == 'nt' else "clear")

    def shutdown(self):
        print("🔒 Shutting down RDG Core AI.")
        exit(0)

# Entry point
if __name__ == "__main__":
    try:
        ai = RDGCoreAI()
        ai.boot()
    except KeyboardInterrupt:
        print("\n🛑 Interrupted. Session closed.")
