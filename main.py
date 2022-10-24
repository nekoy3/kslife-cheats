# coding: utf-8
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs
import time

from cfg_rw import ConfigClass
import bot

#ドライバーを準備するメソッド
def make_driver_process() -> webdriver.Chrome:
        #ChromeOptionsクラスのインスタンスを生成して、それにオプションを追加する
        options = webdriver.ChromeOptions()
        
        #ヘッドレスモードで起動する（バックグラウンドで実行するようになる）
        #options.add_argument("--headless")
        
        #ドライバのパスを指定
        chrome_service = fs.Service(executable_path='./driver/chromedriver.exe')

        #ドライバのパスとオプションを設定してChromeのインスタンスを生成
        chrome = webdriver.Chrome(service=chrome_service, options=options)

        #タイムアウトを五秒で設定、読み込み終わるまで待機する
        chrome.implicitly_wait(5) 

        return chrome

def main():
    configs = ConfigClass().read_config()
    #長時間稼働するプログラムなので一度使用したらメモリからも削除する
    if configs['login']['password'] == 'terminal':
        configs['login']['password'] = getpass('パスワードを入力・・・: ')

    #webdriver読み込み
    chrome = make_driver_process()

    #K's lifeログイン前画面に移動
    chrome.get("https://ksuweb.kyusan-u.ac.jp/portalv2/")

    #ログイン画面へのボタンをクリック(XPath)
    chrome.find_element(By.XPATH, '//*[@id="left_container"]/div/ul[1]/li/a').click()

    #アクティブになっているログイン前画面を閉じる
    chrome.close()

    #ログイン画面をアクティブウィンドウにする
    chrome.switch_to.window(chrome.window_handles[-1])

    chrome.find_element(By.ID, "userNameInput").send_keys(configs['login']['mail'])
    chrome.find_element(By.ID, "passwordInput").send_keys(configs['login']['password'])
    chrome.find_element(By.ID, "submitButton").click()

    time.sleep(3)

if __name__ == '__main__':
    main()