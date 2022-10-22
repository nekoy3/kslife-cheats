# coding: utf-8
from selenium import webdriver
from getpass import getpass

import cfg_rw
import bot

configs = cfg_rw.main()
#長時間稼働するプログラムなので一度使用したらメモリからも削除する
if configs['login']['pass'] == 'xxx':
    configs['login']['pass'] = getpass('パスワードを入力・・・: ')

client = bot.MyClient()

chrome = webdriver.Chrome(executable_path='./driver/chromedriver.exe')
chrome.get("https://www.nttdocomo.co.jp/mydocomo/")