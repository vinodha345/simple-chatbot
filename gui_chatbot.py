from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import tkinter as tk

bot = ChatBot("SympoBot")
trainer = ListTrainer(bot)

conversation = [
    "Hi","Hello there!",
    "What is your name?","I am sympoBot,your symposium assistant.",
    "It's a student event where ideas and projects are shared.",
    "Bye","Goodbye! All the best!"
]
trainer.train(conversation)                 

root = tk.Tk()
root.title("SympoBot")

chat_log = tk.Text(root, height=20,
width=60, bg="white")
chat_log.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(side=tk.LEFT, padx=10,pady=10)

def respond():
    user_input = entry.get()
    response = bot.get_response(user_input)
    chat_log.insert(tk.END, f"You:{user_input}\nBot: {response}\n\n")
    entry.delete(0, tk.END)


send_button = tk.Button(root,text="Send", command=respond)
send_button.pack(side=tk.LEFT)
root.mainloop()
