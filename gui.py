"""Quick-Calc: Tkinter GUI for calculator."""

import tkinter as tk
from tkinter import messagebox
from calculator import Calculator


class CalculatorApp:
    """Tkinter GUI for Quick-Calc calculator."""

    def __init__(self, root):
        self.calc = Calculator()
        self.root = root
        self.root.title("Quick-Calc")
        self.root.geometry("300x400")
        self.root.resizable(False, False)

        self.display_var = tk.StringVar(value="0")
        self.create_widgets()

    def create_widgets(self):
        display_frame = tk.Frame(self.root, padx=10, pady=10)
        display_frame.pack(fill=tk.BOTH)

        display = tk.Entry(
            display_frame,
            textvariable=self.display_var,
            font=("Arial", 24),
            justify="right",
            state="readonly",
        )
        display.pack(fill=tk.BOTH)

        buttons_frame = tk.Frame(self.root, padx=10, pady=10)
        buttons_frame.pack(fill=tk.BOTH, expand=True)

        buttons = [
            ("C", 0, 0, lambda: self.on_clear()),
            ("/", 0, 1, lambda: self.on_operator("/")),
            ("*", 0, 2, lambda: self.on_operator("*")),
            ("-", 0, 3, lambda: self.on_operator("-")),
            ("7", 1, 0, lambda: self.on_digit("7")),
            ("8", 1, 1, lambda: self.on_digit("8")),
            ("9", 1, 2, lambda: self.on_digit("9")),
            ("+", 1, 3, lambda: self.on_operator("+")),
            ("4", 2, 0, lambda: self.on_digit("4")),
            ("5", 2, 1, lambda: self.on_digit("5")),
            ("6", 2, 2, lambda: self.on_digit("6")),
            ("=", 2, 3, lambda: self.on_equals(), 2),
            ("1", 3, 0, lambda: self.on_digit("1")),
            ("2", 3, 1, lambda: self.on_digit("2")),
            ("3", 3, 2, lambda: self.on_digit("3")),
            ("0", 4, 0, lambda: self.on_digit("0")),
            (".", 4, 1, lambda: self.on_decimal()),
        ]

        for btn in buttons:
            text = btn[0]
            row = btn[1]
            col = btn[2]
            command = btn[3]
            colspan = btn[4] if len(btn) > 4 else 1

            tk.Button(
                buttons_frame,
                text=text,
                font=("Arial", 18),
                width=5 * colspan,
                command=command,
            ).grid(
                row=row, column=col, columnspan=colspan, sticky="nsew", padx=3, pady=3
            )

        for i in range(5):
            buttons_frame.rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.columnconfigure(i, weight=1)

    def on_digit(self, digit):
        result = self.calc.input_digit(digit)
        self.display_var.set(result)

    def on_operator(self, operator):
        self.calc.set_operator(operator)

    def on_equals(self):
        try:
            result = self.calc.calculate()
            self.display_var.set(result)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            self.display_var.set("0")

    def on_clear(self):
        result = self.calc.clear()
        self.display_var.set(result)

    def on_decimal(self):
        if "." not in self.calc.current_input:
            self.calc.current_input += "."
            self.display_var.set(self.calc.current_input)


def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
