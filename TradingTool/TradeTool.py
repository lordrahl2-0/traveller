import tkinter as tk
from tkinter import messagebox
import random


class TravellerTradeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Traveller Trade Automation")

        # Dice Roll Input
        self.dice_label = tk.Label(root, text="Enter Dice Roll (or press Roll)")
        self.dice_label.pack()

        self.dice_entry = tk.Entry(root)
        self.dice_entry.pack()

        self.roll_button = tk.Button(root, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack()

        # Trade Category Selection
        self.category_label = tk.Label(root, text="Select Trade Category")
        self.category_label.pack()

        self.trade_categories = ["Common Goods", "Luxury Items", "Industrial Materials"]
        self.category_var = tk.StringVar(root)
        self.category_var.set(self.trade_categories[0])

        self.category_menu = tk.OptionMenu(
            root, self.category_var, *self.trade_categories
        )
        self.category_menu.pack()

        # Calculate Trade Button
        self.calculate_button = tk.Button(
            root, text="Calculate Trade", command=self.calculate_trade
        )
        self.calculate_button.pack()

        # Output Field
        self.output_text = tk.Text(root, height=10, width=50)
        self.output_text.pack()

    def roll_dice(self):
        roll = random.randint(2, 12)
        self.dice_entry.delete(0, tk.END)
        self.dice_entry.insert(0, str(roll))

    def calculate_trade(self):
        try:
            dice_roll = int(self.dice_entry.get())
            category = self.category_var.get()
            trade_result = f"Trade calculation for roll {dice_roll} in category {category}: (Placeholder calculations)"

            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, trade_result)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number")


if __name__ == "__main__":
    root = tk.Tk()
    app = TravellerTradeGUI(root)
    root.mainloop()
