print("Hi, I am your friendly bot!")

name = input("What is your name?")
print(f"That is a nice name, {name}!")

birthyear = int(input("What is your Birthyear?"))
age = 2025 - birthyear
print(f"Your age is, {age}")

if age > 30:
    print("Your age is more that 30!")

elif age < 30:
    print("Your age is less than 30!")

else:
    print("Your age is 30")

marks = []
for i in range(3):
    m = int(input("Enter marks: "))
    marks.append(m)

print(marks)

sum = 0
for m in marks:
    sum = sum + m

print(f"sum = {sum}")

perc = sum / 300 * 100
print(f"Your percentage is {perc}!")

if perc > 90:
    grade = 'A'

elif perc >= 70 and perc <= 90:
    grade = 'B'

elif perc >= 50 and perc <= 70:
    grade = 'C'

elif perc >= 30 and perc <= 50:
    grade = 'D'

else:
    grade = 'E'
print(f"Your grade is {grade}")

feel = input("How do you feel after getting your grade?")

from textblob import TextBlob
def sentiment_analysis(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score < 0:
        print("negative_senitiment_detector")

    elif sentiment_score > 0:
        print("positive_sentiment_detected")

    else:
        print("neutral_sentiment_detected")

sentiment_analysis(feel)
