import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from pathlib import Path

def set_font():
    # フォントファイルへのパスを指定
    font_path = Path("static/fonts/NotoSerifJP-Regular.ttf")  # フォントファイルの実際のパス
    font_prop = fm.FontProperties(fname=font_path)
    
    # フォント設定
    plt.rcParams['font.family'] = font_prop.get_name()

set_font()
