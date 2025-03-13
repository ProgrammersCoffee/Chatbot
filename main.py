from transformers import pipeline

chatbot = pipeline("text-generation", model="bigscience/bloomz-560m")
user_message = "what would i cook for dinner "
response=chatbot(user_message)
print(response)
