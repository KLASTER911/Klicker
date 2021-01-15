from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.common.action_chains import ActionChains
import time
browser = webdriver.Firefox()
browser.get("http://smmok14.ru/") #переход на сайт
browser.maximize_window() #открытие окна на весь экран
def auth():
    browser.find_element_by_xpath("//*[@x-ulogin-button='vkontakte']").click() #клик по кнопке входа через ВК
    for handle in browser.window_handles:
        browser.switch_to_window(handle) #переход на 2 страницу браузера
    time.sleep(3)
    try:
        login = browser.find_element_by_xpath("//*[@name='email']") #находит поле мыла/телефона 
    except:
        time.sleep(3)
        login = browser.find_element_by_xpath("//*[@name='email']") #находит поле мыла/телефона
    login.send_keys(",,,") #вводит мыло/телефон
    pswd = browser.find_element_by_xpath("//*[@name='pass']") #находит поле пароля
    pswd.send_keys(",,,") #вводит пароль
    browser.find_element_by_xpath("//*[@id='install_allow']").click() #подтверждение №1
    try:
       a = browser.find_element_by_xpath("//*[@id='install_allo']").click() #подтверждение №2
    except:
        print("Авторизация успешна")
    for handle in browser.window_handles:
        browser.switch_to_window(handle) #переход на начальную страницу браузера
    time.sleep(3)
    browser.find_element_by_xpath("//*[@href='http://smmok14.ru/offer/index']").click() #переходит по адресу заданий 
    time.sleep(2)
    browser.find_element_by_xpath("//*[@role='button']").click() # Click "OK"
    b = browser.find_element_by_xpath("//*[@id='user_balance']").text
    print("+++++++++++++++")
    print("Баланс = " + b)
    print("+++++++++++++++")

def ogg():
    while True:
        try:
            text_box = browser.find_element_by_xpath("//*[@class='line']").text
            if text_box == "Извините, в данную минуту у нас нет для Вас заданий":
                print("Заданий нет,переход в режим ожидания")
                time.sleep(1000)
                browser.find_element_by_xpath("//*[@class='active offert']").click()
            else:
                print("--")
        except:
           rab()

def rab():
    name = browser.find_element_by_xpath("//*[@class='project_name']").text
    if name == "Подписка":
        try:
            podp()
            close()
        except:
            udalenie()
    elif name == "Лайк + рассказать друзьям":
        udal_iz_spiska()
    elif name == "Добавить в друзья":
        try:
            drug()
            close()
        except:
            udalenie()
    elif name == "Мне нравится":
        try:
            like()
            close()
        except:
            udalenie()
    else:
       print("Таких вариантов нет...")
       browser.find_element_by_xpath("//*[@class='active offert']").click()
       time.sleep(2)


def udalenie():
    browser.close()
    for handle in browser.window_handles:
        browser.switch_to_window(handle)
    time.sleep(2)
    browser.find_element_by_xpath("//*[@class='ui-icon ui-icon-closethick']").click()
    browser.find_element_by_xpath("//*[@original-title='Больше не показывать']").click()
    print("**Задание удалено**")
def udal_iz_spiska():
    browser.find_element_by_xpath("//*[@original-title='Больше не показывать']").click()
    print("**Очищена позиция Лайк+Репост**")
    browser.find_element_by_xpath("//*[@class='active offert']").click()
    time.sleep(2)
    browser.find_element_by_xpath("//*[@role='button']").click() # Click "OK"

def close():
    time.sleep(6)
    browser.close()
    for handle in browser.window_handles:
        browser.switch_to_window(handle)
    browser.find_element_by_xpath("//*[@class='ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only']").click()
    time.sleep(6)
    browser.find_element_by_xpath("//*[@role='button']").click()
    b = browser.find_element_by_xpath("//*[@id='user_balance']").text
    print("+++++++++++++++")
    print("Баланс = " + b)
    print("+++++++++++++++")

def like():
    print("== Лайк ==")
    browser.find_element_by_xpath("//*[@class='button projectDetails']").click()
    time.sleep(1) 
    browser.find_element_by_xpath("//div[@class='ui-dialog-buttonset']").click() # переход
    time.sleep(2)
    for handle in browser.window_handles:
        browser.switch_to_window(handle)
    time.sleep(4)
    try:
        browser.find_element_by_xpath("//*[@class='flat_button button_wide']").click()
    except:
        browser.find_element_by_xpath("//*[@id='pv_like_link']").click()
def podp():
    print("== Подписка ==")
    browser.find_element_by_xpath("//*[@class='button projectDetails']").click()
    time.sleep(3) 
    browser.find_element_by_xpath("//div[@class='ui-dialog-buttonset']").click() # Подтверждение
    for handle in browser.window_handles:
        browser.switch_to_window(handle)
    time.sleep(4)
    try:
        browser.find_element_by_xpath("//*[@class='flat_button button_big button_wide']").click()
    except:
        browser.find_element_by_xpath("//*[@id='subscribe_button']").click()

def rep():
    print("Репост")
    browser.find_element_by_xpath("//*[@class='button projectDetails']").click()
    time.sleep(3) 
    browser.find_element_by_xpath("//div[@class='ui-dialog-buttonset']").click() # Подтверждение
    for handle in browser.window_handles:
        browser.switch_to_window(handle)
    time.sleep(4)
    try:
        browser.find_element_by_xpath("//*[@class='clear_fix flat_button']").click()
        browser.find_element_by_xpath("//*[@class='wl_post_action_link fl_l ']").click()
        browser.find_element_by_xpath("//*[@id='like_share_send']").click()
    except:
        browser.find_element_by_xpath("//*[@class='fw_like_icon  fl_l']").click()
        browser.find_element_by_xpath("//*[@class='reply_link']").click()
        browser.find_element_by_xpath("//*[@class='flat_button dark_box_btn fl_l']").click()

def drug():
    print("== Добавление в друзья ==")
    browser.find_element_by_xpath("//*[@class='button projectDetails']").click()
    time.sleep(3) 
    browser.find_element_by_xpath("//div[@class='ui-dialog-buttonset']").click() # Подтверждение
    for handle in browser.window_handles:
        browser.switch_to_window(handle)
    time.sleep(4)
    browser.find_element_by_xpath("//*[@class='flat_button button_wide']").click()












def login():
    print("xx")
def password():
    print("xx")

B = auth()
A = ogg()
