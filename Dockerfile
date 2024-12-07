# ベースイメージ設定
FROM python:3.10-slim

# 作業ディレクトリー設定
WORKDIR /work

# 必要なライブラリーリストコピーとインストール
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# アプリケーションコピー
COPY . .

# コンテナで実行するコマンド
CMD ["python", "main.py"]