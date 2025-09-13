from textblob import TextBlob
from colorama import Fore, init, Style, Back

init()

review = input(Fore.RED+Back.LIGHTYELLOW_EX+"How was your week? 😊 "+Style.RESET_ALL)
reviewblob = TextBlob(review)
polarity = reviewblob.sentiment.polarity
if polarity > 0:
    print(Fore.GREEN+Back.LIGHTWHITE_EX+"That's amazing 🏆 ,then you can go to the beach!"+Style.RESET_ALL)

elif polarity < 0:
    print(Fore.BLUE+Back.LIGHTRED_EX+"I hope your coming week will be better! Meanwile you can watch a movie:)"+Style.RESET_ALL)

else:
    print(Fore.LIGHTMAGENTA_EX+Back.LIGHTCYAN_EX+"Let's hope for the best 💕 !Read an inspirational book 👍 "+Style.RESET_ALL)
