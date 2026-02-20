import tkinter as tk
import random

class RPSGame:
    def __init__(self, root):
        self.root = root
        self.root.title("RPS Game - Modern Dark Theme")
        self.root.geometry("480x600")

        self.bg_color = "#121212"       
        self.sidebar_color = "#1e1e1e" 
        self.text_color = "#e0e0e0"     
        self.accent_color = "#00bcd4"   

        self.root.configure(bg=self.bg_color)
        self.user_score = 0
        self.cpu_score = 0
        self.choices = ["rock", "paper", "scissors"]
        self.icons = {"rock": "✊", "paper": "✋", "scissors": "✌️"}

        self.setup_ui()

    def setup_ui(self):
        # Header
        header = tk.Frame(self.root, bg=self.sidebar_color, height=40)
        header.pack(fill="x")
        tk.Label(header, text=" main.py > rock_paper_scissors", font=("Consolas", 10),
                 fg="#b0b0b0", bg=self.sidebar_color, padx=10).pack(side="left")

        # Title
        self.title_label = tk.Label(self.root, text="TERMINAL: RPS GAME",
                                    font=("Consolas", 20, "bold"), fg=self.accent_color,
                                    bg=self.bg_color, pady=20)
        self.title_label.pack()

        # Score Card
        self.score_label = tk.Label(self.root, text="USER_SCORE: 0  |  CPU_SCORE: 0",
                                    font=("Consolas", 14), fg=self.text_color, bg=self.bg_color)
        self.score_label.pack(pady=5)

        # Result Display
        self.result_display = tk.Label(self.root, text=">>> Waiting for input...",
                                       font=("Consolas", 12), fg=self.accent_color, bg=self.bg_color, pady=20)
        self.result_display.pack()

        # Battle Zone
        self.visual_frame = tk.Frame(self.root, bg="#1f1f1f")
        self.visual_frame.pack(pady=20)

        self.user_icon = tk.Label(self.visual_frame, text="❓", font=("Segoe UI Emoji", 60),
                                  bg="#1f1f1f", fg=self.text_color)
        self.user_icon.grid(row=0, column=0, padx=30)

        tk.Label(self.visual_frame, text="VS", font=("Consolas", 24, "bold"),
                 bg="#1f1f1f", fg=self.accent_color).grid(row=0, column=1)

        self.cpu_icon = tk.Label(self.visual_frame, text="🤖", font=("Segoe UI Emoji", 60),
                                 bg="#1f1f1f", fg=self.text_color)
        self.cpu_icon.grid(row=0, column=2, padx=30)

        # Buttons
        self.btn_frame = tk.Frame(self.root, bg=self.bg_color)
        self.btn_frame.pack(pady=30)

        self.create_button("ROCK", "#333333", "rock")
        self.create_button("PAPER", "#333333", "paper")
        self.create_button("SCISSORS", "#333333", "scissors")

        # Footer
        tk.Label(self.root, text="UTF-8  |  Python 3.10  |  Spaces: 4",
                 font=("Consolas", 9), fg="#b0b0b0", bg=self.sidebar_color).pack(side="bottom", fill="x")

    def create_button(self, text, color, choice):
        btn = tk.Button(self.btn_frame, text=text, width=12, height=2, bg=color,
                        fg=self.text_color, activebackground=self.accent_color,
                        activeforeground="#ffffff", font=("Consolas", 10, "bold"),
                        bd=0, cursor="hand2", command=lambda: self.play(choice))
        btn.pack(side="left", padx=5)

    def play(self, user_choice):
        cpu_choice = random.choice(self.choices)

        self.user_icon.config(text=self.icons[user_choice])
        self.cpu_icon.config(text=self.icons[cpu_choice])

        if user_choice == cpu_choice:
            res = "RESULT: DRAW"
            clr = "#fbc02d"   
        elif (user_choice == "rock" and cpu_choice == "scissors") or \
             (user_choice == "paper" and cpu_choice == "rock") or \
             (user_choice == "scissors" and cpu_choice == "paper"):
            res = "RESULT: YOU WIN"
            clr = "#00e676"  
            self.user_score += 1
        else:
            res = "RESULT: CPU WINS"
            clr = "#ff1744"  
            self.cpu_score += 1

        self.result_display.config(text=f">>> {res}", fg=clr)
        self.score_label.config(text=f"USER_SCORE: {self.user_score}  |  CPU_SCORE: {self.cpu_score}")


if __name__ == "__main__":
    root = tk.Tk()
    game = RPSGame(root)
    root.mainloop()
