import os
import tkinter as tk
from tkinter import scrolledtext
from threading import Thread
from dotenv import load_dotenv
import openai as OpenAI

# Load API key
load_dotenv()
client = OpenAI(api_key=("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"))

# Conversation history
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

# ---- Functions ----
def generate_reply(user_input, chat_box):
    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-4o",   
            messages=messages,
            temperature=0.7,
        )
        reply = response.choices[0].message.content
    except Exception as e:
        reply = f"⚠️ Error: {e}"

    messages.append({"role": "assistant", "content": reply})

    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"Assistant: {reply}\n\n", "assistant")
    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)

def handle_send(entry, chat_box):
    user_input = entry.get().strip()
    if not user_input:
        return
    entry.delete(0, tk.END)

    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, f"You: {user_input}\n", "user")
    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)

    Thread(target=generate_reply, args=(user_input, chat_box), daemon=True).start()

# ---- GUI ----
def main():
    window = tk.Tk()
    window.title("ChatGPT GUI")
    window.geometry("600x500")

    chat_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, state=tk.DISABLED)
    chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    chat_box.tag_config("user", foreground="blue")
    chat_box.tag_config("assistant", foreground="green")

    entry = tk.Entry(window, width=80)
    entry.pack(padx=10, pady=(0, 10), side=tk.LEFT, fill=tk.X, expand=True)

    send_button = tk.Button(window, text="Send", command=lambda: handle_send(entry, chat_box))
    send_button.pack(padx=10, pady=(0, 10), side=tk.RIGHT)

    window.mainloop()

if __name__ == "__main__":
    main()
