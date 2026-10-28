from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")  # clé bidon, ignorée
r = client.chat.completions.create(
    model="ministral-3:3b",
    messages=[{"role": "user", "content": "Bonjour"}],
)
print(r.choices[0].message.content)