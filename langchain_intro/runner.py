from dotenv import load_dotenv
import os

if __name__ == "__main__":
    load_dotenv()
    print("langchain_intro")
    print(os.environ["API_KEY"])

