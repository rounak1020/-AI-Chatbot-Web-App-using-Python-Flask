from chatterbot import ChatBot

bot = ChatBot("math", logic_adapters=["chatterbot.logic.MathematicalEvaluation"])

print("---------Math ChatBot---------")

while True:
    user_text = input("type the math equation that you want to solve:")
    print("chatbot:"+ str(bot.get_response(user_text)))