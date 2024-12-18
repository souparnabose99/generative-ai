from dotenv import load_dotenv

load_dotenv()


def get_text_length(text:str) -> int:
    """"""
    return len(text)


if __name__ == "__main__":
    print(get_text_length(text="abcde"))
