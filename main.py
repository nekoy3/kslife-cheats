# coding: utf-8
from getpass import getpass

from bot import MyClient
from cfg_rw import ConfigClass

configs = ConfigClass().read_config()
if configs['login']['password'] == 'terminal':
    configs['login']['password'] = getpass('パスワードを入力・・・: ')

client = MyClient(configs['discord']['user_id'])
