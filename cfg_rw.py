#https://github.com/nekoy3/raspi-nfc-botより
import configparser
import os

config = configparser.ConfigParser()

class ConfigClass:
    pass

def create_config():
    config.read('config.ini', encoding="utf-8_sig")

    config.add_section('login')
    config.set('login', '# K\'s lifeのメールアドレスを入力')
    config.set('login', 'mail', 'xxx@st.kyusan-u.ac.jp')
    config.set('login', '# K\'s lifeのパスワードを入力(xxxにすることでコンソール上から入力することが出来ます。）')
    config.set('login', 'password', 'xxx')

    config.add_section('discord')
    config.set('discord', '# discord->ユーザ設定->マイアカウント->自分の名前の横にある「・・・」をクリック')
    config.set('discord', '# IDをコピーすることで、ユーザIDを取得できるのでそれを設定')
    config.set('discord', 'user_id', 0)

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def main():
    global config
    try:
        config.read('config.ini', encoding="utf-8_sig")

        configs = ConfigClass()
        configs.mail = str(config['login']['mail'])
        configs.password = str(config['login']['password'])

    except Exception as e:
        print("config.iniが存在しないか、設定が間違っています。\n" + str(e))
        #ファイルの存在確認(カレントディレクトリにconfig.iniがあるか)
        if not os.path.isfile('config.ini'):
            create_config()
        exit()
    else:
        return configs

if __name__ == '__main__':
    main()