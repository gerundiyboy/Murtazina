import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.expression = ""

        self.entry = tk.Entry(root, font=("Arial", 18), bd=10, relief=tk.RIDGE, justify="right")
        self.entry.grid(row=0, column=0, columnspan=5, sticky="nsew")

        buttons = [
            ('C', 1, 0), ('←', 1, 1), ('(', 1, 2), (')', 1, 3), ('/', 1, 4),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3), ('atg', 2, 4),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3), ('=', 3, 4),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 1)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
        for i in range(5):
            root.grid_columnconfigure(i, weight=1)

    def create_button(self, text, row, col):
        button = tk.Button(self.root, text=text, font=("Arial", 14),
                           command=lambda: self.on_click(text))
        button.grid(row=row, column=col, sticky="nsew")

    def on_click(self, char):
        operators = "+-*/"

        if char == "C":
            self.expression = ""

        elif char == "←":
            self.expression = self.expression[:-1]

        elif char == "=":
            self.calculate()
            return

        elif char == "atg":
            self.expression += "atg("

        elif char in operators:
            if not self.expression:
                # Только минус можно в начале
                if char == "-":
                    self.expression = "-"
                return
