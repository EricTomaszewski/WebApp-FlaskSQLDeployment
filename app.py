# print("Hello, World!")

from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': '$100,000',
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': '$120,000',
  },
  {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    #'salary': '$140,000',
  },
  {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': "$200,000",
  }
]


@app.route("/")
def hello_world():
  return render_template("home.html", 
                         jobs=JOBS, 
                         owner="by Eric")
  # return "<p>Hello, World!</p>"

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  print("I'm inside if now")
  app.run(host="0.0.0.0", debug=True)
