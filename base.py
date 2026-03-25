from transformers import pipeline

chatbot = pipeline("text-generation", model="bigscience/bloomz-560m")
# updates
conv_history = ""
while True:
    user_message = input("You: ")
    if user_message.lower() == "exit":
        break
    conv_history = conv_history + f"{user_message}"

    response = chatbot(conv_history, max_length=50, truncation=True, do_sample=True, temperature=0.7, top_k=50,
                       num_return_sequences=1)
    bot_reply = response[0]["generated_text"].replace(conv_history, "").strip()
    print("Bot:", bot_reply)
    conv_history += bot_reply + "\n"
