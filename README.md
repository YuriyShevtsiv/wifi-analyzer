
# 🔌 Ethernet Monitor (Python)
<img width="400" height="528" alt="Screenshot 2026-02-07 182552" src="https://github.com/user-attachments/assets/e979c4db-dd15-4fd0-aeb5-7a564a16639a" />

## 📖 Description

**Ethernet Monitor** is a lightweight Python desktop application built with **Tkinter** that monitors the status of a wired (Ethernet) network connection on **Windows** systems.

The app detects whether an Ethernet cable is connected or disconnected, displays the connection status in real time, and logs connection history to a local file.
It is designed specifically for **Ethernet-only setups** and does **not** rely on Wi-Fi or WLAN features.

----

## ✨ Features 

* 🔌 Detects Ethernet connection status (Connected / Disconnected)
* 📊 Displays connection as **100% (connected)** or **0% (disconnected)**
* ⏱ Updates status every second
* 📝 Saves connection history to a log file
* 📂 One-click access to log folder
* 🗑 Ability to clear logs from the UI
* 🖥 Simple, dark-themed graphical interface
* ❌ No Wi-Fi dependency (works on Ethernet-only PCs)

---

## 🛠 Requirements

* **Windows OS**
* **Python 3.8+**
* Built-in Python libraries only:

  * `tkinter`
  * `os`
  * `time`

No third-party packages are required.

---

## 🚀 How It Works

* Uses the Windows command:

  ```
  netsh interface show interface
  ```

  to detect active Ethernet interfaces.
* Ethernet connections do not provide signal strength, so:

  * **Connected** → 100%
  * **Disconnected** → 0%
* Logs are saved every 5 seconds to:

  ```
  ethernet_history.txt
  ```

---

## ▶️ How to Run

1. Make sure Python is installed:

   ```bash
   python --version
   ```

2. Save the script as:

   ```text
   ethernet_monitor.py
   ```

3. Run the program:

   ```bash
   python ethernet_monitor.py
   ```

---

## 📁 Log File

* File name: `ethernet_history.txt`
* Location: Same folder as the script
* Format:

  ```
  [HH:MM:SS] Ethernet (Cable) | 100%
  ```

---

## ⚠️ Limitations

* Ethernet connections do **not** have real signal strength
* Speed, ping, and bandwidth are **not measured**
* Windows-only (uses `netsh`)

---

## 📌 Use Cases

* Ethernet-only desktops
* Servers with GUI access
* Network monitoring demos
* Learning Tkinter + system commands

---

## 📜 License

This project is open-source and free to use for learning and personal projects.
