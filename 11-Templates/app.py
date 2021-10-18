from flask import Flask, render_template

app = Flask(__name__)

@app.route('/login/<username>')
def login(username):
    return render_template('login.html', username=username)

if __name__ == '__main__':
    app.run(debug=True)