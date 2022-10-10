from chatterbot import chatbot
from chatterbot.trainer import chatterbotcorpusTrainer

chatbot = chatbot('bot')
trainer = chatterbotcorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

while True:
    query = str(input(" >>"))
    print(chatbot.get_responcse(query))
    if"exit" in query:
        break
    