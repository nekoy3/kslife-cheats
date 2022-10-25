from selenium import webdriver
import traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

from cfg_rw import ConfigClass
import bot

class BrowserClass:
    #ドライバーを準備するメソッド
    def make_driver_process(self) -> webdriver.Chrome:
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

    def sent_message(self, msg):
        #bot稼働時に代わりにdiscordで送信するように実装する
        print(msg)

    def kslife_access(self, configs):
        #webdriver読み込み
        self.chrome = self.make_driver_process()

        #K's lifeログイン前画面に移動
        self.chrome.get("https://ksuweb.kyusan-u.ac.jp/portalv2/")

        #ログイン画面へのボタンをクリック(XPath)
        self.chrome.find_element(By.XPATH, '//*[@id="left_container"]/div/ul[1]/li/a').click()

        #ログイン画面をアクティブウィンドウにする
        self.chrome.switch_to.window(self.chrome.window_handles[-1])

        #ログイン画面で値を入力する
        try:
            self.chrome.find_element(By.ID, "userNameInput").send_keys(configs['login']['mail'])
            self.chrome.find_element(By.ID, "passwordInput").send_keys(configs['login']['password'])
            self.chrome.find_element(By.ID, "submitButton").click()
        except: 
            self.sent_message("ログイン画面に到達できませんでした。再度お試しください。")
    
        configs['login']['password'] = None 
    
        #サインインボタンを押した後ホーム画面に遷移するまでの処理
        try:
            self.chrome.find_element(By.ID, "errorText")
        except: #find_elementに失敗したら正常
            try: #K's life画面のid=homeがあれば正常遷移
                self.chrome.find_element(By.ID, "home")
            except:
                self.sent_message("ログイン成功後、ホーム画面にたどり着けませんでした。メンテナンス等の原因が考えられるため、手動で確認してください。\n" + traceback.format_exc())
                exit()
            else:
                self.sent_message("正常にホーム画面に遷移しました。")
        else:
            self.sent_message("ログインに失敗しました。IDかパスワードを間違えている可能性があります。config.iniを確認して再度お試しください。")
            exit()
    
        #ログイン前画面を閉じる
        self.chrome.switch_to.window(self.chrome.window_handles[0])
        self.chrome.close()
        self.chrome.switch_to.window(self.chrome.window_handles[-1])

    #出席登録ボタンの意
    def attendance_registration(self):
        #出席登録画面に遷移
        self.chrome.find_element(By.ID, "btnAttendance").click()
    
    #授業アンケートの意
    def class_worksheet(self):
        #メニューバーにカーソルを当てる
        actions = ActionChains(self.chrome)
        actions.move_to_element(
            self.chrome.find_element(By.CLASS_NAME, "d_menu")
        ).perform()

        #授業アンケートを開く
        self.chrome.find_element(By.XPATH, "//*[@id=\"header-menu-sub\"]/li/table/tbody/tr[2]/td[1]/a[6]").click()

    #ホーム画面に戻る
    def back_homemenu(self):
        self.chrome.find_element(By.XPATH, "//*[@id=\"header-navi\"]/h1/a").click()