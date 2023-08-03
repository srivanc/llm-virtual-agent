import json
import config

import openai

openai.api_key = config.OPENAI_API_KEY

def create_chat_response(prompt) :
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=prompt,
      max_tokens=140,
      temperature=1,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0,
    )

    #print(response['choices'][0]['text'].strip())

    return response['choices'][0]['text'].strip()

def main():

    with open('prompts/initial_prompt.txt') as f:
        initial_prompt = f.read()

    print('I am now Initializing as a Chatbot \n')
    response = create_chat_response(initial_prompt)
    print(response.strip())
    print('I am now Ready as a Chatbot \n')


    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        prompt = f"{initial_prompt}\nYou: {user_input}\nChatBot:"
        response = create_chat_response(prompt)
        print(response.strip())
        print('\n')

if __name__ == "__main__":
    main()









