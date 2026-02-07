import tkinter as tk
import os
import time
from tkinter import messagebox

LOG_FILE = "ethernet_history.txt"


def is_ethernet_connected():
    """
    Returns True if ANY Ethernet interface is connected
    """
    try:
        output = os.popen("netsh interface show interface").read()
        for line in output.splitlines():
            if "Connected" in line and "Ethernet" in line:
                return True
    except Exception:
        pass
    return False


def get_ethernet_data():
    """
    Ethernet has no signal strength → use 100% if connected
    """
    if is_ethernet_connected():
        return "Ethernet (Cable)", 100
    return "Disconnected", 0


def save_log(name, signal):
    ts = time.strftime("%H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{ts}] {name} | {signal}%\n")


def update_loop():
    name, signal = get_ethernet_data()

    label_name.config(text=name)
    label_percent.config(text=f"{signal}%")

    color = "#3498db" if signal == 100 else "#e74c3c"

    canvas.coords(bar, 5, 5, 5 + signal * 3.4, 35)
    canvas.itemconfig(bar, fill=color)

    log_box.insert(
        tk.END,
        f"[{time.strftime('%H:%M:%S')}] {signal}%\n"
    )
    log_box.see(tk.END)

    if int(time.time()) % 5 == 0:
        save_log(name, signal)

    root.after(1000, update_loop)


def open_log_folder():
    os.startfile(os.getcwd())


def clear_logs():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
        log_box.delete(1.0, tk.END)
        messagebox.showinfo("System", "Logs cleared")


# ---------------- UI ----------------
root = tk.Tk()
root.title("Ethernet Monitor")
root.geometry("400x500")
root.config(bg="#121212")

tk.Label(
    root,
    text="🔌 Ethernet Monitor",
    font=("Arial", 18, "bold"),
    bg="#121212",
    fg="#00bfff"
).pack(pady=10)

label_name = tk.Label(
    root,
    text="Checking...",
    font=("Arial", 14),
    bg="#121212",
    fg="white"
)
label_name.pack()

label_percent = tk.Label(
    root,
    text="0%",
    font=("Arial", 40, "bold"),
    bg="#121212",
    fg="white"
)
label_percent.pack()

canvas = tk.Canvas(root, width=350, height=40, bg="#333", highlightthickness=0)
canvas.pack(pady=10)

bar = canvas.create_rectangle(5, 5, 5, 35, fill="#3498db", outline="")

tk.Label(
    root,
    text="Connection History",
    bg="#121212",
    fg="gray"
).pack()

log_box = tk.Text(
    root,
    width=40,
    height=8,
    bg="#222",
    fg="#00bfff",
    font=("Consolas", 9)
)
log_box.pack(pady=5)

btn_frame = tk.Frame(root, bg="#121212")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="📁 Logs", width=12, command=open_log_folder)\
    .grid(row=0, column=0, padx=5)

tk.Button(btn_frame, text="🗑 Clear", width=12, command=clear_logs)\
    .grid(row=0, column=1, padx=5)

update_loop()
root.mainloop()

