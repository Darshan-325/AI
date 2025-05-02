from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Initialize the chatbot
bot = ChatBot('Bot')
trainer = ListTrainer(bot)

# Train the bot with multiple inputs
trainer.train([
    "Hi, can I help you",
    "Who are you?",
    "I am your virtual assistant. Ask me any questions...",
    "Where do you operate?",
    "We operate from Singapore",
    "What payment methods do you accept?",
    "We accept debit cards and major credit cards",
    "I would like to speak to your customer service agent",
    "please call +65 3333 3333. Our operating hours are from 9am to 5pm, Monday to Friday"
])

trainer.train([
    "What payment methods do you offer?",
    "We accept debit cards and major credit cards",
    "How to contact customer service agent",
    "please call +65 3333 3333. Our operating hours are from 9am to 5pm, Monday to Friday"
])


while True:
    request = input('you : ')
    if request.lower() == 'ok' or request.lower() == 'bye':
        print('Bot: bye')
        break
    response = bot.get_response(request)
    print('Bot:', response)
