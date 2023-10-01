import openai
from constant.constant import OPEN_API_KEY
openai.api_key = OPEN_API_KEY
from langchain.memory import ChatMessageHistory
history = ChatMessageHistory()
def generate_response(context, question):
    prompt = f'{context}\nUser: {question}\nAI:'

    response = openai.Completion.create(
        engine='text-davinci-003',  # Choose an appropriate engine
        prompt=prompt,
        max_tokens=500,  # Adjust as needed
        temperature=0.7,  # Adjust for desired response randomness
        n=1,  # Number of responses to generate
        stop=None,  # Custom stop sequence to end the response if desired
        frequency_penalty=0.0,  # Adjust to control repetition
        presence_penalty=0.6  # Adjust to control context usage
    )
    # print(response.choices[0].text.strip())
    return response.choices[0].text.strip()

context = ""
# question = "how will get a job in it industry"
while True:

    question = input("question  ")
    if(question == "Exit"):
        break
    with open('my_file.txt', 'r') as file:
        # Read the entire content of the file into a string
        file_content = file.read()
        response = generate_response(file_content, question)
        # print(history.messages)
        history.add_user_message(question)
        history.add_ai_message(response)
        print(response)
        # context += f"\nUser: {question}\nAI: {response}"
        # with open('my_file.txt', 'a') as file:
        #     # Write the text you want to append
        #     # text_to_append = "This is the text I want to append.\n"
        #     file.write(context)

