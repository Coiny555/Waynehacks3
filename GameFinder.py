from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask! Goodbye boi!"

if __name__ == '__main__':
    app.run(debug=True)

#This is, I believe a test file to set up flask, may make changes later