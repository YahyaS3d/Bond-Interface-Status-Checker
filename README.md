#  Bond Interface Status Checker

A simple Python tool to check the status of **Bond Interfaces (Link Aggregation)** on Linux systems, especially useful for environments using **Check Point Security Gateways**.

## 📋 Features

* Lists all available bond interfaces from `/proc/net/bonding/`
* Shows bonding mode (e.g., Active/Backup, LACP)
* Displays the currently active subordinate interface
* Provides health status (`UP`/`DOWN`) of all subordinate interfaces
* Clean, user-friendly CLI with formatted output

## 🚀 How to Use

1. **Run the script**:

   ```bash
   python3 bond_status_checker.py
   ```

2. **Select the bond interface** when prompted (e.g., `bond0`, `bond1`).

3. **View the output**, which includes mode, active interface, and subordinate statuses.

## 🛠 Requirements

* Python 3.x
* Linux system with bonding configured
* Read access to `/proc/net/bonding/`

## 🧑‍💻 Example Output

```
📘 Available Bond Interfaces:
 - bond0
 - bond1

👉 Enter the bond interface you want to inspect (e.g., bond0): bond0

🔍 Bond Interface: bond0
🔧 Mode: IEEE 802.3ad Dynamic link aggregation
📡 Active Interface: eth1

📊 Subordinate Interfaces Status:
  - eth0       Status: UP ✅
  - eth1       Status: UP ✅
```

## 📎 Notes

* Designed for Check Point and other Linux-based appliances.
* Ideal for sysadmins monitoring high availability or link aggregation setups.


