#!/data/data/com.termux/files/usr/bin/bash

echo "🔒 RDGpower Android Firewall Initializing..."

# Check if iptables is available (Root required)
if command -v iptables &> /dev/null; then
  echo "🔥 Root firewall active - applying iptables rules..."

  # Flush existing
  iptables -F

  # Default deny inbound
  iptables -P INPUT DROP
  iptables -P FORWARD DROP
  iptables -P OUTPUT ACCEPT

  # Allow loopback and related
  iptables -A INPUT -i lo -j ACCEPT
  iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

  # Open Termux SSH or HTTP if needed
  iptables -A INPUT -p tcp --dport 8022 -j ACCEPT  # Termux SSH
  iptables -A INPUT -p tcp --dport 8080 -j ACCEPT  # Termux web

  echo "✅ Root-based firewall rules applied."
else
  echo "⚠️ No root access — simulating basic Termux defense."

  termux-wake-lock
  am stop --user 0 com.android.bluetooth
  am stop --user 0 com.android.shell
  am force-stop com.termux

  echo "🛡️ Termux App Defense Activated (Non-root)"
fi

echo "🎯 Android Firewall Deployment Complete."
