# coding: utf-8
#https://github.com/nekoy3/raspi-nfc-botより
import configparser
import traceback
import os

class ConfigClass():
    cfg = configparser.ConfigParser(comment_prefixes='#', allow_no_value=True)
    def create_config(self):
        self.cfg.read('config.ini', encoding="utf-8")

        self.cfg.add_section('login')
        self.cfg.set('login', '# K\'s lifeのメールアドレスを入力')
        self.cfg.set('login', 'mail', 'xxx@st.kyusan-u.ac.jp')
        self.cfg.set('login', '# K\'s lifeのパスワードを入力(値をterminalにすることでコンソール上から入力することが出来る。）')
        self.cfg.set('login', 'password', 'xxx')

        self.cfg.add_section('discord')
        self.cfg.set('discord', '# botのトークンを設定する')
        self.cfg.set('discord', 'token', 'xxx')
        self.cfg.set('discord', '# discord->ユーザ設定->マイアカウント->自分の名前の横にある「・・・」をクリック')
        self.cfg.set('discord', '# IDをコピーすることで、ユーザIDを取得できるのでそれを設定')
        self.cfg.set('discord', 'user_id', 0)

        with open('config.ini', 'w') as configfile:
            self.cfg.write(configfile)

    def read_config(self):
        try:
            self.cfg.read('config.ini')

            self.mail = self.cfg['login']['mail']
            self.password = self.cfg['login']['password']
            self.token = self.cfg['discord']['token']
            self.user_id = int(self.cfg['discord']['user_id'])
        
            if self.mail == 'xxx@st.kyusan-u.ac.jp' or self.password == 'xxx' or self.token == 'xxx' or self.user_id == 0:
                raise ValueError("いずれかの値が初期値になっているので修正してください。")
                
        except Exception as e:
            print("config.iniが存在しないか、設定が間違っています。\n" + traceback.format_exc())
            #ファイルの存在確認(カレントディレクトリにconfig.iniがあるか)
            if not os.path.isfile('config.ini'):
                self.create_config()
            exit()
        else:
            return self.cfg