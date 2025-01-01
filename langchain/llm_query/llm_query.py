from langchain.llms import OpenAI
OPENAI_API_KEY = ""


if __name__ == "__main__":
    llm = OpenAI(openai_api_key=OPENAI_API_KEY)
    res = llm("Share useful information about our solar system")
    print(res)
    print("----------------")
    gen_output = llm.generate(["A fact about Saturn", "Why Jupiter is so scary and big"])
    print(gen_output)
    print(gen_output.model_json_schema())
    print(gen_output.llm_output)

# LLM Output:

# 1. The solar system is approximately 4.6 billion years old.
#
# 2. It consists of the Sun, eight planets, and numerous other smaller objects such as moons, asteroids, and comets.
#
# 3. The four inner planets (Mercury, Venus, Earth, and Mars) are known as the terrestrial planets, as they are made mostly of rock and metal.
#
# 4. The four outer planets (Jupiter, Saturn, Uranus, and Neptune) are known as the gas giants, as they are primarily made of gas and have no solid surface.
#
# 5. The Sun makes up over 99% of the total mass of the solar system.
#
# 6. The largest planet in the solar system is Jupiter, while the smallest is Mercury.
#
# 7. The Earth is the only planet in the solar system known to have life.
#
# 8. The asteroid belt is located between the orbits of Mars and Jupiter and contains thousands of small rocky objects.
#
# 9. The Kuiper Belt is a region beyond Neptune that contains icy objects, including dwarf planets such as Pluto and Eris.
#
# 10. The Oort Cloud is a theoretical sphere of icy bodies that is believed to surround the solar system and marks the outer boundary.
#
# 11. The distance from the Sun to Earth is approximately 93

# generations=[[Generation(text=' is that it is the sixth planet from the Sun and the second-largest planet in the Solar System, after Jupiter. It is also known for its distinctive rings, made up of billions of particles of ice and dust, which orbit around the planet. Saturn has a total of 82 known moons, the largest of which is called Titan. It is a gas giant, meaning it is mostly composed of hydrogen and helium, and it has a relatively low density, meaning if placed in a giant bathtub, it would float. Saturn takes about 29 Earth years to orbit the Sun and has a day length of about 10.7 hours. It was first observed by humans in ancient times and has been a source of fascination and study ever since.', generation_info={'finish_reason': 'stop', 'logprobs': None})], [Generation(text="\n\nJupiter is the largest planet in our solar system, with a diameter over 11 times that of Earth. It is also the fifth planet from the sun, and its immense size and distance from the sun make it a mysterious and awe-inspiring object.\n\nOne of the main reasons Jupiter is so scary and big is its massive size and mass. It is more than twice as massive as all the other planets in the solar system combined. Its immense gravity is strong enough to pull in and capture numerous moons, including the four largest moons known as the Galilean moons: Io, Europa, Ganymede, and Callisto.\n\nThis gas giant is also known for its intense storms and turbulent atmosphere. Its most well-known feature is the Great Red Spot, a massive storm that has been raging on the planet's surface for hundreds of years. Jupiter's atmosphere is filled with powerful winds, lightning, and swirling clouds, making it a chaotic and unpredictable place.\n\nIn addition to its size and storms, Jupiter's composition is also a factor in why it is so scary. Unlike Earth and the other rocky planets, Jupiter is mostly made up of gas, with no solid surface to stand on. This means that if you were to somehow land on Jupiter, you would sink deeper and deeper"

# {'$defs': {'BaseMessage': {'additionalProperties': True, 'description': 'Base abstract message class.\n\nMessages are the inputs and outputs of ChatModels.', 'properties': {'content': {'anyOf': [{'type': 'string'}, {'items': {'anyOf': [{'type': 'string'}, {'type': 'object'}]}, 'type': 'array'}], 'title': 'Content'}, 'additional_kwargs': {'title': 'Additional Kwargs', 'type': 'object'}, 'response_metadata': {'title': 'Response Metadata', 'type': 'object'}, 'type': {'title': 'Type', 'type': 'string'}, 'name': {'anyOf': [{'type': 'string'}, {'type': 'null'}], 'default': None, 'title': 'Name'}, 'id': {'anyOf': [{'type': 'string'}, {'type': 'null'}], 'default': None, 'title': 'Id'}}, 'required': ['content', 'type'], 'title': 'BaseMessage', 'type': 'object'}, 'BaseMessageChunk': {'additionalProperties': True, 'description': 'Message chunk, which can be concatenated with other Message chunks.', 'properties': {'content': {'anyOf': [{'type': 'string'}, {'items': {'anyOf': [{'type': 'string'}, {'type': 'object'}]}, 'type': 'array'}], 'title': 'Content'}, 'additional_kwargs': {'title': 'Additional Kwargs', 'type': 'object'}, 'response_metadata': {'title': 'Response Metadata', 'type': 'object'}, 'type': {'title': 'Type', 'type': 'string'}, 'name': {'anyOf': [{'type': 'string'}, {'type': 'null'}], 'default': None, 'title': 'Name'}, 'id': {'anyOf': [{'type': 'string'}, {'type': 'null'}], 'default': None, 'title': 'Id'}}, 'required': ['content', 'type'], 'title': 'BaseMessageChunk', 'type': 'object'}, 'ChatGeneration': {'description': 'A single chat generation output.\n\nA subclass of Generation that represents the response from a chat model\nthat generates chat messages.\n\nThe `message` attribute is a structured representation of the chat message.\nMost of the time, the message will be of type `AIMessage`.\n\nUsers working with chat models will usually access information via either\n`AIMessage` (returned from runnable interfaces) or `LLMResult` (available\nvia callbacks).', 'properties': {'text': {'default': '', 'title': 'Text', 'type': 'string'}, 'generation_info': {'anyOf': [{'type': 'object'}, {'type': 'null'}], 'default': None, 'title': 'Generation Info'}, 'type': {'const': 'ChatGeneration', 'default': 'ChatGeneration', 'title': 'Type', 'type': 'string'}, 'message': {'$ref': '#/$defs/BaseMessage'}}, 'required': ['message'], 'title': 'ChatGeneration', 'type': 'object'}, 'ChatGenerationChunk': {'description': 'ChatGeneration chunk, which can be concatenated with other\nChatGeneration chunks.', 'properties': {'text': {'default': '', 'title': 'Text', 'type': 'string'}, 'generation_info': {'anyOf': [{'type': 'object'}, {'type': 'null'}], 'default': None, 'title': 'Generation Info'}, 'type': {'const': 'ChatGenerationChunk', 'default': 'ChatGenerationChunk', 'title': 'Type', 'type': 'string'}, 'message': {'$ref': '#/$defs/BaseMessageChunk'}}, 'required': ['message'], 'title': 'ChatGenerationChunk', 'type': 'object'}, 'Generation': {'description': 'A single text generation output.\n\nGeneration represents the response from an "old-fashioned" LLM that\ngenerates regular text (not chat messages).\n\nThis model is used internally by chat model and will eventually\nbe mapped to a more general `LLMResult` object, and then projected into\nan `AIMessage` object.\n\nLangChain users working with chat models will usually access information via\n`AIMessage` (returned from runnable interfaces) or `LLMResult` (available\nvia callbacks). Please refer the `AIMessage` and `LLMResult` schema documentation\nfor more information.', 'properties': {'text': {'title': 'Text', 'type': 'string'}, 'generation_info': {'anyOf': [{'type': 'object'}, {'type': 'null'}], 'default': None, 'title': 'Generation Info'}, 'type': {'const': 'Generation', 'default': 'Generation', 'title': 'Type', 'type': 'string'}}, 'required': ['text'], 'title': 'Generation', 'type': 'object'}, 'GenerationChunk': {'description': 'Generation chunk, which can be concatenated with other Generation chunks.', 'properties': {'text': {'title': 'Text', 'type': 'string'}, 'generation_info': {'anyOf': [{'type': 'object'}, {'type': 'null'}], 'default': None, 'title': 'Generation Info'}, 'type': {'const': 'Generation', 'default': 'Generation', 'title': 'Type', 'type': 'string'}}, 'required': ['text'], 'title': 'GenerationChunk', 'type': 'object'}, 'RunInfo': {'description': 'Class that contains metadata for a single execution of a Chain or model.\n\nDefined for backwards compatibility with older versions of langchain_core.\n\nThis model will likely be deprecated in the future.\n\nUsers can acquire the run_id information from callbacks or via run_id\ninformation present in the astream_event API (depending on the use case).', 'properties': {'run_id': {'format': 'uuid', 'title': 'Run Id', 'type': 'string'}}, 'required': ['run_id'], 'title': 'RunInfo', 'type': 'object'}}, 'description': 'A container for results of an LLM call.\n\nBoth chat models and LLMs generate an LLMResult object. This object contains\nthe generated outputs and any additional information that the model provider\nwants to return.', 'properties': {'generations': {'items': {'items': {'anyOf': [{'$ref': '#/$defs/Generation'}, {'$ref': '#/$defs/ChatGeneration'}, {'$ref': '#/$defs/GenerationChunk'}, {'$ref': '#/$defs/ChatGenerationChunk'}]}, 'type': 'array'}, 'title': 'Generations', 'type': 'array'}, 'llm_output': {'anyOf': [{'type': 'object'}, {'type': 'null'}], 'default': None, 'title': 'Llm Output'}, 'run': {'anyOf': [{'items': {'$ref': '#/$defs/RunInfo'}, 'type': 'array'}, {'type': 'null'}], 'default': None, 'title': 'Run'}, 'type': {'const': 'LLMResult', 'default': 'LLMResult', 'title': 'Type', 'type': 'string'}}, 'required': ['generations'], 'title': 'LLMResult', 'type': 'object'}

# {'token_usage': {'prompt_tokens': 11, 'total_tokens': 372, 'completion_tokens': 361}, 'model_name': 'gpt-3.5-turbo-instruct'}
