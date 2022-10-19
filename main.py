# coding: utf-8
from selenium import webdriver
from getpass import getpass

import cfg_rw
import bot

configs = cfg_rw.main()
if configs['login']['pass'] == 'xxx':
    configs['login']['pass'] = getpass('パスワードを入力・・・: ')

client = bot.MyClient(intents=mybot.intents)

chrome = webdriver.Chrome(executable_path='./driver/chromedriver.exe')
chrome.get("https://www.nttdocomo.co.jp/mydocomo/")