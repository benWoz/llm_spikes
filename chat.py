import openai
import os

private_key = os.environ.get('CHATGPT_KEY')

openai.api_key = private_key

model_engine = "text-davinci-003"
prompt = "Hello, how are you today?"

completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5
)

response = completion.choices[0].text
print(response)