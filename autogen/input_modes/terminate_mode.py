import os
from dotenv import load_dotenv
from autogen import ConversableAgent

load_dotenv()

model = "gpt-4o-mini"
llm_config = {
    "model": model,
    "temperature": 0.9,
    "api_key": os.environ["OPENAI_API_KEY"],
}

agent_with_animal = ConversableAgent(
    "agent_with_animal",
    system_message="You are thinking of an animal. You have the animal 'elephant' in your mind, and I will try to guess it. "
    "If I guess incorrectly, give me a hint. ",
    llm_config=llm_config,
    max_consecutive_auto_reply=1,  # maximum number of consecutive auto-replies before asking for human input
    is_termination_msg=lambda msg: "elephant"
    in msg["content"],  # terminate if the animal is guessed by the other agent
    human_input_mode="TERMINATE",  # ask for human input until the game is terminated
)

agent_guess_animal = ConversableAgent(
    "agent_guess_animal",
    system_message="I have an animal in my mind, and you will try to guess it. "
    "If I give you a hint, use it to narrow down your guesses. ",
    llm_config=llm_config,
    human_input_mode="NEVER",
)

# make sure to clear the chat history before starting a new conversation - delete the cache file
result = agent_with_animal.initiate_chat(
    agent_guess_animal,
    message="I am thinking of an animal. Guess which one!",
)

# Output

# E:\Coding-Mastery\AutoGen\projects\autogen\Scripts\python.exe E:\Coding-Mastery\AutoGen\projects\input_modes\terminate_mode.py
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
#
# >>>>>>>> USING AUTO REPLY...
# agent_with_animal (to agent_guess_animal):
#
# Yes, it is a mammal.
#
# --------------------------------------------------------------------------------
# agent_guess_animal (to agent_with_animal):
#
# Is it typically a domesticated animal?
#
# --------------------------------------------------------------------------------
# Please give feedback to agent_guess_animal. Press enter to skip and use auto-reply, or type 'exit' to stop the conversation: yes
# agent_with_animal (to agent_guess_animal):
#
# yes
#
# --------------------------------------------------------------------------------
# agent_guess_animal (to agent_with_animal):
#
# Is it a common pet?
#
# --------------------------------------------------------------------------------
#
# >>>>>>>> USING AUTO REPLY...
# agent_with_animal (to agent_guess_animal):
#
# No, it is not a common pet.
#
# --------------------------------------------------------------------------------
# agent_guess_animal (to agent_with_animal):
#
# Is it a farm animal?
#
# --------------------------------------------------------------------------------
# Please give feedback to agent_guess_animal. Press enter to skip and use auto-reply, or type 'exit' to stop the conversation: no
# agent_with_animal (to agent_guess_animal):
#
# no
#
# --------------------------------------------------------------------------------
# agent_guess_animal (to agent_with_animal):
#
# Is it a wild mammal?
#
# --------------------------------------------------------------------------------
#
# >>>>>>>> USING AUTO REPLY...
# agent_with_animal (to agent_guess_animal):
#
# Yes, it is a wild mammal.
#
# --------------------------------------------------------------------------------
# agent_guess_animal (to agent_with_animal):
#
# Is it a large mammal?
#
# --------------------------------------------------------------------------------
# Please give feedback to agent_guess_animal. Press enter to skip and use auto-reply, or type 'exit' to stop the conversation: yes
# agent_with_animal (to agent_guess_animal):
#
# yes
#
# --------------------------------------------------------------------------------
# agent_guess_animal (to agent_with_animal):
#
# Is it a type of big cat, like a lion or tiger?
#
# --------------------------------------------------------------------------------
#
# >>>>>>>> USING AUTO REPLY...
# agent_with_animal (to agent_guess_animal):
#
# No, it is not a big cat.
#
# --------------------------------------------------------------------------------
# agent_guess_animal (to agent_with_animal):
#
# Is it a species of bear?
#
# --------------------------------------------------------------------------------
# Please give feedback to agent_guess_animal. Press enter to skip and use auto-reply, or type 'exit' to stop the conversation: no
# agent_with_animal (to agent_guess_animal):
#
# no
#
# --------------------------------------------------------------------------------
# agent_guess_animal (to agent_with_animal):
#
# Is it an elephant?
#
# --------------------------------------------------------------------------------
# Please give feedback to agent_guess_animal. Press enter or type 'exit' to stop the conversation: yes
# agent_with_animal (to agent_guess_animal):
#
# yes
#
# --------------------------------------------------------------------------------
# agent_guess_animal (to agent_with_animal):
#
# Great! The animal you were thinking of is an elephant. Would you like to play again or ask something else?
#
# --------------------------------------------------------------------------------
# Please give feedback to agent_guess_animal. Press enter or type 'exit' to stop the conversation: exit
#
# Process finished with exit code 0
