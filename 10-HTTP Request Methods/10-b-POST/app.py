from flask import Flask, request, redirect, url_for
app = Flask(__name__)

@app.route('/index')
def index():
    return 'Ini adalah halaman index'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['un']
        password = request.form['pw']
        if username == 'dikyindrah' and password == '12345':
            return 'Login sukses, selamat datang %s' %username
        elif username == 'dikyindrah' and password != '12345':
            return 'Login gagal, password salah!'
        else:
            return 'Login gagal, username dan password tidak terdaftar.'
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)





