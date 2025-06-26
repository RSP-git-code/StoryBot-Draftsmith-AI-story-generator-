#importing req libraries
import openai
#  OpenAI API key
openai.api_key=""
# Initial Prompt to the chatbot
messages = [
    {"role": "system", "content": "You are a creative and professional story-writing  assistant. Draft  a story exactly specified by the user."}
]
print("AI Story Generator ")
#User input
while True:
    user_input = input("You: ").strip()
    #Break condition
    if user_input == "":
        print("Story Ended.If you want to generate a new story write a new prompt or enter continue with story.\n")
        break

    # Add user input to message history
    messages.append({"role": "user", "content": user_input})

    # Generate the AI's story continuation
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini-2024-07-18", 
            messages=messages,
            temperature=0.8,
            max_tokens=300
        )

        reply = response["choices"][0]["message"]["content"].strip()
        print(f"\nAI: {reply}\n")

        # Add the AI's response to the conversation
        messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        print(f" Error: {e}")
        break

