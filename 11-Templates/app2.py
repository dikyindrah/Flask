from flask import Flask, render_template

app = Flask(__name__)

@app.route('/show_data')
def show_data():
    data = ['Diky Indra H', 'Ardi Wibowo', 'Tubagus M Bagas']
    return render_template('show_data.html', total_data=len(data), data=data)

if __name__ == '__main__':
    app.run(debug=True)