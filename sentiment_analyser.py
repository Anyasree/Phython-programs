from textblob import TextBlob
import colorama
from colorama import Fore, Style

colorama.init(autoreset = True)

user_name = ""

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity


    if sentiment > 0.75:

        return f"\n{Fore.GREEN}Very Positive Sentiment Detected, Agent {user_name}! (score: {sentiment:.2f})"
        
    elif 0.25 < sentiment <= 0.75:

        return f"\n{Fore.GREEN} Positive Sentiment Detected, Agent {user_name}! (score: {sentiment:.2f})"
    
    elif -0.25 <= sentiment <= 0.25:

        return f"\n{Fore.YELLOW} Neutral Sentiment Detected, Agent {user_name}! (score: {sentiment:.2f})"
    
    elif -0.75 <= sentiment < -0.25:

        return f"\n{Fore.YELLOW} Neutral Sentiment Detected, Agent {user_name}! (score: {sentiment:.2f})"

    elif -0.75 <= sentiment < -0.25:

        return f"\n{Fore.RED} Negative Sentiment Detected, Agent {user_name}! (score: {sentiment:.2f})"

    else:

        return f"\n{Fore.RED}Very Negative Sentiment Detected, Agent {user_name}! (score: {sentiment:.2f})"

text = input("Enter Text that you want to check.")
result = analyze_sentiment(text)
print(result)
