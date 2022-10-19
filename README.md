# kslife-cheats

# 概要  
K's lifeにseleniumでアクセスして、自動出席登録もしくはアンケート回答をdiscord.pyを使ったDiscordのbot経由で実行する。  
  
# メモ(個人用)  
コマンドプロンプトで ```python -m venv venv``` で仮想環境を構築し、pipでパッケージをプロジェクト別に導入する事が出来る。(https://qiita.com/fiftystorm36/items/b2fd47cf32c7694adc2e)  
仮想環境内で動作するには ```.\venv\Scripts\activate```  
終了する場合 ```deactivate```  
パッケージ確認 ```pip freeze```  
パッケージインストール ```pip install パッケージ名```  
requirements.txtへパッケージ一覧を出力する ```pip freeze > requirements.txt```  
requirements.txtから一括でパッケージをインストールする ```pip install -r requirements.txt```  
パッケージをすべて削除する（基本的に個々で削除すること）  
```pip freeze > removepackage.txt```  
```pip uninstall -r removepackage.txt```  
  
seleniumのインストールとリファレンス  
https://nekoy3.net/2022/09/12/selenium-python/  
https://www.seleniumqref.com/api/webdriver_abc_python.html  
chrome 106.0.5249.119  
https://chromedriver.chromium.org/downloads  
  
discord.pyのインストールとリファレンス  
```pip install -U discord.py```  
https://discordpy.readthedocs.io/ja/latest/api.html  