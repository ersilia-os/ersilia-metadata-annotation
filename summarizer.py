import os
from openai import OpenAI
from dotenv import load_dotenv
#loads the environment variables from the .env file
load_dotenv()

# client that is used to make requests to the OpenAI's API
client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

def summarize(text):
    # creates a new chat that generates a response
    completion = client.chat.completions.create(
        model= "gpt-4",
        messages=[
            {"role": "user", "content": f"Summarize this please: {text}"}
        ]
    )
    # returns the text content of the response
    return completion.choices[0].message.content
