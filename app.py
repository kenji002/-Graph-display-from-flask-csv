from flask import Flask, request, render_template
from utils.plot_utils import create_plot
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')  # アップロードフォーム用のHTMLテンプレート

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        graph_html = create_plot(file)
        return render_template('plot.html', graph_html=graph_html)  # プロット表示用のHTMLテンプレート
    return "ファイルがアップロードされていません。"

if __name__ == '__main__':
    app.run(debug=True)


