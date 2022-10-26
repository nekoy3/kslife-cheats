from selenium import webdriver
import traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert

class BrowserClass:
    def __init__(self, mail, password):
        self.mail = mail
        self.password = password
    
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
    
    #全てのウィンドウを閉じてドライバを終了する
    def exit_chrome(self):
        self.chrome.quit()

    def sent_message(self, msg):
        #bot稼働時に代わりにdiscordで送信するように実装する
        print(msg)

    #ログイン処理等をこなしてトップ画面まで遷移する
    def kslife_access(self):
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
            self.chrome.find_element(By.ID, "userNameInput").send_keys(self.mail)
            self.chrome.find_element(By.ID, "passwordInput").send_keys(self.password)
            self.chrome.find_element(By.ID, "submitButton").click()
        except: 
            self.sent_message("ログイン画面に到達できませんでした。時間を空けて再度お試しください。")
            raise Exception("ログイン画面到達不可")
    
        self.password = None 
    
        #サインインボタンを押した後ホーム画面に遷移するまでの処理
        try:
            self.chrome.find_element(By.ID, "errorText")
        except: #find_elementに失敗したら正常
            try: #K's life画面のid=homeがあれば正常遷移
                self.chrome.find_element(By.ID, "home")
            except:
                self.sent_message("ログイン成功後、ホーム画面にたどり着けませんでした。メンテナンス等の原因が考えられるため、手動で確認してください。\n" + traceback.format_exc())
                raise Exception("ホーム画面到達不可")
            else:
                self.sent_message("正常にホーム画面に遷移しました。")
        else:
            self.sent_message("ログインに失敗しました。IDかパスワードを間違えている可能性があります。config.iniを確認して再度お試しください。")
            raise Exception("ログイン失敗")
    
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
    
    #ログアウトボタンを押してウィンドウを閉じる
    def logout_kslife_and_close_window(self):
        self.chrome.find_element(By.XPATH, "//*[@id=\"header-navi\"]/p/a[2]").click()
        #ダイアログが表示されるのでOKボタンを押す
        Alert(self.chrome).accept()
        self.chrome.close()

    #アクセスできるかを確認する
    async def testing_access(self, channel):
        try:
            self.kslife_access()
        except Exception as e:
            error_msg = str(e) + "\nテストアクセスに失敗したためbotを停止しました。"
            await channel.send(content=error_msg)
            self.exit_chrome()
            exit()
        else:
            self.logout_kslife_and_close_window()