from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return "check out my actual blog at: mack.work"

@app.route('/example', methods=['GET'])
def example_route():
    # Your custom function logic goes here
    # This function will be invoked when a GET request is made to "/example"
    return "What’s up, h@ckɇr."

if __name__ == '__main__':
    app.run(debug=True)
