from langchain.llms import OpenAI
OPENAI_API_KEY = "xxxxxx"


if __name__ == "__main__":
    llm = OpenAI(openai_api_key=OPENAI_API_KEY)
    res = llm("Share useful information about our solar system")
    print(res)

# LLM Output:

# 1. The Solar System is made up of the Sun, eight planets, and various smaller objects such as comets, asteroids, and moons.
#
# 2. The Sun is a massive, glowing ball of gas that provides light and heat to the planets in our Solar System. It makes up about 99.8% of the total mass of the entire Solar System.
#
# 3. The eight planets in our Solar System are Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune. They are divided into two categories: the inner planets (Mercury, Venus, Earth, and Mars) and the outer planets (Jupiter, Saturn, Uranus, and Neptune).
#
# 4. The Solar System is about 4.6 billion years old and formed from a giant cloud of gas and dust called the solar nebula.
#
# 5. The four inner planets are known as the terrestrial planets because they are small, rocky, and have solid surfaces. The outer planets, also called gas giants, are much larger and mostly made up of gas and ice.
#
# 6. The asteroid belt, located between Mars and Jupiter, is a region of the Solar System where many small rocky bodies called asteroids orbit the Sun.
#
# 7. The Kuiper Belt is a region of the Solar