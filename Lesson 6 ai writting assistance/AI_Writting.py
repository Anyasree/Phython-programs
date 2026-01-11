import os
from groq import Groq
import google.generativeai as genai
from colorama import init, Fore, Style
from dotenv import load_dotenv

# Initialize colorama
init(autoreset=True)

# Load environment variables
load_dotenv()

# Initialize API clients
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Check which APIs are available
groq_available = GROQ_API_KEY is not None
gemini_available = GEMINI_API_KEY is not None

if not groq_available and not gemini_available:
    raise ValueError("No API keys found! Please add GROQ_API_KEY or GEMINI_API_KEY to your .env file.")

# Initialize clients
groq_client = Groq(api_key=GROQ_API_KEY) if groq_available else None
if gemini_available:
    genai.configure(api_key=GEMINI_API_KEY)

# Function to generate AI response with fallback
def generate_response(prompt, temperature=0.3):
    """Generate a response trying Groq first, then Gemini as fallback."""

    # Try Groq first (faster and more reliable)
    if groq_available:
        try:
            chat_completion = groq_client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a professional essay writing assistant. Provide well-structured, coherent, and engaging content."
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model="llama-3.3-70b-versatile",
                temperature=temperature,
                max_tokens=4096,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            print(Fore.YELLOW + f"⚠️ Groq failed, trying Gemini... ({str(e)[:50]})")

    # Fallback to Gemini
    if gemini_available:
        try:
            model = genai.GenerativeModel('gemini-1.5-flash')
            generation_config = genai.types.GenerationConfig(temperature=temperature)
            response = model.generate_content(prompt, generation_config=generation_config)
            return response.text
        except Exception as e:
            return f"Error: Both APIs failed. Groq: unavailable, Gemini: {str(e)}"

    return "Error: No available API to generate response."

# Step 1: Get essay details
def get_essay_details():
    api_status = []
    if groq_available:
        api_status.append("Groq")
    if gemini_available:
        api_status.append("Gemini")

    print(Fore.CYAN + f"\n=== AI Writing Assistant (Using: {' + '.join(api_status)}) ===\n")

    # Gather user information for the essay
    topic = input(Fore.YELLOW + "What is the topic of your essay? ")
    essay_type = input(Fore.YELLOW + "What type of essay are you writing? (e.g., Argumentative, Expository, Descriptive, Persuasive, Analytical) ")

    # Modified section for selecting word count
    print(Fore.GREEN + "\nSelect the desired essay word count:")
    print(Fore.GREEN + "1. 300 words")
    print(Fore.GREEN + "2. 900 words")
    print(Fore.GREEN + "3. 1200 words")
    print(Fore.GREEN + "4. 2000 words")

    word_count_choice = input(Fore.YELLOW + "Please enter the number corresponding to your choice (1-4): ")
    word_count_dict = {"1": "300", "2": "900", "3": "1200", "4": "2000"}

    # Validate word count choice
    while word_count_choice not in word_count_dict:
        print(Fore.RED + "Invalid choice. Please select a number between 1-4.")
        word_count_choice = input(Fore.YELLOW + "Please enter the number corresponding to your choice (1-4): ")

    length = word_count_dict[word_count_choice]

    target_audience = input(Fore.YELLOW + "Who is the target audience for your essay? (e.g., High school students, College professors) ")
    specific_points = input(Fore.YELLOW + "Do you have any specific points that must be included in the essay? (Press Enter to skip) ")

    # Additional details
    stance = input(Fore.YELLOW + "What is your stance on the topic? (e.g., For, Against, Neutral) ")
    references = input(Fore.YELLOW + "Are there any sources, quotes, or references you'd like to include? (Press Enter to skip) ")
    writing_style = input(Fore.YELLOW + "Do you have any preferences for writing style? (e.g., Formal, Conversational, Academic, Creative) ")

    # Ask for outline preference
    outline_needed = input(Fore.YELLOW + "Would you like the AI to suggest an outline first? (Yes/No) ").lower()

    # Return the gathered information
    return {
        "topic": topic,
        "essay_type": essay_type,
        "length": length,
        "target_audience": target_audience,
        "specific_points": specific_points,
        "stance": stance,
        "references": references,
        "writing_style": writing_style,
        "outline_needed": outline_needed
    }

# Generate outline if needed
def generate_outline(details):
    if details['outline_needed'] == 'yes':
        outline_prompt = f"""Create a detailed outline for a {details['length']}-word {details['essay_type']} essay about {details['topic']}.

Requirements:
- Stance: {details['stance']}
- Target Audience: {details['target_audience']}
- Writing Style: {details['writing_style']}
{f"- Specific Points to Include: {details['specific_points']}" if details['specific_points'] else ""}
{f"- References: {details['references']}" if details['references'] else ""}

Provide a clear structure with main sections, subsections, and key points to cover."""

        outline = generate_response(outline_prompt, 0.3)
        print(Fore.CYAN + "\n=== Suggested Outline ===")
        print(Fore.GREEN + outline)

        proceed = input(Fore.YELLOW + "\nWould you like to proceed with essay generation based on this outline? (Yes/No) ").lower()
        if proceed != 'yes':
            print(Fore.RED + "Essay generation cancelled.")
            return False
    return True

# Step 2: Generate Essay Content
def generate_essay_content(details):
    # Ask for creative vs structured temperature preference
    print(Fore.CYAN + "\nTemperature setting controls creativity:")
    print(Fore.CYAN + "- Lower (0.2-0.4): More structured and focused")
    print(Fore.CYAN + "- Higher (0.6-0.9): More creative and varied")

    temperature_input = input(Fore.YELLOW + "Enter temperature value (0.2-0.9, recommended: 0.5): ")
    try:
        temperature = float(temperature_input)
        temperature = max(0.2, min(0.9, temperature))  # Clamp between 0.2 and 0.9
    except ValueError:
        temperature = 0.5
        print(Fore.YELLOW + "Invalid input. Using default temperature: 0.5")

    essay_sections = {}

    # Generate introduction
    introduction_prompt = f"""Write an engaging introduction for a {details['length']}-word {details['essay_type']} essay about {details['topic']}.

Requirements:
- Stance: {details['stance']}
- Target Audience: {details['target_audience']}
- Writing Style: {details['writing_style']}

The introduction should hook the reader and clearly state the thesis."""

    print(Fore.CYAN + "\n⏳ Generating introduction...")
    introduction = generate_response(introduction_prompt, temperature)
    essay_sections['introduction'] = introduction
    print(Fore.CYAN + "\n=== Generated Introduction ===")
    print(Fore.GREEN + introduction)

    # Ask if user wants the full body or a step-by-step body
    body_style = input(Fore.YELLOW + "\nWould you like the AI to write the body step-by-step or generate a full draft? (Step-by-step/Full draft): ").lower()

    # Generate body content based on style
    if body_style == "full draft":
        body_prompt = f"""Write a detailed body section for a {details['length']}-word {details['essay_type']} essay about {details['topic']}.

Requirements:
- Stance: {details['stance']}
- Target Audience: {details['target_audience']}
- Writing Style: {details['writing_style']}
{f"- Specific Points to Include: {details['specific_points']}" if details['specific_points'] else ""}
{f"- References to Include: {details['references']}" if details['references'] else ""}

Provide well-structured paragraphs with strong arguments, evidence, and analysis."""

        print(Fore.CYAN + "\n⏳ Generating full body section...")
        body = generate_response(body_prompt, temperature)
        essay_sections['body'] = body
        print(Fore.CYAN + "\n=== Generated Full Body ===")
        print(Fore.GREEN + body)
    else:
        # Step-by-step body generation
        body_step_prompt = f"""Write step-by-step arguments for a {details['essay_type']} essay on {details['topic']}.

Requirements:
- Stance: {details['stance']}
- Target Audience: {details['target_audience']}
{f"- Specific Points to Include: {details['specific_points']}" if details['specific_points'] else ""}

Provide 3-4 main arguments with evidence and reasoning for each."""

        print(Fore.CYAN + "\n⏳ Generating step-by-step body...")
        body_step = generate_response(body_step_prompt, temperature)
        essay_sections['body'] = body_step
        print(Fore.CYAN + "\n=== Generated Step-by-Step Body ===")
        print(Fore.GREEN + body_step)

    # Generate conclusion
    conclusion_prompt = f"""Write a powerful conclusion for a {details['length']}-word {details['essay_type']} essay about {details['topic']}.

Requirements:
- Stance: {details['stance']}
- Target Audience: {details['target_audience']}
- Writing Style: {details['writing_style']}

The conclusion should summarize main points and leave a lasting impression."""

    print(Fore.CYAN + "\n⏳ Generating conclusion...")
    conclusion = generate_response(conclusion_prompt, temperature)
    essay_sections['conclusion'] = conclusion
    print(Fore.CYAN + "\n=== Generated Conclusion ===")
    print(Fore.GREEN + conclusion)

    return essay_sections

# Step 3: Feedback and Refinement
def feedback_and_refinement(essay_sections, details):
    satisfaction = input(Fore.YELLOW + "\nHow satisfied are you with the generated content? (Rate from 1 to 5): ")

    if satisfaction != "5":
        feedback = input(Fore.YELLOW + "Please provide feedback on how we can improve the content (tone, structure, specific sections, etc.): ")

        # Ask which section to refine
        print(Fore.CYAN + "\nWhich section would you like to refine?")
        print(Fore.GREEN + "1. Introduction")
        print(Fore.GREEN + "2. Body")
        print(Fore.GREEN + "3. Conclusion")
        print(Fore.GREEN + "4. Entire essay")

        section_choice = input(Fore.YELLOW + "Enter your choice (1-4): ")

        section_map = {
            "1": "introduction",
            "2": "body",
            "3": "conclusion",
            "4": "full"
        }

        section_to_refine = section_map.get(section_choice, "full")

        if section_to_refine == "full":
            full_essay = f"{essay_sections['introduction']}\n\n{essay_sections['body']}\n\n{essay_sections['conclusion']}"
            refine_prompt = f"""Improve this essay based on the following feedback: {feedback}

Original essay:
{full_essay}

Provide the complete improved version."""
        else:
            refine_prompt = f"""Improve this {section_to_refine} based on the following feedback: {feedback}

Original {section_to_refine}:
{essay_sections[section_to_refine]}

Provide the improved version."""

        print(Fore.CYAN + f"\n⏳ Refining {section_to_refine}...")
        refined = generate_response(refine_prompt, 0.5)
        print(Fore.CYAN + f"\n=== Refined {section_to_refine.title()} ===")
        print(Fore.GREEN + refined)

        # Update the section
        if section_to_refine != "full":
            essay_sections[section_to_refine] = refined

        return refined
    else:
        print(Fore.CYAN + "\n✓ Thank you! The essay looks good.")
        return None

# Save essay to file
def save_essay(essay_sections, details):
    save_option = input(Fore.YELLOW + "\nWould you like to save the essay to a file? (Yes/No) ").lower()

    if save_option == 'yes':
        filename = f"essay_{details['topic'].replace(' ', '_')[:30]}.txt"

        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("="*70 + "\n")
                f.write(f"ESSAY: {details['topic']}\n")
                f.write("="*70 + "\n\n")
                f.write(f"Type: {details['essay_type']}\n")
                f.write(f"Length: {details['length']} words\n")
                f.write(f"Stance: {details['stance']}\n")
                f.write(f"Target Audience: {details['target_audience']}\n")
                f.write(f"Writing Style: {details['writing_style']}\n\n")
                f.write("="*70 + "\n")
                f.write("INTRODUCTION\n")
                f.write("="*70 + "\n\n")
                f.write(essay_sections['introduction'] + "\n\n")
                f.write("="*70 + "\n")
                f.write("BODY\n")
                f.write("="*70 + "\n\n")
                f.write(essay_sections['body'] + "\n\n")
                f.write("="*70 + "\n")
                f.write("CONCLUSION\n")
                f.write("="*70 + "\n\n")
                f.write(essay_sections['conclusion'] + "\n")

            print(Fore.GREEN + f"\n✓ Essay saved successfully to: {filename}")
        except Exception as e:
            print(Fore.RED + f"\n✗ Error saving file: {str(e)}")

# Main Function
def run_activity():
    print(Fore.CYAN + "\n" + "="*70)
    print(Fore.CYAN + "      Welcome to the AI Writing Assistant (Hybrid Mode)")
    print(Fore.CYAN + "="*70)

    try:
        # Get essay details from user
        details = get_essay_details()

        # Generate outline if requested
        if not generate_outline(details):
            return

        # Generate the essay content based on the details
        essay_sections = generate_essay_content(details)

        # Ask for feedback and refine
        feedback_and_refinement(essay_sections, details)

        # Save essay to file
        save_essay(essay_sections, details)

        print(Fore.CYAN + "\n" + "="*70)
        print(Fore.CYAN + "         Thank you for using AI Writing Assistant!")
        print(Fore.CYAN + "="*70 + "\n")

    except KeyboardInterrupt:
        print(Fore.RED + "\n\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(Fore.RED + f"\n\nAn error occurred: {str(e)}")

# Run the Activity
if __name__ == "__main__":
    run_activity()