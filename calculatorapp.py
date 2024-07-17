# Calculator App

import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.entry = tk.Entry(self.root, width=25, borderwidth=5, font=("Arial", 16))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.root, text=button, width=5, height=2, font=("Arial", 14), command=lambda button=button: self.click_button(button)).grid(row=row_val, column=col_val, padx=3, pady=3)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        tk.Button(self.root, text="Clear", width=14, height=1, font=("Arial", 14), command=self.clear).grid(row=row_val, column=0, columnspan=4, padx=3, pady=3)

        tk.Button(self.root, text="Backspace", width=11, height=1, font=("Arial", 14), command=self.backspace).grid(row=row_val+1, column=0, columnspan=2, padx=3, pady=3)

        tk.Button(self.root, text="Square Root", width=11, height=1, font=("Arial", 14), command=self.sqrt).grid(row=row_val+1, column=2, columnspan=2, padx=3, pady=3)

    def click_button(self, button):
        if button == '=':
            try:
                result = str(eval(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, button)

    def clear(self):
        self.entry.delete(0, tk.END)

    def backspace(self):
        self.entry.delete(len(self.entry.get())-1, tk.END)

    def sqrt(self):
        try:
            result = str(eval(self.entry.get() + "**0.5"))
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
        except Exception as e:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(background="light gray")  # Set the background color of the root window
    app = CalculatorApp(root)
    root.mainloop()