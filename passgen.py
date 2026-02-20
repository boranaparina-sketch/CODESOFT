import tkinter as tk
from tkinter import messagebox
import string
import secrets

DARK_BG = "#0f172a"        
CARD_BG = "#1e293b"        
ACCENT = "#14b8a6"         
TEXT_WHITE = "#e0e7ff"    
GREEN = "#22c55e"          
RED = "#ef4444"            

def generate_password():
    chars = string.ascii_lowercase
    if var_upper.get(): chars += string.ascii_uppercase
    if var_nums.get():  chars += string.digits
    if var_syms.get():  chars += string.punctuation
    
    if not chars:
        messagebox.showwarning("Selection Empty", "Please select at least one character type!")
        return

    length = int(len_slider.get())
    password = "".join(secrets.choice(chars) for _ in range(length))
    
    result_entry.config(state="normal")
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)
    result_entry.config(state="readonly")
    
    update_strength(length, len(chars))

def update_strength(length, char_pool):
    if length < 10 or char_pool < 40:
        strength_bar.config(width=100, bg=RED)
        strength_text.config(text="Weak", fg=RED)
    elif length < 16:
        strength_bar.config(width=200, bg="#fbbf24") # Amber
        strength_text.config(text="Medium", fg="#fbbf24")
    else:
        strength_bar.config(width=300, bg=GREEN)
        strength_text.config(text="Strong", fg=GREEN)

def copy_pass():
    root.clipboard_clear()
    root.clipboard_append(result_entry.get())
    copy_btn.config(text="COPIED!", fg=GREEN)
    root.after(1500, lambda: copy_btn.config(text="COPY", fg=ACCENT))

# --- UI Setup ---
root = tk.Tk()
root.title("SecurePass Engine")
root.geometry("400x550")
root.configure(bg=DARK_BG)
root.resizable(False, False)

card = tk.Frame(root, bg=CARD_BG, padx=20, pady=20, highlightthickness=1, highlightbackground="#334155")
card.place(relx=0.5, rely=0.5, anchor="center", width=350, height=480)

tk.Label(card, text="PASSWORD GEN", font=("Impact", 22), bg=CARD_BG, fg=ACCENT).pack(pady=10)

result_frame = tk.Frame(card, bg="#334155", padx=10, pady=10)
result_frame.pack(fill="x", pady=10)

result_entry = tk.Entry(result_frame, font=("Courier New", 16, "bold"), bd=0, bg="#334155", fg=TEXT_WHITE, justify="center")
result_entry.insert(0, "********")
result_entry.config(state="readonly")
result_entry.pack(fill="x")

strength_text = tk.Label(card, text="", font=("Arial", 9, "bold"), bg=CARD_BG, fg=TEXT_WHITE)
strength_text.pack()
strength_bg = tk.Frame(card, bg="#334155", height=5, width=300)
strength_bg.pack(pady=5)
strength_bar = tk.Frame(strength_bg, bg=ACCENT, height=5, width=0)
strength_bar.place(x=0, y=0)

tk.Label(card, text="Length:", font=("Arial", 10), bg=CARD_BG, fg=TEXT_WHITE).pack(anchor="w", padx=10)
len_slider = tk.Scale(card, from_=8, to=32, orient="horizontal", bg=CARD_BG, fg=ACCENT, highlightthickness=0, troughcolor="#334155")
len_slider.set(16)
len_slider.pack(fill="x", padx=10, pady=5)

options_frame = tk.Frame(card, bg=CARD_BG)
options_frame.pack(pady=10)

var_upper = tk.BooleanVar(value=True)
var_nums = tk.BooleanVar(value=True)
var_syms = tk.BooleanVar(value=False)

def create_check(text, var):
    return tk.Checkbutton(options_frame, text=text, variable=var, bg=CARD_BG, fg=TEXT_WHITE, 
                          selectcolor=DARK_BG, activebackground=CARD_BG, activeforeground=ACCENT, font=("Arial", 10))

create_check("Uppercase (A-Z)", var_upper).pack(anchor="w")
create_check("Numbers (0-9)", var_nums).pack(anchor="w")
create_check("Symbols (!@#)", var_syms).pack(anchor="w")

gen_btn = tk.Button(card, text="GENERATE", command=generate_password, bg=ACCENT, fg=DARK_BG, 
                    font=("Arial", 12, "bold"), bd=0, height=2, cursor="hand2", activebackground=TEXT_WHITE)
gen_btn.pack(fill="x", pady=(20, 5))

copy_btn = tk.Button(card, text="COPY", command=copy_pass, bg=CARD_BG, fg=ACCENT, 
                     font=("Arial", 10, "bold"), bd=0, cursor="hand2")
copy_btn.pack()

root.mainloop()
