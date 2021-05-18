from flask import Flask

app = Flask(__name__)

# Routing Statis (Static Routing)
@app.route('/index')
def index():
    return 'ini adalah halaman index'

if __name__ == '__main__':
    app.run(debug=True)