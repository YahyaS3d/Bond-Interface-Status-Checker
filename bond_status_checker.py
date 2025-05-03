import os
import re

def list_bond_interfaces():
    bonding_path = "/proc/net/bonding"
    if not os.path.isdir(bonding_path):
        print("[ERROR] Bonding directory not found. Are bond interfaces configured?")
        return []
    
    return os.listdir(bonding_path)

def parse_bond_status(bond_interface):
    bond_file = f"/proc/net/bonding/{bond_interface}"

    if not os.path.exists(bond_file):
        print(f"[ERROR] Bond interface '{bond_interface}' not found.")
        return

    with open(bond_file, 'r') as f:
        data = f.read()

    print("\n" + "="*50)
    print(f"🔍 Bond Interface: {bond_interface}")
    print("="*50)

    # Get bonding mode
    mode = re.search(r'Bonding Mode:\s+(.+)', data)
    print(f"🔧 Mode: {mode.group(1) if mode else 'Unknown'}")

    # Get currently active interface
    active = re.search(r'Currently Active Slave:\s+(\w+)', data)
    print(f"📡 Active Interface: {active.group(1) if active else 'None'}")

    # Subordinate interfaces and their statuses
    print("\n📊 Subordinate Interfaces Status:")
    slaves = re.findall(r'Slave Interface: (\w+).*?MII Status: (\w+)', data, re.DOTALL)
    if not slaves:
        print("  No subordinate interfaces found.")
    else:
        for iface, status in slaves:
            symbol = "✅" if status.lower() == "up" else "❌"
            print(f"  - {iface:<10} Status: {status.upper()} {symbol}")

    print("="*50 + "\n")

def main():
    interfaces = list_bond_interfaces()
    if not interfaces:
        print("No bond interfaces found. Exiting.")
        return

    print("📘 Available Bond Interfaces:")
    for iface in interfaces:
        print(f" - {iface}")

    selected = input("\n👉 Enter the bond interface you want to inspect (e.g., bond0): ").strip()
    if selected not in interfaces:
        print(f"[ERROR] '{selected}' is not a valid bond interface.")
        return

    parse_bond_status(selected)

if __name__ == "__main__":
    main()
