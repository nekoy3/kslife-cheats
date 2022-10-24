# coding: utf-8
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.by import By
import time

from cfg_rw import ConfigClass
import bot

def main():
    configs = ConfigClass().read_config()
    #長時間稼働するプログラムなので一度使用したらメモリからも削除する
    if configs['login']['password'] == 'terminal':
        configs['login']['password'] = getpass('パスワードを入力・・・: ')

    #webdriver読み込み
    chrome = webdriver.Chrome(executable_path='./driver/chromedriver.exe')

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
    chrome.find_element(By.LINK_TEXT, "サインイン").click()

    time.sleep(3)

if __name__ == '__main__':
    main()