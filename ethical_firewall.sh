

#!/bin/bash

echo "🛡️ Activating Supreme Ethical Firewall..."

# 1. Flush existing rules (optional — use with caution)
iptables -F

# 2. Set default policies
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# 3. Allow localhost (loopback)
iptables -A INPUT -i lo -j ACCEPT

# 4. Allow established and related connections
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# 5. Allow specific ports (SSH, HTTP, HTTPS) — edit as needed
iptables -A INPUT -p tcp --dport 22 -j ACCEPT   # SSH
iptables -A INPUT -p tcp --dport 80 -j ACCEPT   # HTTP
iptables -A INPUT -p tcp --dport 443 -j ACCEPT  # HTTPS

# 6. Log dropped packets (optional, advanced users only)
# iptables -A INPUT -j LOG --log-prefix "DROP_INPUT: "

echo "✅ Ethical Firewall Rules Applied Successfully."

# Save rules permanently (Linux systems only)
# For Debian/Ubuntu:
# iptables-save > /etc/iptables/rules.v4
