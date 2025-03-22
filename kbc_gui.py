import tkinter as tk
from tkinter import messagebox, font

class KBCGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Kaun Banega Crorepati")
        self.root.geometry("800x600")
        self.root.configure(bg="#000044")
        
        self.questions = [
            {
                "question": "Who was the first President of the United States?",
                "options": ["Abraham Lincoln", "George Washington", "John F. Kennedy", "Thomas Jefferson"],
                "correct": 1,
                "prize": "1,000"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "options": ["Earth", "Jupiter", "Mars", "Venus"],
                "correct": 2,
                "prize": "2,000"
            },
            {
                "question": "What is the capital of France?",
                "options": ["London", "Rome", "Berlin", "Paris"],
                "correct": 3,
                "prize": "5,000"
            },
            {
                "question": "Who wrote the play 'Romeo and Juliet'?",
                "options": ["Charles Dickens", "William Shakespeare", "George Orwell", "Mark Twain"],
                "correct": 1,
                "prize": "10,000"
            },
            {
                "question": "What is the largest ocean on Earth?",
                "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
                "correct": 3,
                "prize": "50,000"
            },
            {
                "question": "Who was the first woman to win a Nobel Prize?",
                "options": ["Marie Curie", "Florence Nightingale", "Mother Teresa", "Ada Lovelace"],
                "correct": 0,
                "prize": "1 Crore"
            }
        ]
        
        self.current_question = 0
        self.correct_answers = 0
        
        # GUI Elements
        self.main_frame = tk.Frame(root, bg="#000044")
        self.main_frame.pack(pady=50)
        
        self.question_label = tk.Label(
            self.main_frame,
            text="",
            wraplength=600,
            bg="#000044",
            fg="white",
            font=("Helvetica", 16, "bold")
        )
        self.question_label.pack(pady=20)
        
        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(
                self.main_frame,
                text="",
                width=40,
                height=2,
                bg="#004080",
                fg="white",
                font=("Helvetica", 12),
                command=lambda i=i: self.check_answer(i)
            )
            btn.pack(pady=5)
            self.option_buttons.append(btn)
        
        self.score_label = tk.Label()
        root,
        text="Prize Money: ₹0",
        bg="#000044",
        fg="gold",
        ont=("Helvetica", 14, "bold")
        self.score_label.pack(side="bottom", pady=20)
        
        self.load_question()
    
    def load_question(self):
        if self.current_question < len(self.questions):
            q = self.questions[self.current_question]
            self.question_label.config(text=q["question"])
            for i, option in enumerate(q["options"]):
                self.option_buttons[i].config(text=f"{chr(65+i)}) {option}")
            self.score_label.config(text=f"Current Prize: ₹{q['prize']}")
        else:
            self.show_result()
    
    def check_answer(self, selected):
        q = self.questions[self.current_question]
        if selected == q["correct"]:
            self.correct_answers += 1
            messagebox.showinfo("Correct!", "Sahi Jawaab! 🎉")
        else:
            messagebox.showerror("Wrong", f"Galat Jawaab! Correct answer: {q['options'][q['correct']]}")
        
        self.current_question += 1
        self.load_question()
    
    def show_result(self):
        self.main_frame.destroy()
        result_frame = tk.Frame(self.root, bg="#000044")
        result_frame.pack(pady=100)
        
        if self.correct_answers == len(self.questions):
            text = "Badhai Ho! Aap Jeet Gaye!\n₹7 Crore!"
            color = "gold"
        elif self.correct_answers > 0:
            text = f"Aapne {self.correct_answers} Sawal Sahi Jawab Diye!\n₹1 Crore!"
            color = "lightgreen"
        else:
            text = "Aby ja BSDk tery bs ki baat ni crore patti bnnna!"
            color = "red"
        
        tk.Label(
            result_frame,
            text=text,
            font=("Helvetica", 18, "bold"),
            bg="#000044",
            fg=color
        ).pack(pady=20)
        
        tk.Button(
            result_frame,
            text="Play Again",
            command=self.restart_game,
            bg="#004080",
            fg="white",
            font=("Helvetica", 14)
        ).pack(pady=20)
    
    def restart_game(self):
        self.root.destroy()
        root = tk.Tk()
        KBCGame(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    game = KBCGame(root)
    root.mainloop()