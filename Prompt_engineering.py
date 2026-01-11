import google.generativeai as genai

# Configure the API
genai.configure(api_key="AIzaSyDpqrB33vTa-F9yPG_IJeyrcaIRLePBcFk")

# Initialize the model globally
model = genai.GenerativeModel('gemini-pro')

def generate_response(prompt):
    """Generate a response using the Gemini model."""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating response: {str(e)}"
    
def clear_prompt():
    """Example of a clear, specific prompt."""
    print("\n=== CLEAR PROMPT ===")
    clear_prompt_text = """
    Write a Python function that takes a list of numbers and returns 
    the sum of all even numbers in the list. Include:
    1. Function documentation
    2. Input validation
    3. Example usage
    """

    print(f"Prompt: {clear_prompt_text}")
    response = generate_response(clear_prompt_text)
    print(f"\nResponse:\n{response}")
    return response

def vague_prompt():
    """Example of a vague prompt (less effective)."""
    print("\n=== VAGUE PROMPT ===")
    vague_prompt_text = "Write some code about numbers"
    
    print(f"Prompt: {vague_prompt_text}")
    response = generate_response(vague_prompt_text)
    print(f"\nResponse:\n{response}")
    return response

def silly_prompt():
    """Example of using context and specificity."""
    print("\n=== CONTEXTUAL PROMPT ===")
    contextual_prompt = """
    I'm teaching a beginner Python class. Can you explain what a 
    list comprehension is using:
    - Simple language
    - A practical example with numbers
    - Common mistakes to avoid
    """
    
    print(f"Prompt: {contextual_prompt}")
    response = generate_response(contextual_prompt)
    print(f"\nResponse:\n{response}")
    return response

def structured_prompt():
    """Example of a structured prompt with format specification."""
    print("\n=== STRUCTURED PROMPT ===")
    structured_prompt_text = """
    Analyze the following Python code and provide feedback in this format:
    
    Code:
    def calculate(x, y):
        return x + y
    
    Please provide:
    1. Code Quality (1-10):
    2. Strengths:
    3. Areas for Improvement:
    4. Refactored Version:
    """
    
    print(f"Prompt: {structured_prompt_text}")
    response = generate_response(structured_prompt_text)
    print(f"\nResponse:\n{response}")
    return response

def main():
    """Run all prompt examples."""
    print("=" * 60)
    print("PROMPT ENGINEERING EXAMPLES")
    print("=" * 60)
    
    # Run different prompt examples
    clear_prompt()
    vague_prompt()
    silly_prompt()
    structured_prompt()
    
    print("\n" + "=" * 60)
    print("KEY TAKEAWAYS:")
    print("- Be specific and clear about what you want")
    print("- Provide context when needed")
    print("- Specify the format you want")
    print("- Include examples when helpful")
    print("=" * 60)

if __name__ == "__main__":
    main()