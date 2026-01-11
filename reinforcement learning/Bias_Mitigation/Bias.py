from groq import Groq
import config

# Initialize the Groq API client
client = Groq(api_key=config.GROQ_API_KEY)

def generate_response(prompt, temperature=0.3):
    """Generate a response from Groq API."""
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def bias_mitigation_activity():
    """Conducts the bias mitigation activity."""
    print("\n=== BIAS MITIGATION ACTIVITY ===\n")
    
    prompt = input("Enter a prompt to explore bias (e.g., 'Describe the ideal doctor'): ")
    initial_response = generate_response(prompt)
    print(f"\nInitial AI Response: {initial_response}")
    
    # NEW: Allow user to skip if no bias found
    print("\n" + "="*60)
    print("Do you see any bias in this response?")
    print("="*60)
    
    modified_prompt = input("\nModify the prompt to reduce bias (or type 'skip' if no bias found): ")
    
    # NEW: Check if user wants to skip
    if modified_prompt.lower() in ['skip', 'exit', 'no', 'none', '']:
        print("\n✓ Great! You identified that this response shows no obvious bias.")
        print("This is an important skill - recognizing when AI does well!")
        return
    
    # If not skipping, continue with modified prompt
    modified_response = generate_response(modified_prompt)
    print(f"\nModified AI Response: {modified_response}")
    
    # Show comparison
    print("\n" + "="*60)
    print("COMPARISON:")
    print("="*60)
    print("Did the modified prompt reduce bias?")
    print("What differences do you notice between the two responses?")

def token_limit_activity():
    """Conducts the token limit activity."""
    print("\n=== TOKEN LIMIT ACTIVITY ===\n")
    
    long_prompt = input("Enter a long prompt (more than 300 words): ")
    long_response = generate_response(long_prompt)
    print(f"\nResponse to Long Prompt:")
    print(f"Length: {len(long_response)} characters")
    print(f"{long_response[:500]}...")
    
    short_prompt = input("\nNow, condense the prompt to be more concise: ")
    short_response = generate_response(short_prompt)
    print(f"\nResponse to Condensed Prompt:")
    print(f"Length: {len(short_response)} characters")
    print(f"{short_response}")
    
    # Show comparison
    print("\n" + "="*60)
    print("COMPARISON:")
    print("="*60)
    print(f"Original response: {len(long_response)} characters")
    print(f"Condensed response: {len(short_response)} characters")
    print("Was the condensed prompt more effective?")

def run_activity():
    """Runs the entire activity for the user."""
    print("\n" + "="*60)
    print("     AI LEARNING ACTIVITY: BIAS & TOKEN LIMITS")
    print("="*60)
    
    activity_choice = input("\nWhich activity would you like to run?\n1: Bias Mitigation\n2: Token Limits\n3: Exit\n\nYour choice: ")

    if activity_choice == "1":
        bias_mitigation_activity()
    elif activity_choice == "2":
        token_limit_activity()
    elif activity_choice == "3":
        print("\n✓ Exiting. Thank you for learning about AI!")
        return
    else:
        print("\n✗ Invalid choice. Please choose 1, 2, or 3.")
    
    # Ask if they want to continue
    continue_choice = input("\n\nWould you like to run another activity? (yes/no): ")
    if continue_choice.lower() in ['yes', 'y']:
        run_activity()
    else:
        print("\n✓ Thank you for learning about AI! Goodbye!")

if __name__ == "__main__":
    run_activity()