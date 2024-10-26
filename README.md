# Graph Display from Flask CSV

このプロジェクトは、Flaskフレームワークを使用してCSVファイルからデータを読み込み、Matplotlibを用いてグラフを表示するアプリケーションです。

## 概要

このアプリケーションでは、CSVファイルに保存されたデータを読み込み、Webブラウザ上でグラフを生成して表示します。ユーザーはCSVファイルをアップロードし、アップロードされたデータに基づいてグラフを生成することができます。

## 必要条件

- Python 3.x
- Flask
- Pandas
- Matplotlib
- Seaborn

## セットアップ手順

1. リポジトリをクローンします。

   ```bash
   git clone https://github.com/yourusername/Graph-display-from-flask-csv.git
   cd Graph-display-from-flask-csv
2. 必要なパッケージをインストールします。
   ```bash
    pip install -r requirements.txt
3. アプリケーションを実行します。
   ```bash
    python app.py
4. Webブラウザを開き、http://127.0.0.1:5000/にアクセスします。

**使用方法**
1. アップロードフォームにCSVファイルを選択し、[送信]ボタンをクリックします。
2. アップロードされたデータに基づいてグラフが生成され、表示されます。

**フォルダ構成**
Graph-display-from-flask-csv/  
&emsp; ├── app.py &emsp;&emsp;&emsp;&emsp; # メインアプリケーションファイル  
&emsp; ├── requirements.txt &emsp; # 必要なパッケージ一覧  
&emsp; ├── templates/ &emsp;&emsp;&emsp;&emsp; # HTMLテンプレートフォルダ  
&emsp;&emsp;&emsp; ├── upload.html &emsp;&emsp; # アップロードフォーム  
&emsp;&emsp;&emsp; └── plot.html &emsp;&emsp;&emsp; # グラフ表示用テンプレート  
&emsp; └── static/ &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; # 静的ファイル（CSS, JS等）


**ライセンス**
このプロジェクトはMITライセンスのもとで公開されています。詳しくは、LICENSEファイルをご覧ください。
作者
kenji002
.
└── Edit me to generate/
    ├── a/
    │   └── nice/
    │       └── tree/
    │           ├── diagram!
    │           └── :)
    └── Use indentation/
        ├── to indicate/
        │   ├── file
        │   ├── and
        │   ├── folder
        │   └── nesting.
        └── You can even/
            └── use/
                ├── markdown
                └── bullets!
