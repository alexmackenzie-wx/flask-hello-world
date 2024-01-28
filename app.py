from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return "Armin, would love to chat sometime: <a href='mailto:alex@tapestry.vc'>alex@tapestry.vc</a>"

@app.route('/example', methods=['GET'])
def example_route():
    # Your custom function logic goes here
    # This function will be invoked when a GET request is made to "/example"
    return "Hello Why Now reader, consider subscribing?"

if __name__ == '__main__':
    app.run(debug=True)
