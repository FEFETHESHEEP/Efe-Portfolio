import tkinter as tk
import random
import time
import threading

snippets = [
    "def greet(name):\n    return f\"Hello, {name}!\"",
    "for i in range(5):\n    print(i * i)",
    "import math\nprint(math.pi)",
    "def add(a, b):\n    return a + b",
    "numbers = [1, 2, 3, 4]\nsquares = [x**2 for x in numbers]",
    "from datetime import datetime\nprint(datetime.now())",
    "try:\n    x = 10 / 0\nexcept ZeroDivisionError:\n    print(\"Oops!\")",
    "class Dog:\n    def __init__(self, name):\n        self.name = name\n    def bark(self):\n        print(f\"{self.name} says woof!\")",
]

def generate_random_code():
    chosen = random.sample(snippets, k=random.randint(3, 6))
    return "\n\n".join(chosen)

def type_text(widget, text, delay=0.02):
    widget.delete("1.0", tk.END)
    def writer():
        for char in text:
            widget.insert(tk.END, char)
            widget.update()
            time.sleep(delay)
    threading.Thread(target=writer).start()

def launch_writer_window():
    window = tk.Tk()
    window.title("")
    window.geometry("800x600")

    text = tk.Text(window, font=("Courier New", 12), bg="black", fg="lime", insertbackground="white")
    text.pack(expand=True, fill="both", padx=10, pady=10)

    code = generate_random_code()
    type_text(text, code)

    window.mainloop()

launch_writer_window()