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

human_proxy = ConversableAgent(
    "human_proxy",
    llm_config=False,  # no LLM used for human proxy
    human_input_mode="ALWAYS",  # always ask for human input
)

result = human_proxy.initiate_chat(
    agent_with_animal,
    message="Dog",
)

# Output

# E:\Coding-Mastery\AutoGen\projects\autogen\Scripts\python.exe E:\Coding-Mastery\AutoGen\projects\input_modes\always_mode.py
# E:\Coding-Mastery\AutoGen\projects\autogen\Lib\site-packages\flaml\__init__.py:20: UserWarning: flaml.automl is not available. Please install flaml[automl] to enable AutoML functionalities.
#   warnings.warn("flaml.automl is not available. Please install flaml[automl] to enable AutoML functionalities.")
# human_proxy (to agent_with_animal):
#
# Dog
#
# --------------------------------------------------------------------------------
# agent_with_animal (to human_proxy):
#
# No, that's not correct. Would you like to try again or would you like a hint?
#
# --------------------------------------------------------------------------------
# Replying as human_proxy. Provide feedback to agent_with_animal. Press enter to skip and use auto-reply, or type 'exit' to end the conversation:
#
# >>>>>>>> NO HUMAN INPUT RECEIVED.
#
# >>>>>>>> USING AUTO REPLY...
# human_proxy (to agent_with_animal):
#
#
#
# --------------------------------------------------------------------------------
# agent_with_animal (to human_proxy):
#
# I'm sorry, I didn't receive your response. Please type in the animal you are thinking of or let me know if you'd like a hint.
#
# --------------------------------------------------------------------------------
# Replying as human_proxy. Provide feedback to agent_with_animal. Press enter to skip and use auto-reply, or type 'exit' to end the conversation: cat
# human_proxy (to agent_with_animal):
#
# cat
#
# --------------------------------------------------------------------------------
# agent_with_animal (to human_proxy):
#
# No, that's not correct. Here's your hint: This animal is the largest land animal in the world and is known for its tusks. What animal are you thinking of?
#
# --------------------------------------------------------------------------------
# Replying as human_proxy. Provide feedback to agent_with_animal. Press enter to skip and use auto-reply, or type 'exit' to end the conversation: giraffe
# human_proxy (to agent_with_animal):
#
# giraffe
#
# --------------------------------------------------------------------------------
# agent_with_animal (to human_proxy):
#
# No, that's not correct. Let me give you another hint: This animal has a prehensile trunk. What animal are you thinking of?
#
# --------------------------------------------------------------------------------
# Replying as human_proxy. Provide feedback to agent_with_animal. Press enter to skip and use auto-reply, or type 'exit' to end the conversation: hippo
# human_proxy (to agent_with_animal):
#
# hippo
#
# --------------------------------------------------------------------------------
# agent_with_animal (to human_proxy):
#
# No, that's not correct. Let me give you another hint: This animal is known for its large ears and tusks. What animal are you thinking of?
#
# --------------------------------------------------------------------------------
# Replying as human_proxy. Provide feedback to agent_with_animal. Press enter to skip and use auto-reply, or type 'exit' to end the conversation: elephant
# human_proxy (to agent_with_animal):
#
# elephant
#
# --------------------------------------------------------------------------------
#
# Process finished with exit code 0