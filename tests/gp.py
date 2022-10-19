# coding: utf-8
from getpass import getpass

# 名前とパスワードの入力を受け付ける
name = input('なまえ:')
password = getpass('pass(このあと表示します): ')

print("name:" + name + " さんのpassは" + password + "です")

#https://www.lifewithpython.com/2015/05/python-get-password-from-standard-input.html