import openai

# Set your OpenAI GPT-2 API key
openai.api_key = 'YOUR_API_KEY'

# Define the function to interact with the GPT-2 API
def ask_gpt2(question, model="text-davinci-002"):
    response = openai.Completion.create(
        engine=model,
        prompt=question,
        max_tokens=100,
    )
    return response.choices[0].text.strip()

# Chat with the GPT-2 model
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Exiting...")
        break
    answer = ask_gpt2(user_input)
    print(f"ChatGPT2: {answer}")
