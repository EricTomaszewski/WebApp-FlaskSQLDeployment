# print("Hello, World!")

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_world():
  return render_template("home.html")
  # return "<p>Hello, World!</p>"


if __name__ == "__main__":
  print("I'm inside if now")
  app.run(host="0.0.0.0", debug=True)
