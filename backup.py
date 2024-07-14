#pip install google-generativeai

import google.generativeai

google.generativeai.configure(api_key='AIzaSyA6qDFfBLt7mY43fVB9w-oaIJNvwlZ5mJw')

model = google.generativeai.GenerativeModel('gemini-1.5-flash')


prompt = str()
historico = str()
resposta = str()

while prompt != 'fim':
    prompt = input('You:')
    response = model.generate_content('Do not use emojis in your responses. Answer me in Brazilian Portuguese. Ask questions and comments about random topics as if you were a real human being, with likes and feelings, and we did not know each other. Do not write too much, answer in single, very short sentences. Imagine these were the last words we exchanged:' + historico + '. ' + prompt)
    resposta = response.text
    historico = historico + prompt + resposta
    print(resposta)
