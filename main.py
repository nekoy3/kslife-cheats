# coding: utf-8
from selenium import webdriver
from getpass import getpass

from cfg_rw import ConfigClass
import bot

configs = ConfigClass().read_config()
#長時間稼働するプログラムなので一度使用したらメモリからも削除する
if configs['login']['password'] == 'terminal':
    configs['login']['password'] = getpass('パスワードを入力・・・: ')

#client = bot.MyClient()

#chrome = webdriver.Chrome(executable_path='./driver/chromedriver.exe')
#chrome.get("https://www.nttdocomo.co.jp/mydocomo/")