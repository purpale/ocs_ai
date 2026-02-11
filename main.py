import anthropic

client = anthropic.Anthropic(
    api_key="", # 请替换成您的ModelScope Access Token
    base_url="https://api-inference.modelscope.cn")

message = client.messages.create(
    model="Qwen/Qwen2.5-7B-Instruct", # ModelScope Model-Id
    messages=[
        {"role": "user", "content": "write a python quicksort"}
    ],
    max_tokens = 1024
)
print(message.content[0].text)