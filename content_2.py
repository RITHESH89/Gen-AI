import os
from dotenv import load_dotenv
from google import genai

# Load .env
load_dotenv()

# create client
client = genai. Client(
   api_key=os. getenv("GEMINI_API_KEY")
)

#Empty Conversation history
messages = []

#First user message
user_input_1 = "Wo is Virat Kohli?"

messages.append(
  {
   "role":"user",
  "parts": [{"text":user_input_1}]
   }
)

#Generate Second response
response_2 = client.models.generate_content(
  model="gemini-3-flash-preview",
  contents=messages
)


print(response_2.text)
