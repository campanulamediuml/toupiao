#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from pyvirtualdisplay import Display
from selenium import webdriver
import os

# fire_fox_driver = '/usr/bin'
# os.environ["webdriver.ie.driver"] = fire_fox_driver

def good_artical(ident):
    
    driver = webdriver.Chrome()#这里使用Firefox浏览
    driver.get('http://www.dyejia.cn/ca/2017080401000116.htm')
    good_artical = driver.find_element_by_xpath('//*[@id="data_row4"]/div/ul/li[1]/a/div')
    ActionChains(driver).click(good_artical).perform()
    time.sleep(3)
    for i in [4,14,20,21,23,25,26,44]:
        vote = driver.find_element_by_xpath('//*[@id="data_vote_list"]/div[1]/ul/li['+str(i)+']/div/div[2]/div[1]/div/label')
        driver.execute_script('arguments[0].scrollIntoView();',vote)
        time.sleep(1)
        ActionChains(driver).move_to_element(vote).click(vote).perform()
    commitment = driver.find_element_by_xpath('//*[@id="vote_bt"]')
    ActionChains(driver).click(commitment).perform()
    driver.find_element_by_xpath('//*[@id="alert3"]/div[2]/div/div[1]/input').send_keys(ident)
    commitment = driver.find_element_by_xpath('//*[@id="alert3"]/div[2]/div/div[2]/a[1]')
    ActionChains(driver).click(commitment).perform()
    time.sleep(1)
    driver.close()

def good_parter(ident):
    
    driver = webdriver.Chrome()#这里使用Firefox浏览
    driver.get('http://www.dyejia.cn/ca/2017080401000116.htm')
    good_artical = driver.find_element_by_xpath('//*[@id="data_row4"]/div/ul/li[2]/a/div')
    ActionChains(driver).click(good_artical).perform()
    time.sleep(3)
    for i in [2,17,24,25,44]:
        vote = driver.find_element_by_xpath('//*[@id="data_vote_list"]/div[2]/ul/li['+str(i)+']/div[1]/div/div/label')
        driver.execute_script('arguments[0].scrollIntoView();',vote)
        time.sleep(1)
        ActionChains(driver).move_to_element(vote).click(vote).perform()
    commitment = driver.find_element_by_xpath('//*[@id="vote_bt"]')
    ActionChains(driver).click(commitment).perform()
    driver.find_element_by_xpath('//*[@id="alert3"]/div[2]/div/div[1]/input').send_keys(ident)
    commitment = driver.find_element_by_xpath('//*[@id="alert3"]/div[2]/div/div[2]/a[1]')
    ActionChains(driver).click(commitment).perform()
    time.sleep(1)
    driver.close()

def good_part(ident):
    
    driver = webdriver.Chrome()#这里使用Firefox浏览
    driver.get('http://www.dyejia.cn/ca/2017080401000116.htm')
    good_artical = driver.find_element_by_xpath('//*[@id="data_row4"]/div/ul/li[3]/a/div')
    ActionChains(driver).click(good_artical).perform()
    time.sleep(3)
    for i in [6,7,8,9,43]:
        vote = driver.find_element_by_xpath('//*[@id="data_vote_list"]/div[2]/ul/li['+str(i)+']/div[1]/div/div/label')
        driver.execute_script('arguments[0].scrollIntoView();',vote)
        time.sleep(1)
        ActionChains(driver).move_to_element(vote).click(vote).perform()
    commitment = driver.find_element_by_xpath('//*[@id="vote_bt"]')
    ActionChains(driver).click(commitment).perform()
    driver.find_element_by_xpath('//*[@id="alert3"]/div[2]/div/div[1]/input').send_keys(ident)
    commitment = driver.find_element_by_xpath('//*[@id="alert3"]/div[2]/div/div[2]/a[1]')
    ActionChains(driver).click(commitment).perform()
    time.sleep(1)
    driver.close()

def good_movie(ident):
    
    driver = webdriver.Chrome()#这里使用Firefox浏览
    driver.get('http://www.dyejia.cn/ca/2017080401000116.htm')
    good_artical = driver.find_element_by_xpath('//*[@id="data_row4"]/div/ul/li[4]/a/div')
    ActionChains(driver).click(good_artical).perform()
    time.sleep(3)
    for i in [5,6,7,8]:
        vote = driver.find_element_by_xpath('//*[@id="data_vote_list"]/div[1]/ul/li['+str(i)+']/div/div[2]/div[1]/div/label')
        driver.execute_script('arguments[0].scrollIntoView();',vote)
        time.sleep(1)
        ActionChains(driver).move_to_element(vote).click(vote).perform()
    commitment = driver.find_element_by_xpath('//*[@id="vote_bt"]')
    ActionChains(driver).click(commitment).perform()
    driver.find_element_by_xpath('//*[@id="alert3"]/div[2]/div/div[1]/input').send_keys(ident)
    commitment = driver.find_element_by_xpath('//*[@id="alert3"]/div[2]/div/div[2]/a[1]')
    ActionChains(driver).click(commitment).perform()
    time.sleep(1)
    driver.close()

def good_case(ident):
    
    driver = webdriver.Chrome()#这里使用Firefox浏览
    driver.get('http://www.dyejia.cn/ca/2017080401000116.htm')
    good_artical = driver.find_element_by_xpath('//*[@id="data_row4"]/div/ul/li[5]/a/div')
    ActionChains(driver).click(good_artical).perform()
    time.sleep(3)
    for i in [6,7,8,9,39]:
        vote = driver.find_element_by_xpath('//*[@id="data_vote_list"]/div[1]/ul/li['+str(i)+']/div/div[2]/div[1]/div/label')
        driver.execute_script('arguments[0].scrollIntoView();',vote)
        time.sleep(1)
        ActionChains(driver).move_to_element(vote).click(vote).perform()
    commitment = driver.find_element_by_xpath('//*[@id="vote_bt"]')
    ActionChains(driver).click(commitment).perform()
    driver.find_element_by_xpath('//*[@id="alert3"]/div[2]/div/div[1]/input').send_keys(ident)
    commitment = driver.find_element_by_xpath('//*[@id="alert3"]/div[2]/div/div[2]/a[1]')
    ActionChains(driver).click(commitment).perform()
    time.sleep(1)
    driver.close()

def good_examp(ident):
    
    driver = webdriver.Chrome()#这里使用Firefox浏览
    driver.get('http://www.dyejia.cn/ca/2017080401000116.htm')
    good_artical = driver.find_element_by_xpath('//*[@id="data_row4"]/div/ul/li[6]/a/div')
    ActionChains(driver).click(good_artical).perform()
    time.sleep(3)
    for i in [14,19,23,26,29,32]:
        vote = driver.find_element_by_xpath('//*[@id="data_vote_list"]/div[2]/ul/li['+str(i)+']/div[1]/div/div/label')
        driver.execute_script('arguments[0].scrollIntoView();',vote)
        time.sleep(1)
        ActionChains(driver).move_to_element(vote).click(vote).perform()
    commitment = driver.find_element_by_xpath('//*[@id="vote_bt"]')
    ActionChains(driver).click(commitment).perform()
    driver.find_element_by_xpath('//*[@id="alert3"]/div[2]/div/div[1]/input').send_keys(ident)
    commitment = driver.find_element_by_xpath('//*[@id="alert3"]/div[2]/div/div[2]/a[1]')
    ActionChains(driver).click(commitment).perform()
    time.sleep(1)
    driver.close()


def main(ident):
    good_artical(ident.strip())
    good_parter(ident.strip())
    good_part(ident.strip())
    good_movie(ident.strip())
    good_case(ident.strip())
    good_examp(ident.strip())


def auto():
    ident_list = open('ident.txt').readlines()
    # for ident in ident_list:
    #     try:
    #         main(ident)
    #     except Exception,e:
    #         print e
    #         continue
    pool = ThreadPool(10)
    pool.map(main,ident_list)
    pool.close()

while 1:
    try:
        display = Display(visible=0, size=(1920, 1080))
        display.start()
        auto()
        display.stop()
    except Exception,e:
        print e 
        os.system('ps -ef|grep Xvfb|grep -v grep|cut -c 9-15|xargs kill -9')
        os.system('ps -ef|grep chromedriver|grep -v grep|cut -c 9-15|xargs kill -9')
        time.sleep(3)
        continue

# print open('ident.txt').readlines()

  
    
