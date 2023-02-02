import openai

# Step 1: Set up a Python environment with the necessary dependencies
# Step 2: Initialize the OpenAI API client with your API key
api_key = "YOUR_API_KEY"
openai.api_key = api_key

# Step 3: Start a new conversation by sending an initial message to the API
def start_conversation(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response["choices"][0]["text"].strip()
    return message

# Step 4: After receiving the response from the API, add the current message to the conversation history
# Step 5: Use the updated conversation history as context for the next message to the API
conversation_history = []
def continue_conversation(prompt, conversation_history):
    context = " ".join(conversation_history)
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{context} {prompt}",
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response["choices"][0]["text"].strip()
    return message

# Step 6: Repeat steps 4 and 5 until the conversation is finished
# Step 7: Save the conversation history, if desired, for future reference or analysis
def run_conversation():
    prompt = "Hello, how can I help you today?"
    conversation_history.append(prompt)
    message = start_conversation(prompt)
    conversation_history.append(message)
    print(message)

    while True:
        prompt = input("You: ")
        conversation_history.append(prompt)
        message = continue_conversation(prompt, conversation_history)
        conversation_history.append(message)
        print(f"Bot: {message}")

run_conversation()
