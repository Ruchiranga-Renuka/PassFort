import tkinter as tk
import re


def check_password(event=None):
    password = entry.get()

    checks = [
        ("At least 8 characters", len(password) >= 8),
        ("Contains uppercase letter", bool(re.search(r"[A-Z]", password))),
        ("Contains lowercase letter", bool(re.search(r"[a-z]", password))),
        ("Contains a number", bool(re.search(r"\d", password))),
        ("Contains a special character", bool(re.search(r"[!@#$%^&*(),.?\"{}|<>]", password))),
    ]

    passed = sum(1 for _, result in checks if result)

    for index, (label, result) in enumerate(checks):
        icon = "✓" if result else "✕"
        rule_labels[index].config(text=f"{icon}  {label}", fg="#2f3b52")

    if passed == 5:
        rating, color = "💪 Very Strong", "#16a34a"
    elif passed == 4:
        rating, color = "🟢 Strong", "#22c55e"
    elif passed == 3:
        rating, color = "🟡 Moderate", "#f59e0b"
    elif passed == 2:
        rating, color = "🟠 Weak", "#f97316"
    else:
        rating, color = "🔴 Very Weak", "#ef4444"

    strength_label.config(text=rating, fg=color)
    score_label.config(text=f"{passed} / 5 rules passed")

    bar_canvas.delete("all")
    bar_canvas.create_rectangle(0, 0, 300, 18, fill="#e5e7eb", outline="", tags="bg")
    bar_width = max(12, int((passed / 5) * 300))
    bar_canvas.create_rectangle(0, 0, bar_width, 18, fill=color, outline="", tags="bar")


def toggle_password():
    if entry.cget("show") == "*":
        entry.config(show="")
        toggle_btn.config(text="Hide")
    else:
        entry.config(show="*")
        toggle_btn.config(text="Show")


root = tk.Tk()
root.title("PassFort Password Checker")
root.geometry("460x520")
root.resizable(False, False)
root.configure(bg="#f3f6fb")

card = tk.Frame(root, bg="#ffffff", highlightthickness=1, highlightbackground="#e4e8f0")
card.pack(fill="both", expand=True, padx=18, pady=18)

header = tk.Frame(card, bg="#ffffff")
header.pack(fill="x", padx=24, pady=(20, 14))

icon_label = tk.Label(header, text="🔐", font=("Segoe UI", 24), bg="#ffffff")
icon_label.pack(anchor="w")

title_label = tk.Label(header, text="Password Checker", font=("Segoe UI", 18, "bold"),
                       bg="#ffffff", fg="#1f2937")
title_label.pack(anchor="w", pady=(4, 2))

subtitle_label = tk.Label(header, text="Build a stronger password with live feedback",
                          font=("Segoe UI", 10), bg="#ffffff", fg="#6b7280")
subtitle_label.pack(anchor="w")

entry_frame = tk.Frame(card, bg="#f8fafc", highlightthickness=1, highlightbackground="#dbe2ea")
entry_frame.pack(fill="x", padx=24, pady=(4, 12))

entry = tk.Entry(entry_frame, show="*", font=("Segoe UI", 13), width=28, relief="flat", bd=0,
                 bg="#f8fafc", fg="#111827", highlightthickness=0)
entry.pack(side="left", fill="x", expand=True, padx=(10, 0), ipady=8)
entry.bind("<KeyRelease>", check_password)
entry.focus_set()

toggle_btn = tk.Button(entry_frame, text="Show", font=("Segoe UI", 10, "bold"),
                       command=toggle_password, relief="flat", bd=0, bg="#4f46e5",
                       fg="#ffffff", cursor="hand2", padx=10, pady=6)
toggle_btn.pack(side="right", padx=6, pady=6)

strength_panel = tk.Frame(card, bg="#ffffff")
strength_panel.pack(fill="x", padx=24, pady=(4, 8))

strength_label = tk.Label(strength_panel, text="", font=("Segoe UI", 15, "bold"),
                          bg="#ffffff", fg="#111827")
strength_label.pack(anchor="w")

score_label = tk.Label(strength_panel, text="", font=("Segoe UI", 10),
                       bg="#ffffff", fg="#6b7280")
score_label.pack(anchor="w", pady=(2, 8))

bar_canvas = tk.Canvas(strength_panel, width=300, height=18, bg="#ffffff",
                       highlightthickness=0, bd=0)
bar_canvas.pack(anchor="w")

rules_frame = tk.Frame(card, bg="#f8fafc", highlightthickness=1, highlightbackground="#e5e7eb")
rules_frame.pack(fill="x", padx=24, pady=(10, 16))

rules = [
    "At least 8 characters",
    "Contains uppercase letter",
    "Contains lowercase letter",
    "Contains a number",
    "Contains a special character",
]
rule_labels = []
for rule in rules:
    lbl = tk.Label(rules_frame, text=f"✕  {rule}", font=("Segoe UI", 10),
                   bg="#f8fafc", fg="#4b5563", anchor="w")
    lbl.pack(fill="x", padx=10, pady=4)
    rule_labels.append(lbl)

footer_label = tk.Label(card, text="Built with Python & Tkinter", font=("Segoe UI", 8),
                        bg="#ffffff", fg="#9ca3af")
footer_label.pack(side="bottom", pady=(0, 14))

check_password()
root.mainloop()
