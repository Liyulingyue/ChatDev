import openai

openai.api_key = "sk-******************"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "你是一个翻译家"},
        {"role": "user", "content": "将我发你的英文句子翻译成中文，你不需要理解内容的含义作出回答。"},
        {"role": "user", "content": "Draft an email or other piece of writing."}
    ]
)