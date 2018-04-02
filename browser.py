from selenium import webdriver
import os,time
from selenium.webdriver.common.keys import Keys


src_dir = os.getcwd()
#t=time.time()
driver = webdriver.Chrome('{}\\chromedriver.exe'.format(src_dir))
#print time.time()-t


def closeTab():
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
    driver.quit()

def newTab():
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
    driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
    windows = driver.window_handles
    time.sleep(3)
    driver.switch_to.window(windows[-1])
    driver.get('http://www.google.com/')

def browserCommands(key):
    print key
    if key == 'new tab':
        newTab()
    elif key == 'close tab':
        closeTab()

def gesture():
    pass

if __name__ == '__main__':
    browserCommands('new tab')
    time.sleep(3)
    browserCommands('new tab')
    time.sleep(3)
    browserCommands('close tab')