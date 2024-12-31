from langchain.llms import OpenAI
OPENAI_API_KEY = "xxxx"


if __name__ == "__main__":
    llm = OpenAI(openai_api_key=OPENAI_API_KEY)
    res = llm("Share useful information about our solar system")
    print(res)
    print("----------------")
    gen_output = llm.generate(["A fact about Saturn", "Why Jupiter is so scary and big"])
    print(gen_output)

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

# generations=[[Generation(text=' is that it is the sixth planet from the Sun and the second-largest planet in the Solar System, after Jupiter. It is also known for its distinctive rings, made up of billions of particles of ice and dust, which orbit around the planet. Saturn has a total of 82 known moons, the largest of which is called Titan. It is a gas giant, meaning it is mostly composed of hydrogen and helium, and it has a relatively low density, meaning if placed in a giant bathtub, it would float. Saturn takes about 29 Earth years to orbit the Sun and has a day length of about 10.7 hours. It was first observed by humans in ancient times and has been a source of fascination and study ever since.', generation_info={'finish_reason': 'stop', 'logprobs': None})], [Generation(text="\n\nJupiter is the largest planet in our solar system, with a diameter over 11 times that of Earth. It is also the fifth planet from the sun, and its immense size and distance from the sun make it a mysterious and awe-inspiring object.\n\nOne of the main reasons Jupiter is so scary and big is its massive size and mass. It is more than twice as massive as all the other planets in the solar system combined. Its immense gravity is strong enough to pull in and capture numerous moons, including the four largest moons known as the Galilean moons: Io, Europa, Ganymede, and Callisto.\n\nThis gas giant is also known for its intense storms and turbulent atmosphere. Its most well-known feature is the Great Red Spot, a massive storm that has been raging on the planet's surface for hundreds of years. Jupiter's atmosphere is filled with powerful winds, lightning, and swirling clouds, making it a chaotic and unpredictable place.\n\nIn addition to its size and storms, Jupiter's composition is also a factor in why it is so scary. Unlike Earth and the other rocky planets, Jupiter is mostly made up of gas, with no solid surface to stand on. This means that if you were to somehow land on Jupiter, you would sink deeper and deeper"