import tkinter as tk
import re

def check_password(event=None):
    password = entry.get()

    checks = [
        ("At least 8 characters",      len(password) >= 8),
        ("Contains uppercase letter",   bool(re.search(r'[A-Z]', password))),
        ("Contains lowercase letter",   bool(re.search(r'[a-z]', password))),
        ("Contains a number",           bool(re.search(r'\d', password))),
        ("Contains a special character",bool(re.search(r'[!@#$%^&*(),.?\":{}|<>]', password))),
    ]

    passed = sum(1 for _, result in checks if result)

    for i, (label, result) in enumerate(checks):
        icon = "✅" if result else "❌"
        rule_labels[i].config(text=f"  {icon}  {label}")

    if passed == 5:
        rating, color = "💪 Very Strong", "#2e7d32"
    elif passed == 4:
        rating, color = "🟢 Strong", "#388e3c"
    elif passed == 3:
        rating, color = "🟡 Moderate", "#f9a825"
    elif passed == 2:
        rating, color = "🟠 Weak", "#e65100"
    else:
        rating, color = "🔴 Very Weak", "#c62828"

    strength_label.config(text=rating, fg=color)
    score_label.config(text=f"{passed} / 5 rules passed")

    bar_canvas.delete("bar")
    bar_width = int((passed / 5) * 340)
    bar_canvas.create_rectangle(0, 0, bar_width, 14, fill=color, outline="", tags="bar")

def toggle_password():
    if entry.cget("show") == "*":
        entry.config(show="")
        toggle_btn.config(text="Hide")
    else:
        entry.config(show="*")
        toggle_btn.config(text="Show")

root = tk.Tk()
root.title("Password Checker")
root.geometry("420x420")
root.resizable(False, False)
root.configure(bg="#f5f5f5")

tk.Label(root, text="Password Checker", font=("Helvetica", 18, "bold"),
         bg="#f5f5f5", fg="#212121").pack(pady=(24, 4))
tk.Label(root, text="Check how strong your password is",
         font=("Helvetica", 10), bg="#f5f5f5", fg="#757575").pack()

frame = tk.Frame(root, bg="#f5f5f5")
frame.pack(pady=16)
entry = tk.Entry(frame, show="*", font=("Helvetica", 13), width=22,
                 relief="flat", bd=0, bg="#ffffff",
                 highlightthickness=1, highlightbackground="#cccccc",
                 highlightcolor="#1565c0")
entry.pack(side="left", ipady=8, ipadx=6)
entry.bind("<KeyRelease>", check_password)
toggle_btn = tk.Button(frame, text="Show", font=("Helvetica", 10),
                       command=toggle_password, relief="flat",
                       bg="#e3f2fd", fg="#1565c0", cursor="hand2", padx=6)
toggle_btn.pack(side="left", padx=(6, 0), ipady=6)

bar_canvas = tk.Canvas(root, width=340, height=14, bg="#e0e0e0",
                       highlightthickness=0, bd=0)
bar_canvas.pack()

strength_label = tk.Label(root, text="", font=("Helvetica", 13, "bold"),
                           bg="#f5f5f5")
strength_label.pack(pady=(10, 2))
score_label = tk.Label(root, text="", font=("Helvetica", 10),
                        bg="#f5f5f5", fg="#757575")
score_label.pack()

rules_frame = tk.Frame(root, bg="#ffffff", relief="flat",
                        highlightthickness=1, highlightbackground="#e0e0e0")
rules_frame.pack(pady=14, padx=30, fill="x")

rules = [
    "At least 8 characters",
    "Contains uppercase letter",
    "Contains lowercase letter",
    "Contains a number",
    "Contains a special character",
]
rule_labels = []
for rule in rules:
    lbl = tk.Label(rules_frame, text=f"  ❌  {rule}",
                   font=("Helvetica", 10), bg="#ffffff",
                   fg="#424242", anchor="w")
    lbl.pack(fill="x", padx=8, pady=3)
    rule_labels.append(lbl)

tk.Label(root, text="Built with Python & Tkinter",
         font=("Helvetica", 8), bg="#f5f5f5", fg="#bdbdbd").pack(side="bottom", pady=8)

root.mainloop()