from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return "Armin, would love to chat sometime: <a href='mailto:alex@tapestry.vc'>alex@tapestry.vc</a>"

if __name__ == '__main__':
    app.run(debug=True)
