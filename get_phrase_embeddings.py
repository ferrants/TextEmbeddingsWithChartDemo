import json
from datetime import datetime
from pydantic import BaseModel
from openai import OpenAI

OPEN_AI_KEY = "ADD API KEY"
OPEN_AI_ORG = "ADD ORG ID"


class StringEmbedding(BaseModel):
    text: str
    happy_scale: int
    sad_scale: int
    angry_scale: int
    excited_scale: int
    bored_scale: int
    about_summer_scale: int
    about_winter_scale: int
    about_clothes_scale: int
    about_food_scale: int
    about_sports_scale: int
    about_music_scale: int
    about_movies_scale: int
    about_books_scale: int
    about_technology_scale: int

class StringEmbeddingsResponse(BaseModel):
    collection: list[StringEmbedding]


client = OpenAI(api_key=OPEN_AI_KEY, organization=OPEN_AI_ORG)

phrases = [
    "it's really cold today, glad I have my warm jacket and some hot chocolate",
    "I'm so excited for the summer, I can't wait to go to the beach and have a picnic",
    "I love winter, it's so cozy and I get to wear my favorite sweaters",
    "I'm going to a concert this weekend, I can't wait to hear my favorite band",
    "I'm going to watch a movie tonight, I love watching movies",
    "I'm going to read a book tonight, I love reading books",
    "I'm going to play some video games tonight, I love playing video games",
    "I'm really tired from work today, I can't wait to relax and watch some TV",
    "I'm super excited about our new project at work, I can't wait to get started",
]
phrase_str = "\n".join(phrases)

prompt = f"""You are helping categorize a bunch of phrases by assigning them a 0-10 rating for how much the text relates to a number of different scales.

Here are the phrases for categorization, each on their own line:
<Phrases>
{phrase_str}
</Phrases>

Now, apply a 0-10 rating for each phrase in this collection of phrases, relative to each other. Use the full 0-10 range of the scale.
"""

print("Requesting")
completion = client.beta.chat.completions.parse(
    model="gpt-4o-2024-08-06",
    messages=[
        {"role": "user", "content": prompt}
    ],
    response_format=StringEmbeddingsResponse,
)

parsed_response = completion.choices[0].message.parsed
json_response = parsed_response.model_dump()
response_as_str = json.dumps(json_response, indent=2)
print(response_as_str)

date_str_now = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
filename = f"response_{date_str_now}.json"

print(f"Writing to {filename}")
with open(filename, "w") as f:
    f.write(response_as_str)
    
print("Complete")

