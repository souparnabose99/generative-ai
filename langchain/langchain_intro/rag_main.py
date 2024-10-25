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

# Output -->
# Requesting the model to generate a response...
#
# In the labyrinth of code we find,
# A concept both complex and kind,
# Recursion whispers a looping tale,
# Of functions that in themselves prevail.
#
# A function that calls its own name,
# With each repetition, not for fame,
# But to break a problem into parts,
# Unraveling the complexity that charts.
#
# Like a mirror reflecting its own reflection,
# Recursion dives deep, a coding connection,
# A dance of patterns, a looping grace,
# Unveiling solutions in a recursive embrace.
#
# So dive into the recursive flow,
# Let the code in patterns grow,
# Each call a journey inward bound,
# In the beauty of recursion, wisdom is found.