from dotenv import load_dotenv
from openai import OpenAI
from colorama import Fore
import warnings


warnings.filterwarnings("ignore")

# LOAD ENV VARIABLES
load_dotenv()

# Load the model
client = OpenAI()

# Define a request
print(Fore.GREEN + "Requesting the model to generate a response..." + Fore.RESET + "\n")

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant"},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming"}
    ]
)

print(Fore.BLUE + completion.choices[0].message.content)