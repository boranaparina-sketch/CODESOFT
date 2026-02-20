import tkinter as tk
from tkinter import messagebox

COLOR_BG = "#121212"          
COLOR_CARD = "#1E1E1E"        
COLOR_ACCENT = "#BB86FC"      
COLOR_TEXT = "#E1E1E1"        
COLOR_OP = "#03DAC6"          

class ModernCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Aero Calc")
        self.root.geometry("360x560")
        self.root.configure(bg=COLOR_BG)
        
        self.equation = ""
        
        # --- Display Section ---
        self.display_frame = tk.Frame(self.root, bg=COLOR_BG, pady=20)
        self.display_frame.pack(expand=True, fill="both")

        self.label_small = tk.Label(self.display_frame, text="", font=("Arial", 12), bg=COLOR_BG, fg=COLOR_OP, anchor="e")
        self.label_small.pack(fill="x", padx=25)

        self.label_main = tk.Label(self.display_frame, text="0", font=("Arial", 42, "bold"), bg=COLOR_BG, fg=COLOR_TEXT, anchor="e")
        self.label_main.pack(fill="x", padx=20)

        self.buttons_frame = tk.Frame(self.root, bg=COLOR_CARD, padx=10, pady=20)
        self.buttons_frame.pack(fill="both", expand=True)
        
        btns = [
            ['C', '±', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', 'DEL', '=']
        ]

        for r, row in enumerate(btns):
            for c, char in enumerate(row):
                self.create_button(char, r, c)

    def create_button(self, text, r, c):
        fg_col = COLOR_TEXT
        if text in ['/', '*', '-', '+', '=']:
            fg_col = COLOR_OP
        elif text in ['C', '±', '%', 'DEL']:
            fg_col = COLOR_ACCENT

        btn = tk.Button(self.buttons_frame, text=text, font=("Arial", 16, "bold"),
                        bg=COLOR_CARD, fg=fg_col, bd=0, activebackground="#333333",
                        activeforeground=fg_col, width=4, height=2,
                        command=lambda x=text: self.on_click(x))
        btn.grid(row=r, column=c, sticky="nsew", padx=5, pady=5)
        
        btn.bind("<Enter>", lambda e: btn.config(bg="#252525"))
        btn.bind("<Leave>", lambda e: btn.config(bg=COLOR_CARD))
        
        self.buttons_frame.grid_columnconfigure(c, weight=1)
        self.buttons_frame.grid_rowconfigure(r, weight=1)

    def on_click(self, char):
        if char == "C":
            self.equation = ""
            self.label_small.config(text="")
            self.label_main.config(text="0")
        elif char == "DEL":
            self.equation = self.equation[:-1]
            self.label_main.config(text=self.equation if self.equation else "0")
        elif char == "=":
            try:
                formatted_eq = self.equation.replace('×', '*').replace('÷', '/')
                result = str(eval(formatted_eq))
                self.label_small.config(text=self.equation + " =")
                self.label_main.config(text=result)
                self.equation = result
            except:
                messagebox.showerror("Error", "Invalid Format")
                self.equation = ""
        else:
            if self.label_main.cget("text") == "0" or self.equation == "":
                self.equation = str(char)
            else:
                self.equation += str(char)
            self.label_main.config(text=self.equation)

if __name__ == "__main__":
    root = tk.Tk()
    try:
        root.attributes('-alpha', 0.96) 
    except: pass
    
    ModernCalculator(root)
    root.mainloop()
