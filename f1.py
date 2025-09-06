print("Hi, I am your friendly bot!")
name = input("What is your name?")
print(f"You have an amazing name, {name}!")
print("How are you feeling?")
feeling = input().lower()
if feeling in["good", "fine", "great"]:
    print("Thats good to know")

else:
    print("I hope your day gets better.")

sport = input("What is favorite sport?")
print("Thats also my favorite sport!!!")

from textblob import TextBlob

def get_mood_from_text(text):
    analysis = TextBlob(text)

    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Postive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

input1 = input("Type a statement and i will tell you your mood")
mood = get_mood_from_text(input1)
print("Your mood is", mood)