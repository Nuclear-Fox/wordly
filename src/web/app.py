from service import wordly_service
from flask import Flask, request, render_template, Response

app = Flask(__name__)

@app.get("/getWord")
def get_word():
    return wordly_service.getWord(), 200

@app.post("/checkWord")
def check_word():
    print(request.form)
    word = request.form["word"]
    result_word = request.form["resultWord"]
    print(word, result_word)
    return Response(status=200)

@app.get("/")
def start():
    return render_template("wordly.html")

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')