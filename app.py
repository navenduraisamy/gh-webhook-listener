from flask import Flask, request
import json

# Create a Flask app
app = Flask(__name__)

# Define a route and a view function
@app.route('/')
def hello_world():
    return 'Hello, World! This is a simple Flask server.'

@app.route('/wh',methods=['POST'])
def foo():
   data = json.loads(request.data)
   print(data)
   return "OK"


if __name__ == '__main__':
    # Run the app
    app.run(debug=True)
