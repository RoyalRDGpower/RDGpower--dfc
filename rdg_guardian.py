#!/usr/bin/env python3

import os
import platform
import datetime

class RDGGuardian:
    def __init__(self):
        self.system = platform.system()
        self.log_file = f"logs/security_log_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        self.run_guardian()

    def run_guardian(self):
        print("🛡️ RDG Guardian Activated")
        self.log("🕒 Guardian started at " + str(datetime.datetime.now()))
        self.system_info()
        self.check_services()

    def log(self, message):
        os.makedirs("logs", exist_ok=True)
        with open(self.log_file, "a") as log:
            log.write(message + "\n")
        print(message)

    def system_info(self):
        self.log(f"📡 System: {self.system}")
        self.log(f"📅 Date: {datetime.datetime.now()}")
        self.log("📦 Checking disk usage:")
        os.system("df -h >> " + self.log_file)

    def check_services(self):
        self.log("🔍 Checking open ports and running services...")
        if self.system == "Linux" or "Android":
            os.system("netstat -tulnp >> " + self.log_file)

if __name__ == "__main__":
    RDGGuardian()
