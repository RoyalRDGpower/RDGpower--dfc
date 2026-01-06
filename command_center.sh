#!/data/data/com.termux/files/usr/bin/bash
# or use #!/bin/bash for PC

clear
echo "=============================="
echo "⚔️  RDGpower DevOps Command Center"
echo "=============================="
echo ""
echo "Select an operation:"
echo "1. Run Ethical Firewall (PC)"
echo "2. Run Ethical Firewall (Android)"
echo "3. Launch AI Core"
echo "4. Launch Supreme Toolkit"
echo "5. Run Guardian AI Sentinel"
echo "6. Exit"
echo ""

read -p "Enter choice [1-6]: " choice

case $choice in
  1) bash ethical_firewall.sh ;;
  2) bash ethical_firewall_android.sh ;;
  3) python3 ai-core.py ;;
  4) python3 supreme_tools.py ;;
  5) python3 rdg_guardian.py ;;
  6) echo "👋 Exiting Supreme Control Console." ;;
  *) echo "❌ Invalid option. Try again." ;;
esac
