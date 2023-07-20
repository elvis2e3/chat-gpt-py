import openai


def chat_gpt(text: str) -> str:
    openai.api_key = "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"


    # create a chat completion
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "user", "content": text}]
    )

    # print the chat completion
    return chat_completion.choices[0].message.content


