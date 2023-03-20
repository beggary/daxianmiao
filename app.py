from flask import Flask, render_template, request
import openai
import urllib3
import os

app = Flask(__name__)
urllib3.disable_warnings()
# %%
openai.api_key = "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"

# %%
# os.environ["HTTPS_PROXY"] = '172.104.102.91:8080'


# os.environ['HTTPS_PROXY'] = 'http://185.160.26.114:80'


@app.route('/')
def index():
    return render_template("2.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.route('/chatGPT', methods=['POST'])
def chatGPT():
    while True:
        inputText = request.form['inputText']
        messages = [{"role": "system", "content": inputText}]
        response = openai.ChatCompletion.create(

            model="gpt-3.5-turbo",

            messages=messages
        )
        # 后台打印
        print(inputText)
        print(response.get("choices")[0]["message"]["content"])
        talk = response.get("choices")[0]["message"]["content"]
        messages.append({"role": "system", "content": talk})
        return talk


# if __name__ == '__main__':
# chatGPT("")
# app.run()
