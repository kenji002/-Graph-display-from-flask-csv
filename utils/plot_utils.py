import pandas as pd
import plotly.express as px
import plotly.io as pio
from io import StringIO

def create_plot(file) -> str:
    """CSVファイルからデータを読み込み、プロットを生成し、HTMLとして返す"""
    
    # CSVファイルの読み込み
    data = pd.read_csv(StringIO(file.read().decode('utf-8')))
    
    # Plotlyでグラフを作成
    fig = px.line(data, x='X軸列名', y='Y軸列名')  # 適切な列名に変更

    # グラフをHTMLに変換
    graph_html = pio.to_html(fig, full_html=False)

    return graph_html






