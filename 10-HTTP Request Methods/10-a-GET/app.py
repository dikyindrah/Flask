from flask import Flask, request, redirect, url_for
app = Flask(__name__)

@app.route('/index')
def index():
    return 'Ini adalah halaman index'

@app.route('/search', methods=['GET','POST'])
def search():
    if request.method == 'GET':
        # Pernyataan untuk satu query
        buah = request.args.get('buah')
        if buah == 'jeruk':
            return 'Hasil pencarian: buah %s ditemukan.' %buah
        else:
            return 'Hasil pencarian: buah %s tidak ditemukan.' %buah

        # # Pernyataan untuk lebih dari satu query
        # # Buka url http://127.0.0.1:5000/search?buah=jeruk&sayur=brokoli
        # buah = request.args.get('buah')
        # sayur = request.args.get('sayur')
        # return 'Hasil pencarian: buah %s dan sayur %s ditemukan.' %(buah, sayur)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

