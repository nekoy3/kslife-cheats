# coding: utf-8
from selenium import webdriver

chrome = webdriver.Chrome(executable_path='./driver/chromedriver.exe')
chrome.get("https://www.nttdocomo.co.jp/mydocomo/")