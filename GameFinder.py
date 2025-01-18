from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #For the pages on the app 
def home():
    return render_template('home.html')

@app.route('/about') #For the about page
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(debug=True)

#This is, I believe a test file to set up flask, may make changes later