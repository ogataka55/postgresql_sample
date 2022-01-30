import os

from dotenv import load_dotenv

load_dotenv()  # .envの読み取り

print(os.environ.get("SECRET"))  # 環境変数を参照
