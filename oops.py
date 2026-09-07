# oops in python 
#oops - object oriented programming
# student details
#class 
"""Remember & Match: a calm memory game designed for older adults.

Run with: python oops.py
"""

import random
import tkinter as tk
from tkinter import messagebox


class MemoryGame:
    """A gentle matching game with large controls and optional support."""

    PAIRS = ("TEA", "BOOK", "FLOWER", "MUSIC", "HOME", "SUN")
    COLORS = ("#f6d365", "#9ad7d8", "#f7b2ad", "#c8b6e8", "#b8d99b", "#f4c2a1")
    CARD_BACK = "#315c68"
    TEXT = "#173b43"

    def __init__(self, root):
        self.root = root
        self.root.title("Remember and Match")
        self.root.configure(bg="#fffaf0")
        self.root.minsize(720, 680)
        self.cards = []
        self.open_cards = []
        self.matched = set()
        self.level = 1
        self.pair_count = 3
        self.reward_count = 0
        self.moves = 0
        self.busy = False
        self.status = None
        self.buttons = []
        self.build_screen()
        self.new_game()

    def build_screen(self):
        header = tk.Frame(self.root, bg="#fffaf0")
        header.pack(fill="x", padx=36, pady=(28, 8))

        tk.Label(
            header,
            text="Remember and Match",
            font=("Georgia", 30, "bold"),
            fg=self.TEXT,
            bg="#fffaf0",
        ).pack(anchor="w")
        tk.Label(
            header,
            text="Take your time. Find two cards that are the same.",
            font=("Arial", 17),
            fg="#49636a",
            bg="#fffaf0",
        ).pack(anchor="w", pady=(4, 0))

        self.status = tk.Label(
            self.root,
            text="",
            font=("Arial", 18, "bold"),
            fg=self.TEXT,
            bg="#fffaf0",
            height=2,
        )
        self.status.pack(fill="x", padx=36)

        self.level_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 16, "bold"),
            fg="#49636a",
            bg="#fffaf0",
        )
        self.level_label.pack(fill="x", padx=36)

        self.reward_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 16, "bold"),
            fg="#9a6418",
            bg="#fffaf0",
        )
        self.reward_label.pack(fill="x", padx=36)

        board = tk.Frame(self.root, bg="#fffaf0")
        board.pack(expand=True, padx=36, pady=8)
        for index in range(12):
            button = tk.Button(
                board,
                text="?",
                font=("Arial", 25, "bold"),
                width=9,
                height=3,
                bg=self.CARD_BACK,
                fg="white",
                activebackground="#477d87",
                activeforeground="white",
                relief="flat",
                bd=0,
                command=lambda card_index=index: self.choose(card_index),
            )
            button.grid(row=index // 4, column=index % 4, padx=8, pady=8, sticky="nsew")
            self.buttons.append(button)

        controls = tk.Frame(self.root, bg="#fffaf0")
        controls.pack(fill="x", padx=36, pady=(4, 30))
        tk.Button(
            controls,
            text="Show Again",
            font=("Arial", 17, "bold"),
            bg="#f0c36a",
            fg=self.TEXT,
            activebackground="#e2ad4e",
            relief="flat",
            padx=18,
            pady=10,
            command=self.show_again,
        ).pack(side="left")
        tk.Button(
            controls,
            text="New Game",
            font=("Arial", 17, "bold"),
            bg="#315c68",
            fg="white",
            activebackground="#477d87",
            relief="flat",
            padx=18,
            pady=10,
            command=self.new_game,
        ).pack(side="right")

    def new_game(self):
        self.level = 1
        self.reward_count = 0
        self.start_level()

    def start_level(self):
        self.pair_count = min(2 + self.level, len(self.PAIRS))
        self.cards = list(self.PAIRS[: self.pair_count]) * 2
        random.shuffle(self.cards)
        self.open_cards = []
        self.matched = set()
        self.moves = 0
        self.busy = False
        for index, button in enumerate(self.buttons):
            if index < len(self.cards):
                button.grid()
                button.configure(text="?", bg=self.CARD_BACK, state="normal", relief="flat")
            else:
                button.grid_remove()
        self.level_label.configure(text=f"Level {self.level} of 4   |   {self.pair_count} pairs")
        self.reward_label.configure(text=f"Rewards earned: {self.reward_count} stars")
        self.status.configure(text="Choose any card to begin.")

    def choose(self, index):
        if self.busy or index in self.matched or index in self.open_cards:
            return
        self.open_cards.append(index)
        self.buttons[index].configure(
            text=self.cards[index],
            bg=self.COLORS[self.PAIRS.index(self.cards[index])],
            fg=self.TEXT,
        )
        if len(self.open_cards) == 1:
            self.status.configure(text="Now find the card that matches it.")
        else:
            self.moves += 1
            self.busy = True
            self.root.after(850, self.check_pair)

    def check_pair(self):
        first, second = self.open_cards
        if self.cards[first] == self.cards[second]:
            self.matched.update((first, second))
            for index in (first, second):
                self.buttons[index].configure(state="disabled", relief="sunken")
            self.status.configure(text="Good match. Keep going when you are ready.")
        else:
            for index in (first, second):
                self.buttons[index].configure(text="?", bg=self.CARD_BACK, fg="white")
            self.status.configure(text="That is okay. Try another pair.")
        self.open_cards = []
        self.busy = False
        if len(self.matched) == len(self.cards):
            self.status.configure(text=f"Wonderful! You finished in {self.moves} turns.")
            level_reward = self.level
            self.reward_count += level_reward
            self.reward_label.configure(text=f"Rewards earned: {self.reward_count} stars")
            if self.level < 4:
                messagebox.showinfo(
                    "Level complete",
                    f"You found every pair!\n\n"
                    f"Reward: {level_reward} star{'s' if level_reward != 1 else ''}\n\n"
                    f"Now let us try Level {self.level + 1}.",
                )
                self.level += 1
                self.start_level()
            else:
                messagebox.showinfo(
                    "Well done",
                    f"You completed every level!\n\n"
                    f"Your reward: {self.reward_count} stars\n"
                    "You are a Memory Champion!",
                )

    def show_again(self):
        if self.busy or self.open_cards:
            return
        remaining = [index for index in range(len(self.cards)) if index not in self.matched]
        if not remaining:
            return
        self.busy = True
        for index in remaining:
            self.buttons[index].configure(
                text=self.cards[index],
                bg=self.COLORS[self.PAIRS.index(self.cards[index])],
                fg=self.TEXT,
            )
        self.status.configure(text="Here is a little reminder. Look carefully.")
        self.root.after(1800, self.hide_unmatched)

    def hide_unmatched(self):
        for index in range(len(self.cards)):
            if index not in self.matched:
                self.buttons[index].configure(text="?", bg=self.CARD_BACK, fg="white")
        self.busy = False
        self.status.configure(text="Choose any card when you are ready.")


if __name__ == "__main__":
    app = tk.Tk()
    MemoryGame(app)
    app.mainloop()

