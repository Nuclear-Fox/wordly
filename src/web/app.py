# -*- coding: utf-8 -*-

import wordly_service
from flask import Flask, request, render_template

app = Flask(__name__)

@app.get("/getWord")
def get_word():
    return wordly_service.get_word(), 200

@app.post("/checkWord")
def check_word():
    word = request.form["word"]
    result_word = request.form["resultWord"]
    print(word, result_word)
    res = wordly_service.check_word(word, result_word)
    print(res)
    return res

@app.get("/")
def start():
    return render_template("wordly.html")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')