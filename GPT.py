import tkinter as tk
from tkinter import scrolledtext
from transformers import pipeline
import threading

# Model yüklemesi
generator = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")

# Konuşma geçmişi
conversation = []

# Yapay zekanın cevabını oluşturma fonksiyonu
def generate_reply(prompt):
    response = generator(
        prompt,
        max_new_tokens=60,
        num_return_sequences=1,
        pad_token_id=50256,
        temperature=0.7,
        top_k=50,
        top_p=0.9
    )
    reply = response[0]["generated_text"][len(prompt):].strip()
    return reply

# Kullanıcıdan gelen mesaja tepki verme fonksiyonu
def handle_response(user_input):
    conversation.append(f"You: {user_input}")

    recent_history = conversation[-6:]
    prompt = "\n".join(recent_history) + "\nAI:"

    reply = generate_reply(prompt)

    chat_history.insert(tk.END, f"AI: {reply}\n\n", "ai")
    chat_history.yview(tk.END)

    conversation.append(f"AI: {reply}")

# Mesaj gönderme işlevi (butona basıldığında çalışır)
def send_message():
    user_input = entry.get()
    if not user_input.strip():
        return

    chat_history.insert(tk.END, f"You: {user_input}\n", "user")
    entry.delete(0, tk.END)
    window.update()

    # Cevap üretimini ayrı bir thread içinde yapalım ki arayüz donmasın
    threading.Thread(target=handle_response, args=(user_input,)).start()

# Tkinter arayüzü
window = tk.Tk()
window.title("Basit GPT Sohbet Arayüzü")

chat_history = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=80, height=20)
chat_history.pack(padx=10, pady=10)
chat_history.tag_config("user", foreground="blue")
chat_history.tag_config("ai", foreground="green")

entry = tk.Entry(window, width=80)
entry.pack(padx=10, pady=(0, 10))
entry.bind("<Return>", lambda event: send_message())

send_button = tk.Button(window, text="Gönder", command=send_message)
send_button.pack()

window.mainloop()
