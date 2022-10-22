class TestClass():
    string = 'default super_method'
    #関数アノテーション　返す値の型をコメントしておける（が無視することが出来るので注意）
    def super_method(self) -> None:
        print(self.string)
    
    def super_my_method(sekf) -> None:
        print('self?')

class SubClass(TestClass):
    def run_super_my_method(self):
        self.super_my_method()


sushi = SubClass()

sushi.run_super_my_method()
sushi.super_method()