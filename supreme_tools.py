#!/usr/bin/env python3

import os
import subprocess
import platform

class SupremeToolkit:
    def __init__(self):
        self.options = {
            "1": self.sysinfo,
            "2": self.run_firewall,
            "3": self.scan_ports,
            "4": self.git_status,
            "99": self.exit_tool
        }

    def show_menu(self):
        print("\n🔧 Supreme Ethical AI Tool Menu")
        print("1. 📊 System Info")
        print("2. 🛡️ Run Firewall Script")
        print("3. 🌐 Scan Common Ports")
        print("4. 📁 Git Repo Status")
        print("99. ❌ Exit")

    def sysinfo(self):
        print("\n🧠 Gathering System Info...")
        print(f"System: {platform.system()} {platform.release()}")
        print(f"Architecture: {platform.machine()}")
        print(f"Node Name: {platform.node()}\n")

    def run_firewall(self):
        print("\n🛡️ Running firewall script...")
        if os.path.exists("ethical_firewall.sh"):
            os.system("bash ethical_firewall.sh")
        elif os.path.exists("ethical_firewall_android.sh"):
            os.system("bash ethical_firewall_android.sh")
        else:
            print("❌ No firewall script found.")

    def scan_ports(self):
        print("\n🌐 Scanning localhost common ports (22, 80, 443)...")
        ports = [22, 80, 443]
        for port in ports:
            result = subprocess.run(["nc", "-zv", "127.0.0.1", str(port)],
                                    capture_output=True, text=True)
            status = "🟢 OPEN" if "succeeded" in result.stderr else "🔴 CLOSED"
            print(f"Port {port}: {status}")

    def git_status(self):
        print("\n📁 Checking Git Repo Status...")
        os.system("git status")

    def exit_tool(self):
        print("👋 Exiting Supreme Tool.")
        exit(0)

    def run(self):
        while True:
            self.show_menu()
            choice = input("👉 Select: ").strip()
            if choice in self.options:
                self.options[choice]()
            else:
                print("⚠️ Invalid choice. Try again.")

# Entry
if __name__ == "__main__":
    toolkit = SupremeToolkit()
    toolkit.run()
