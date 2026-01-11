import google.generativeai as genai

API_KEY = "AIzaSyBunvpzNE8_yfsEUzynvXePn1nidmqt4fA"  

def generate_response(prompt, temperature=0.3):
    """
    Generate a response from Gemini API based on the given prompt.
    Args:
        prompt (str): The input prompt for the AI
        temperature (float): Controls randomness (0.0-1.0, lower = more focused)
    Returns:
        str: The AI's response text
    """
    try:
        genai.configure(api_key=API_KEY)
        model = genai.GenerativeModel('gemini-2.5-flash-lite-preview-09-2025')

        generation_config = {
            'temperature': temperature,
            'max_output_tokens': 200,
        }

        response = model.generate_content(
            prompt,
            generation_config=generation_config
        )

        return response.text

    except Exception as e:
        return f"Error generating response: {str(e)}"


def run_activity():
    """
    Main activity function that demonstrates zero-shot, one-shot, and few-shot learning.
    """
    print("=" * 70)
    print("EXPLORING AI WITH ZERO-SHOT, ONE-SHOT, AND FEW-SHOT LEARNING")
    print("=" * 70)
    print("\nThis activity demonstrates how providing examples affects AI responses:")
    print("• Zero-Shot: No examples provided")
    print("• One-Shot: One example provided")
    print("• Few-Shot: Multiple examples provided")
    print("\n" + "=" * 70 + "\n")

    print("STEP 1: Provide Your Input")
    print("-" * 40)
    category = input("Enter a category (e.g., animal, food, city, color): ").strip()
    item = input(f"Enter a specific item to classify as {category}: ").strip()
    print("\n")

    print("=" * 70)
    print("PART 1: ZERO-SHOT LEARNING (No Examples)")
    print("=" * 70)
    zero_shot_prompt = f"Is {item} a {category}? Answer with yes or no and briefly explain."
    print(f"Prompt: {zero_shot_prompt}")
    print("\nAI Response:")
    print(generate_response(zero_shot_prompt))
    print("\n")

    print("=" * 70)
    print("PART 2: ONE-SHOT LEARNING (One Example)")
    print("=" * 70)

    if category.lower() == "animal":
        example = "A dog is an animal."
    elif category.lower() == "food":
        example = "Pizza is a food."
    elif category.lower() == "city":
        example = "Paris is a city."
    else:
        example = f"Example item is a {category}."

    one_shot_prompt = f"{example}\n\nIs {item} a {category}? Answer with yes or no and briefly explain."
    print(f"Prompt:\n{one_shot_prompt}")
    print("\nAI Response:")
    print(generate_response(one_shot_prompt))
    print("\n")

    print("=" * 70)
    print("PART 3: FEW-SHOT LEARNING (Multiple Examples)")
    print("=" * 70)

    if category.lower() == "animal":
        examples = "A dog is an animal.\nA cat is an animal.\nA car is not an animal."
    elif category.lower() == "food":
        examples = "Pizza is a food.\nApple is a food.\nA rock is not a food."
    elif category.lower() == "city":
        examples = "Paris is a city.\nTokyo is a city.\nMount Everest is not a city."
    else:
        examples = f"Item1 is a {category}.\nItem2 is a {category}.\nItem3 is not a {category}."

    few_shot_prompt = f"{examples}\n\nIs {item} a {category}? Answer with yes or no and briefly explain."
    print(f"Prompt:\n{few_shot_prompt}")
    print("\nAI Response:")
    print(generate_response(few_shot_prompt))
    print("\n")

    print("=" * 70)
    print("PART 4: CREATIVE FEW-SHOT LEARNING (Story Generation)")
    print("=" * 70)
    creative_prompt = f"""Example 1: The dragon flew over mountains.
Example 2: The wizard cast a powerful spell.
Example 3: The knight rode into battle.

Now write a creative one-sentence story about: {item}"""

    print(f"Prompt:\n{creative_prompt}")
    print("\nAI Response (with higher temperature for creativity):")
    print(generate_response(creative_prompt, temperature=0.7))
    print("\n")

    print("=" * 70)
    print("PART 5: REFLECTION")
    print("=" * 70)
    print("\nThink about these questions:")
    print("\n1. How did the AI's responses differ between zero-shot, one-shot, and few-shot?")
    print("2. Which approach gave the most accurate or relevant response?")
    print("3. How did providing examples help guide the AI's understanding?")
    print("4. In the creative example, how did increasing temperature affect the output?")
    print("\n" + "=" * 70)
    print("Activity Complete! Thank you for exploring AI learning approaches.")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    run_activity()