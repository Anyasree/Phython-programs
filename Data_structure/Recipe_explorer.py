pasta = ("Pasta Arrabiata", "Italian", 20, "Medium")
biryani = ("Chicken Biryani", "Indian", 45, "Hard")
print("Recipe 1:", pasta)
print ("Name:", pasta[0])
print("Cuisine:", pasta[1])
print ("Difficulty:", pasta[-1])

all_recipes = (pasta, biryani)
print("\nFirst recipe name:", all_recipes[0][0])
print ("Second recipe time:", all_recipes [1][2], "mins")
print("Pasta details (sliced):", pasta[1:3])

print("\nPasta Recipe details:")
for detail in pasta:
    print(" -", detail)

pasta_ingredients = {"tomato", "garlic", "olive oil", " chilli", "pasta", "garlic"}
biryani_ingredients = {"rice", "chicken", "garlic", "onion", "tomato", "spices"}
print("\nPasta ingredients:", pasta_ingredients)
print("Biryani ingredients:", biryani_ingredients) 
print("Total pasta ingredients:", len(pasta_ingredients))

pasta_ingredients.add("parmesan")
pasta_ingredients.discard("chilli")
print("\nUpdated pasta ingredients:", pasta_ingredients)

all_ingredients = pasta_ingredients.union(biryani_ingredients)
common = pasta_ingredients.intersection(biryani_ingredients) 
only_pasta = pasta = pasta_ingredients.difference(biryani_ingredients)
unique_to_each = pasta_ingredients.symmetric_difference(biryani_ingredients)

print("\nAll ingredients (union):", all_ingredients)
print("Common ingredients (intersection):", common)
print("Only in Pasta (difference):", only_pasta)
print("Not shared (sym. difference):", unique_to_each)
