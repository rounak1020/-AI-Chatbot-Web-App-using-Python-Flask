from chatterbot import ChatBot

bot = ChatBot("units", logic_adapters=["chatterbot.logic.UnitConversion"])

while True:
    user_text = input("ask a question(unit conversion):")
    chatbot_response = str(bot.get_response(user_text))
    print("chatbot: ", chatbot_response)