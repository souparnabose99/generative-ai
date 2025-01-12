import os
from autogen import AssistantAgent, UserProxyAgent, ConversableAgent
from dotenv import load_dotenv
import warnings
warnings.simplefilter(action="ignore")

load_dotenv()

model = "gpt-4o-mini"

llm_config = {
    "model": model,
    "api_key": os.environ.get("OPENAI_API_KEY")
}

agent = ConversableAgent(
    name="ai-agent",
    llm_config=llm_config,
    code_execution_config=False,
    human_input_mode="NEVER"
)

response = agent.generate_reply(messages=[{"role": "user", "content": "What is AGI?"}])
print(response)

# Output:
# AGI, or Artificial General Intelligence, refers to a type of artificial intelligence that has the ability to understand, learn, and apply intelligence across a wide range of tasks, mimicking human cognitive abilities. Unlike narrow AI, which is designed to perform specific tasks (like language translation or playing chess), AGI would be able to perform any intellectual task that a human can do, exhibiting abilities such as reasoning, problem-solving, understanding complex ideas, learning from experience, and adapting to new situations.
#
# Key characteristics of AGI include:
#
# 1. **Versatility**: AGI can perform a wide variety of tasks rather than being limited to one domain.
# 2. **Autonomous Learning**: It can learn and improve its capabilities autonomously, similar to how humans learn from experience.
# 3. **Understanding Context**: AGI should be able to understand context and nuance, which are often crucial for human reasoning and decision-making.
# 4. **Reasoning and Problem-Solving**: It should be equipped with the ability to reason, solve problems, and plan in complex and dynamic environments.
#
# As of now, AGI remains a theoretical concept, and achieving it poses significant technical and ethical challenges. Current AI systems, including those utilizing advanced machine learning techniques, are still classified as narrow AI.