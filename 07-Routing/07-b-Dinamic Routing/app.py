from flask import Flask

app = Flask(__name__)

# Routing Dinamis (Dinamic Routing)
@app.route('/profile/<username>')
def index(username):
    return 'ini adalah halaman profile %s' %username

if __name__ == '__main__':
    app.run(debug=True)