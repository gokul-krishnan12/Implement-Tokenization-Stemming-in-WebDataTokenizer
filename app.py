from flask import Flask, render_template, request
from nlp_processor import process_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    input_text = ""

    if request.method == "POST":
        input_text = request.form["text"]
        result = process_text(input_text)

    return render_template("index.html", input_text=input_text, result=result)

if __name__ == "__main__":
    app.run(debug=True)
