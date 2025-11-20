# 💬🤖simple-chatbot
# 🤖 SympoBot – A Simple Tkinter ChatBot
SympoBot is a lightweight desktop chatbot application built using Python, ChatterBot, and Tkinter.
It can respond to basic user queries and is designed to act as a symposium assistant.

# 📌 Features

.🗣️ Chat with SympoBot using a simple GUI
.⚡ Trained using ChatterBot’s ListTrainer
.💬 Displays user and bot messages inside a chat window
.🪟 Built using Python’s Tkinter library
.🧠 Easy to modify and train with your own conversation data

# 🛠️ Technologies Used
1.Python 3
2.Tkinter (GUI)
3.ChatterBot
4.ChatterBot Corpus

# 📂 Project Setup
# 1. Install Dependencies
Make sure you have Python 3 installed, then run:
#bash
pip install chatterbot chatterbot-corpus


# ⚠️ If ChatterBot installation gives errors, install the specific compatible version:
#bash
pip install chatterbot==1.0.4

# ▶️ How to Run the Bot
Save the script as sympobot.py
Run the program:
#bash
python sympobot.py

The Tkinter window will open, and you can start chatting with SympoBot.

# 🧠 Training Data
The bot is trained using a simple conversation list:
#python
conversation = [
    "Hi","Hello there!",
    "What is your name?","I am sympoBot, your symposium assistant.",
    "It's a student event where ideas and projects are shared.",
    "Bye","Goodbye! All the best!"
]


You can add more lines to customize the bot’s knowledge.
