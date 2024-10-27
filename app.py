from flask import Flask, render_template, request, redirect, url_for
from utils.data_ut
ils import load_csv_data, get_columns
from utils.plot_utils import create_plot

app = Flask(__name__)

# ファイルアップロードの処理
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        data = load_csv_data(file)
        columns = get_columns(data)
        return render_template('select.html', columns=columns)
    return render_template('upload.html')

# データ項目選択後の処理
@app.route('/plot', methods=['POST'])
def plot():
    x_column = request.form['x_column']
    y_column = request.form['y_column']
    data = load_csv_data(request.files['file'])
    img_path = create_plot(data, x_column, y_column)
    return render_template('plot.html', img_path=img_path)

if __name__ == '__main__':
    app.run(debug=True)





