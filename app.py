from flask import Flask, render_template, request
from finance_ai import finance_advice

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():

    answer = ""

    if request.method == "POST":

        query = request.form["query"]

        answer = finance_advice(query)

    return render_template("index.html", answer=answer)


if __name__ == "__main__":
    app.run(debug=True)