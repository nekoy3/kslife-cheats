#https://github.com/nekoy3/raspi-nfc-botより
import configparser
import os

class ConfigClass(configparser.ConfigParser()):
    def create_config(self):
        self.read('config.ini', encoding="utf-8_sig")

        self.add_section('login')
        self.set('login', '# K\'s lifeのメールアドレスを入力')
        self.set('login', 'mail', 'xxx@st.kyusan-u.ac.jp')
        self.set('login', '# K\'s lifeのパスワードを入力(値をterminalにすることでコンソール上から入力することが出来る。）')
        self.set('login', 'password', 'xxx')

        self.add_section('discord')
        self.set('discord', '# botのトークンを設定する')
        self.set('discord', 'token', 'xxx')
        self.set('discord', '# discord->ユーザ設定->マイアカウント->自分の名前の横にある「・・・」をクリック')
        self.set('discord', '# IDをコピーすることで、ユーザIDを取得できるのでそれを設定')
        self.set('discord', 'user_id', 0)

        with open('config.ini', 'w') as configfile:
            self.write(configfile)

    def read_config(self):
        try:
            cfg = self.read('config.ini', encoding="utf-8_sig")

            self.mail = str(cfg['login']['mail'])
            self.password = str(cfg['login']['password'])
            self.token = str(cfg['discord']['token'])
            self.user_id = int(cfg['discord']['user_id'])
        
            if self.mail == 'xxx@st.kyusan-u.ac.jp' or self.password == 'xxx' or self.token == 'xxx' or self.user_id == 0:
                raise ValueError("いずれかの値が初期値になっているので修正してください。")

        except Exception as e:
            print("config.iniが存在しないか、設定が間違っています。\n" + str(e))
            #ファイルの存在確認(カレントディレクトリにconfig.iniがあるか)
            if not os.path.isfile('config.ini'):
                self.create_config()
            exit()
        else:
            return self.cfg