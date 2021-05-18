from flask import Flask

app = Flask(__name__)

# Routing ke url http://127.0.0.1:5000/index
@app.route('/index')
def index():
    return 'ini adalah halaman index'

if __name__ == '__main__':
    app.run(debug=True)