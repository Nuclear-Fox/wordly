from service import wordly_service
from flask import Flask, request, render_template

app = Flask(__name__)

@app.get("/getWord")
def get_word():
    return wordly_service.getWord(), 200

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')