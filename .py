import google.generativeai as genai

API_KEY = "AIzaSyC_5gSbP0J2yd02_SVH6NAyTFDm-h1ObFQ"
genai.configure(api_key=API_KEY)

# List all available models
print("Available Gemini models:")
for model in genai.list_models():
    if 'generateContent' in model.supported_generation_methods:
        print(model.name)