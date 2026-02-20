import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌟 Modern To-Do List")
        self.root.geometry("420x520")
        self.root.configure(bg="#D4D0D0")  
        self.root.resizable(False, False)

        self.tasks = []

        
        tk.Label(root, text="📝 TO-DO LIST", font=("Helvetica", 22, "bold"),
                 bg="#D4D0D0", fg="#0F1110").pack(pady=15)

        
        entry_frame = tk.Frame(root, bg="#DBD8D8")
        entry_frame.pack(pady=10)

        self.task_entry = tk.Entry(entry_frame, font=("Helvetica", 14), width=20, bd=0,
                                   fg="#ffffff", bg="#1e1e1e", insertbackground="#ffffff")
        self.task_entry.pack(side="left", padx=(0,10))
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        add_btn = tk.Button(entry_frame, text="ADD", command=self.add_task,
                            bg="#00fa9a", fg="#121212", bd=0, width=8,
                            font=("Helvetica", 12, "bold"), cursor="hand2")
        add_btn.pack(side="left")

        
        list_frame = tk.Frame(root, bg="#121212")
        list_frame.pack(pady=10)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(list_frame, font=("Helvetica", 14), width=30, height=15,
                                  bg="#1e1e1e", fg="#ffffff", selectbackground="#00e5ff",
                                  bd=0, highlightthickness=0, yscrollcommand=scrollbar.set)
        self.listbox.pack()
        scrollbar.config(command=self.listbox.yview)

        
        btn_frame = tk.Frame(root, bg="#121212")
        btn_frame.pack(pady=10)

        del_btn = tk.Button(btn_frame, text="DELETE", command=self.delete_task,
                            bg="#ff1744", fg="#ffffff", bd=0, width=10,
                            font=("Helvetica", 12, "bold"), cursor="hand2")
        del_btn.pack(side="left", padx=5)

        done_btn = tk.Button(btn_frame, text="MARK DONE", command=self.mark_done,
                             bg="#00e676", fg="#121212", bd=0, width=12,
                             font=("Helvetica", 12, "bold"), cursor="hand2")
        done_btn.pack(side="left", padx=5)

        clr_btn = tk.Button(btn_frame, text="CLEAR ALL", command=self.clear_all,
                            bg="#ff9100", fg="#121212", bd=0, width=10,
                            font=("Helvetica", 12, "bold"), cursor="hand2")
        clr_btn.pack(side="left", padx=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected)
        else:
            messagebox.showwarning("Warning", "Please select a task to delete!")

    def mark_done(self):
        selected = self.listbox.curselection()
        if selected:
            task = self.listbox.get(selected)
            if not task.startswith("✔️ "):
                self.listbox.delete(selected)
                self.listbox.insert(selected, "✔️ " + task)
        else:
            messagebox.showwarning("Warning", "Please select a task to mark done!")

    def clear_all(self):
        if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
            self.listbox.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
