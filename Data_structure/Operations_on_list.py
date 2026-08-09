fruits = ["Apple", "Mango", "Banana", "Orange", "Grapes"]
print("Original list:")
print(fruits)
print("Number of fruits:", fruits [0])
print("Last fruits:", fruits[-1])
fruits.append("Watermelon")
print("After adding Watermelon:")
print(fruits)
fruits.insert(2, "Pineapple")
print("After inserting Pineapple:")
print(fruits)
fruits.remove("Banana")
print("After removing Banana:")
print(fruits)
if "Mango" in fruits:
    print("Mango is in the list. ")
else:
    print("Mango is not in the list. ")
fruits.sort()
print("Sorted list: ")
print(fruits)
fruits.reverse()
print("Reversed list: ")
print(fruits)
print("All fruits: ")
for fruit in fruits:
    print(fruit)
    