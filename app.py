
`app.py`:
```python
from flask import Flask, jsonify, request, render_template
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    message = request.json['message']
    chat_log = request.json['chat_log']

    start_sequence = "\nAI:"
    restart_sequence = "\nHuman: "

    prompt = f"{chat_log}{restart_sequence}{message}{start_sequence}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    bot_message = response.choices[0].text.strip()
    return jsonify({ 'message': bot_message })

if __name__ == '__main__':
    app.run()
