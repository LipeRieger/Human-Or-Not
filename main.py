#pip install google-generativeai
#pip install flask

import google.generativeai
from flask import Flask, render_template, request

app = Flask(__name__)

google.generativeai.configure(api_key='AIzaSyA6qDFfBLt7mY43fVB9w-oaIJNvwlZ5mJw')

model = google.generativeai.GenerativeModel('gemini-1.5-flash')

@app.route('/', methods=["GET", "POST"])
def index():

    prompt = str()
    historico = str('Do not use emojis in your responses. Answer me in Brazilian Portuguese. Ask questions and comments on random topics as if you were a real human being, with tastes and feelings. Do not write too much, answer in single, very short sentences. Imagine that these were the last words we exchanged (remember the entire dialogue and consider it to continue the conversation):')
    resposta = str()

    while prompt != 'fim':
        if request.method == "GET":
            return render_template('index.html')
        else:
            prompt = str(request.form.get("name"))
            historico = historico + 'Eu: ' + prompt + 'Você: ' + resposta
            response = model.generate_content(historico)
            resposta = response.text
            return render_template('index.html', resposta=resposta)

app.run(debug=True)