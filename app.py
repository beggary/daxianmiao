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
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


@app.route('/chatGPT', methods=['POST'])
def chatGPT():
    inputText = request.form['inputText']
    user_ip = request.remote_addr
    response = openai.ChatCompletion.create(

        model="gpt-3.5-turbo",

        messages=[
            # {"role": "system", "content": "Python开发经验的资深算法工程师"},
            #
            {"role": "user", "content": inputText}
        ]
    )
    talk = response.get("choices")[0]["message"]["content"]
    return talk


# if __name__ == '__main__':
# chatGPT("")
# app.run()
