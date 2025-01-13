import os
from autogen import AssistantAgent, UserProxyAgent
from dotenv import load_dotenv

load_dotenv()

model = "gpt-4o-mini"
llm_config = {
    "model": model,
    "api_key": os.environ.get("OPENAI_API_KEY"),
}

assistant = AssistantAgent("Assistant-Agent", llm_config)
user_proxy = UserProxyAgent(
    "User-Proxy",
    llm_config=llm_config,
    code_execution_config={
        "workd_dir": "code_execution",
        "use_docker": False,
    },
    human_input_mode="NEVER",
)

# start the agents
user_proxy.initiate_chat(
    assistant,
    message="What is the famous about Portugal?",
)

# Output:

# User-Proxy (to Assistant-Agent):
#
# What is the famous about Portugal?
#
# --------------------------------------------------------------------------------
# Assistant-Agent (to User-Proxy):
#
#
#
# --------------------------------------------------------------------------------
# User-Proxy (to Assistant-Agent):
#
# Portugal is famous for a variety of reasons, including:
#
# 1. **Historic Cities**: Cities like Lisbon and Porto are known for their rich history, stunning architecture, and vibrant culture. The historic neighborhoods, such as Alfama in Lisbon and Ribeira in Porto, attract many visitors.
#
# 2. **Fado Music**: This traditional genre of music is characterized by its melancholic and expressive style, often dealing with themes of longing and nostalgia. Fado is a UNESCO-recognized cultural heritage.
#
# 3. **Port Wine**: The Douro Valley is famous for producing Port wine, a fortified wine that is highly regarded worldwide. The cellars in Porto are a popular destination for wine tasting.
#
# 4. **Beautiful Landscapes**: Portugal boasts diverse landscapes ranging from rolling hills and countryside in the Alentejo region to stunning beaches in the Algarve. The Azores and Madeira islands are also renowned for their natural beauty.
#
# 5. **Cork Production**: Portugal is the largest producer of cork in the world, known for its high-quality cork oak trees. This sustainable material is used for wine stoppers, flooring, and various products.
#
# 6. **Azulejos**: These colorful ceramic tiles are a hallmark of Portuguese architecture and can be seen adorning buildings, churches, and even metro stations.
#
# 7. **Pastéis de Nata**: These delicious custard tarts are a beloved Portuguese pastry. They are often enjoyed with coffee and are a must-try for visitors.
#
# 8. **Exploration History**: Portugal has a rich maritime history, being a leading nation during the Age of Discoveries in the 15th and 16th centuries. Famous explorers like Vasco da Gama and Ferdinand Magellan were Portuguese.
#
# 9. **UNESCO Sites**: Portugal is home to numerous UNESCO World Heritage Sites, including the Tower of Belém, the Monastery of Batalha, and the cultural landscape of Sintra.
#
# 10. **Friendly Culture**: The Portuguese people are known for their hospitality, making visitors feel welcome and at home.
#
# These elements, among others, contribute to Portugal's unique charm and allure as a travel destination.
#
# --------------------------------------------------------------------------------
# Assistant-Agent (to User-Proxy):
