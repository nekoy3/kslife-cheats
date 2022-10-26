# coding: utf-8
from getpass import getpass

from bot import MyClient
from cfg_rw import ConfigClass
from kslife_access import BrowserClass

configs = ConfigClass().read_config()
if configs['login']['password'] == 'terminal':
    configs['login']['password'] = getpass('パスワードを入力・・・: ')

kslife = BrowserClass(configs['login']['mail'], configs['login']['password'])
configs['login']['password'] = None

client = MyClient(configs['discord']['user_id'], kslife)
client.run(configs['discord']['token'])