import os
import json
import time
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

# Try to load .env file if python-dotenv is available
try:
    load_dotenv()
    os.getenv("GEMINI_API_KEY")
    load_dotenv()

except ImportError:
    print("Note: python-dotenv not installed. Install with: pip install python-dotenv")

# Import with compatibility - prioritize the stable old SDK
try:
    # Try old SDK first (google-generativeai) - more stable
    import google.generativeai as genai
    USE_OLD_SDK = True
    print("✅ Using google-generativeai (stable)")
except ImportError:
    try:
        # Fall back to new SDK (google-genai) if old one not available
        import google.genai as genai_new
        from google.genai import types
        USE_OLD_SDK = False
        print("✅ Using google-genai (newer)")
    except ImportError:
        print("\n❌ ERROR: No Google AI package found!")
        print("\nPlease install:")
        print("  pip install google-generativeai")
        exit(1)

class AILearningActivity:
    """Enhanced AI learning activity with improved features."""

    def __init__(self):
        """Initialize the activity and validate API key."""
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("Error: GEMINI_API_KEY environment variable not set. Please set it before running.")

        if USE_OLD_SDK:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-1.5-pro')
            self.model_name = 'gemini-1.5-flash'
        else:
            self.client = genai_new.Client(api_key=self.api_key)
            self.model_name = 'gemini-1.5-flash-latest'  # Different format for new SDK

        self.session_history = []
        print(f"✅ Using {'google-generativeai' if USE_OLD_SDK else 'google-genai'} SDK")

    def generate_response(self, prompt, temperature=0.3, max_retries=3):
        """Generate a response from Gemini API with error handling and retry logic."""
        for attempt in range(max_retries):
            try:
                if USE_OLD_SDK:
                    # Old SDK (google-generativeai)
                    generation_config = genai.GenerationConfig(
                        temperature=temperature,
                        max_output_tokens=2048
                    )
                    response = self.model.generate_content(
                        prompt,
                        generation_config=generation_config
                    )
                    return response.text
                else:
                    # New SDK (google-genai)
                    contents = [types.Content(
                        role="user",
                        parts=[types.Part(text=prompt)]
                    )]
                    config = types.GenerateContentConfig(
                        temperature=temperature,
                        max_output_tokens=2048
                    )
                    response = self.client.models.generate_content(
                        model=self.model_name,
                        contents=contents,
                        config=config
                    )
                    return response.text
            except Exception as e:
                error_msg = str(e)

                # Check if it's a rate limit error
                if "429" in error_msg or "quota" in error_msg.lower():
                    if attempt < max_retries - 1:
                        wait_time = 60 * (attempt + 1)  # Wait 60, 120, 180 seconds
                        print(f"\n⚠️ Rate limit hit. Waiting {wait_time} seconds before retry...")
                        time.sleep(wait_time)
                        continue
                    else:
                        return f"Rate limit exceeded. Please wait a few minutes and try again.\n\nTip: The free tier has limited requests per minute. Consider:\n1. Waiting 2-3 minutes between activities\n2. Getting an API key with higher limits at https://aistudio.google.com/"

                # For other errors, return immediately
                return f"Error generating response: {error_msg}"

        return "Failed after multiple retries. Please try again later."

    def get_valid_rating(self):
        """Get a valid rating from 1-5 with error handling."""
        while True:
            try:
                rating = int(input("\nRate the response from 1 (bad) to 5 (good): "))
                if 1 <= rating <= 5:
                    return rating
                print("Please enter a number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")

    def get_valid_choice(self, options):
        """Get a valid menu choice with error handling."""
        while True:
            try:
                choice = input(f"\nEnter your choice (1-{options}): ")
                choice_num = int(choice)
                if 1 <= choice_num <= options:
                    return choice_num
                print(f"Please enter a number between 1 and {options}.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    def save_to_history(self, activity_type, data):
        """Save activity data to session history."""
        entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "activity": activity_type,
            "data": data
        }
        self.session_history.append(entry)

    def reinforcement_learning_activity(self):
        """Conducts an enhanced reinforcement learning activity."""
        print("\n" + "="*60)
        print("REINFORCEMENT LEARNING ACTIVITY")
        print("="*60)
        print("\nThis activity demonstrates how AI improves through feedback.")
        print("You'll provide a prompt, rate the response, and see improvement.\n")

        # Get user input
        prompt = input("Enter a prompt for the AI (e.g., 'Explain quantum computing'): ").strip()
        if not prompt:
            print("Prompt cannot be empty. Returning to menu.")
            return

        # Generate initial response
        print("\n⏳ Generating initial response...")
        initial_response = self.generate_response(prompt)
        print(f"\n--- Initial AI Response ---\n{initial_response}\n")

        # Get feedback
        rating = self.get_valid_rating()
        feedback = input("Provide specific feedback for improvement: ").strip()

        if not feedback:
            print("No feedback provided. Skipping improvement step.")
            return

        # Generate improved response using feedback
        print("\n⏳ Applying your feedback to improve the response...")
        improvement_prompt = f"""Previous response to the prompt "{prompt}":
{initial_response}

User rating: {rating}/5
User feedback: {feedback}

Please provide an improved response that addresses the user's feedback while maintaining accuracy and clarity."""

        improved_response = self.generate_response(improvement_prompt, temperature=0.5)
        print(f"\n--- Improved AI Response ---\n{improved_response}\n")

        # Get rating for improved response
        print("Now rate the improved response:")
        improved_rating = self.get_valid_rating()

        # Save to history
        self.save_to_history("Reinforcement Learning", {
            "prompt": prompt,
            "initial_response": initial_response,
            "initial_rating": rating,
            "feedback": feedback,
            "improved_response": improved_response,
            "improved_rating": improved_rating
        })

        # Reflection
        print("\n" + "-"*60)
        print("REFLECTION QUESTIONS")
        print("-"*60)
        print(f"1. Initial rating: {rating}/5 → Improved rating: {improved_rating}/5")
        print(f"   Did the rating improve? {'Yes!' if improved_rating > rating else 'Consider providing more specific feedback next time.'}")
        print("\n2. How did the model's response change after receiving feedback?")
        print("\n3. In real reinforcement learning, thousands of feedback examples")
        print("   train the model. How might this scale improve AI performance?")
        print("\n4. What are the limitations of this feedback approach?")

        input("\nPress Enter to continue...")

    def role_based_prompt_activity(self):
        """Conducts an enhanced role-based prompts activity."""
        print("\n" + "="*60)
        print("ROLE-BASED PROMPTS ACTIVITY")
        print("="*60)
        print("\nThis activity shows how different roles produce different responses.")
        print("You'll see the same topic explained from multiple perspectives.\n")

        # Get user input
        category = input("Enter a category (e.g., science, history, technology): ").strip()
        if not category:
            print("Category cannot be empty. Returning to menu.")
            return

        topic = input(f"Enter a specific {category} topic: ").strip()
        if not topic:
            print("Topic cannot be empty. Returning to menu.")
            return

        # Define multiple roles
        roles = {
            "Teacher": f"You are an elementary school teacher. Explain {topic} in simple, engaging terms suitable for 10-year-old students. Use analogies and examples they can relate to.",
            "Expert": f"You are a leading expert in {category}. Provide a detailed, technical explanation of {topic} with precise terminology and advanced concepts.",
            "Journalist": f"You are a science journalist writing for a general audience. Explain {topic} in an engaging, accessible way that highlights why it matters to everyday people.",
            "Student": f"You are a curious student asking about {topic}. Ask thoughtful questions and express what confuses you about this concept.",
            "Poet": f"You are a poet. Describe {topic} using creative metaphors, imagery, and emotional language. Make it beautiful and thought-provoking."
        }

        print("\n⏳ Generating responses from different perspectives...\n")

        responses = {}
        for role, prompt in roles.items():
            print(f"🎭 {role}'s Perspective:")
            print("-" * 60)
            response = self.generate_response(prompt, temperature=0.6)
            responses[role] = response
            print(f"{response}\n")

        # Save to history
        self.save_to_history("Role-Based Prompts", {
            "category": category,
            "topic": topic,
            "responses": responses
        })

        # Reflection
        print("\n" + "="*60)
        print("REFLECTION QUESTIONS")
        print("="*60)
        print("\n1. Which perspective did you find most helpful? Why?")
        print("\n2. How did vocabulary and complexity differ across roles?")
        print("\n3. Which role would be most appropriate for:")
        print("   - A research paper?")
        print("   - A children's book?")
        print("   - A news article?")
        print("\n4. How can role-based prompts improve AI applications in education,")
        print("   customer service, or content creation?")
        print("\n5. What are potential risks of AI adopting different 'personas'?")

        input("\nPress Enter to continue...")

    def compare_temperatures_activity(self):
        """New activity: demonstrates temperature parameter effects."""
        print("\n" + "="*60)
        print("TEMPERATURE COMPARISON ACTIVITY (BONUS)")
        print("="*60)
        print("\nThis activity shows how 'temperature' affects AI creativity.")
        print("Temperature controls randomness: low = consistent, high = creative.\n")

        prompt = input("Enter a creative prompt (e.g., 'Write a haiku about coding'): ").strip()
        if not prompt:
            print("Prompt cannot be empty. Returning to menu.")
            return

        temperatures = [0.1, 0.5, 1.0]

        print("\n⏳ Generating responses at different temperatures...\n")

        for temp in temperatures:
            print(f"🌡️ Temperature {temp} ({'Low/Focused' if temp < 0.4 else 'Medium' if temp < 0.8 else 'High/Creative'}):")
            print("-" * 60)
            response = self.generate_response(prompt, temperature=temp)
            print(f"{response}\n")

        print("\n" + "="*60)
        print("OBSERVATION")
        print("="*60)
        print("\nNotice how higher temperatures produce more varied, creative responses")
        print("while lower temperatures give more focused, predictable answers.")

        input("\nPress Enter to continue...")

    def view_session_history(self):
        """Display the session history."""
        print("\n" + "="*60)
        print("SESSION HISTORY")
        print("="*60)

        if not self.session_history:
            print("\nNo activities completed yet in this session.")
            input("\nPress Enter to continue...")
            return

        for i, entry in enumerate(self.session_history, 1):
            print(f"\n[{i}] {entry['activity']} - {entry['timestamp']}")

        print("\n" + "-"*60)
        choice = input("\nEnter activity number to view details (or press Enter to go back): ").strip()

        if choice.isdigit() and 1 <= int(choice) <= len(self.session_history):
            entry = self.session_history[int(choice) - 1]
            print(f"\n{json.dumps(entry, indent=2)}")

        input("\nPress Enter to continue...")

    def save_history_to_file(self):
        """Save session history to a JSON file."""
        if not self.session_history:
            print("\nNo history to save.")
            input("\nPress Enter to continue...")
            return

        filename = f"ai_learning_session_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        try:
            with open(filename, 'w') as f:
                json.dump(self.session_history, f, indent=2)
            print(f"\n✅ Session history saved to: {filename}")
        except Exception as e:
            print(f"\n❌ Error saving history: {str(e)}")

        input("\nPress Enter to continue...")

    def run(self):
        """Main menu and activity loop."""
        print("\n" + "="*60)
        print("🤖 AI LEARNING ACTIVITY PLATFORM 🤖")
        print("="*60)
        print("\nExplore how AI works through interactive activities!")

        while True:
            print("\n" + "="*60)
            print("MAIN MENU")
            print("="*60)
            print("\n1. Reinforcement Learning Activity")
            print("2. Role-Based Prompts Activity")
            print("3. Temperature Comparison Activity (Bonus)")
            print("4. View Session History")
            print("5. Save History to File")
            print("6. Exit")

            choice = self.get_valid_choice(6)

            if choice == 1:
                self.reinforcement_learning_activity()
            elif choice == 2:
                self.role_based_prompt_activity()
            elif choice == 3:
                self.compare_temperatures_activity()
            elif choice == 4:
                self.view_session_history()
            elif choice == 5:
                self.save_history_to_file()
            elif choice == 6:
                print("\n" + "="*60)
                print("Thank you for exploring AI learning!")
                print("Keep experimenting and learning! 🚀")
                print("="*60 + "\n")
                break

def main():
    """Entry point for the application."""
    try:
        activity = AILearningActivity()
        activity.run()
    except ValueError as e:
        print(f"\n❌ {str(e)}")
        print("\nTo set your API key:")
        print("  Create a .env file with: GEMINI_API_KEY=your-api-key")
        print("  Or set environment variable:")
        print("    PowerShell: $env:GEMINI_API_KEY='your-api-key'")
        print("    CMD:        set GEMINI_API_KEY=your-api-key")
    except KeyboardInterrupt:
        print("\n\nProgram interrupted. Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()