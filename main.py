import openai

# Set your API key
openai.api_key = "YOUR_API_KEY"

# Choose the API endpoint you want to use
model_engine = "text-davinci-002"

# Define the prompt
prompt = "What is the meaning of life?"

# Generate a response
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Print the response
print(response["choices"][0]["text"])
