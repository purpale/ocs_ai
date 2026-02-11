from flask import Flask, request, jsonify
import anthropic

client = anthropic.Anthropic(
    api_key="ms-6604cae5-d73b-4fb4-9e56-c5d74b461eaa", # 请替换成您的ModelScope Access Token
    base_url="https://api-inference.modelscope.cn")

app = Flask(__name__)

@app.route('/wenti', methods=['GET'])
def wenti():
    # 获取查询参数
    title = request.args.get('title')
    options = request.args.get('options')
    ty_pe = request.args.get('type')
    
    # print(title)
    message = client.messages.create(
        model="Qwen/Qwen2.5-7B-Instruct", # ModelScope Model-Id
        messages=[
            {"role": "user", "content": f"请回答{ty_pe}问题，并输出对应的选项答案。不要输出思考过程！只要答案！题目是{title}；选项是{options}"}
        ],
        max_tokens = 1024
    )
    print(message.content[0].text)
    # 处理请求并返回响应
    return jsonify({
        "code": 1,
        "question": title,
        "answer": message.content[0].text
    })

if __name__ == '__main__':
    app.run(debug=True)
