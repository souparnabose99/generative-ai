import os
from autogen import ConversableAgent
from dotenv import load_dotenv

load_dotenv()

model = "gpt-4o-mini"
llm_config = {
    "model": model,
    "api_key": os.environ.get("OPENAI_API_KEY"),
}

agent_with_animal = ConversableAgent(
    "agent_with_animal",
    system_message="You are thinking of an animal. You have the animal 'elephant' in your mind, and I will try to guess it. "
    "If I guess incorrectly, give me a hint. ",
    llm_config=llm_config,
    is_termination_msg=lambda msg: "elephant"
    in msg["content"],  # terminate if the animal is guessed
    human_input_mode="NEVER",  # never ask for human input
)


agent_guess_animal = ConversableAgent(
    "agent_guess_animal",
    system_message="I have an animal in my mind, and you will try to guess it. "
    "If I give you a hint, use it to narrow down your guesses. ",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

agent_with_animal.initiate_chat(
    agent_guess_animal,
    message="I am thinking of an animal. Guess which one!",
)

# Output:

# E:\Coding-Mastery\AutoGen\projects\autogen\Scripts\python.exe E:\Coding-Mastery\AutoGen\projects\input_modes\never_mode.py
# E:\Coding-Mastery\AutoGen\projects\autogen\Lib\site-packages\flaml\__init__.py:20: UserWarning: flaml.automl is not available. Please install flaml[automl] to enable AutoML functionalities.
#   warnings.warn("flaml.automl is not available. Please install flaml[automl] to enable AutoML functionalities.")
# agent_with_animal (to agent_guess_animal):
#
# I am thinking of an animal. Guess which one!
#
# --------------------------------------------------------------------------------
# agent_guess_animal (to agent_with_animal):
#
# Is it a mammal?
#
# --------------------------------------------------------------------------------
# agent_with_animal (to agent_guess_animal):
#
# Yes, it is a mammal.
#
# --------------------------------------------------------------------------------
# agent_guess_animal (to agent_with_animal):
#
# Is it a domesticated animal?
#
# --------------------------------------------------------------------------------
# agent_with_animal (to agent_guess_animal):
#
# No, it is not a domesticated animal.
#
# --------------------------------------------------------------------------------
# agent_guess_animal (to agent_with_animal):
#
# Is it a large mammal?
#
# --------------------------------------------------------------------------------
# agent_with_animal (to agent_guess_animal):
#
# Yes, it is a large mammal.
#
# --------------------------------------------------------------------------------
# agent_guess_animal (to agent_with_animal):
#
# Is this large mammal a carnivore?
#
# --------------------------------------------------------------------------------
# agent_with_animal (to agent_guess_animal):
#
# No, it is not a carnivore.
#
# --------------------------------------------------------------------------------
# agent_guess_animal (to agent_with_animal):
#
# Is this large mammal an herbivore?
#
# --------------------------------------------------------------------------------
# agent_with_animal (to agent_guess_animal):
#
# Yes, it is an herbivore.
#
# --------------------------------------------------------------------------------
# agent_guess_animal (to agent_with_animal):
#
# Is this large herbivore commonly found in Africa?
#
# --------------------------------------------------------------------------------
# agent_with_animal (to agent_guess_animal):
#
# Yes, this large herbivore is commonly found in Africa.
#
# --------------------------------------------------------------------------------
# agent_guess_animal (to agent_with_animal):
#
# Is this animal a type of elephant?
#
# --------------------------------------------------------------------------------
#
# Process finished with exit code 0