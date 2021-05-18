from flask import Flask

app = Flask(__name__)

# Routing Dinamis (Dinamic Routing) dengan tipe data string
@app.route('/profile/<username>')
def profile(username):
    return 'kamu sedang berada pada halaman profile %s' %username

# Routing Dinamis (Dinamic Routing) dengan tipe data integer
@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Nomor blog %d' %postID

# Routing Dinamis (Dinamic Routing) dengan tipe data float
@app.route('/rev/<float:revNO>')
def revisi(revNO):
    return 'Nomor revisi %f' %revNO

if __name__ == '__main__':
    app.run(debug=True)