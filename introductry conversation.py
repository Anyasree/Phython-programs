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
