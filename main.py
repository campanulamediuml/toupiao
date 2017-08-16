#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
# from pyvirtualdisplay import Display
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
    ident_list = ['350204196612272028\n', '320624196012261028\n', '350204195012243026\n', '350204192901073027\n', '350204193808163030\n', '350204194403133014\n', '350204194611073028\n', '350204193502023043\n', '350204193608253015\n', '350204193910210016\n', '350204193912283016\n', '350204195604062018\n', '350204195310052076\n', '350204193311253049\n', '350203192911181025\n', '350204193609073024\n', '350204194004111029\n', '350204193807073017\n', '305204193611101012\n', '350204194812093017\n', '350204193202103017\n', '350204193911273027\n', '350204193612043010\n', '350204193311073013\n', '350204194605050014\n', '350204194311283015\n', '350204193501213021\n', '350204194310102032\n', '350204194504013011\n', '350204195609083037\n', '350204195411013025\n', '350204195011200032\n', '35020419611101002X\n', '350204195208163095\n', '350204198809283045\n', '350102195404150517\n', '350204195311043016\n', '35020419830129304X\n', '350203196503291020\n', '350204197103313025\n', '350204196501193028\n', '350202194010090014\n', '350202194011040027\n', '350203199102103037\n', '350204193812031057\n', '350204194407234015\n', '35020419450604302x\n', '350203195309232014\n', '350203196002260023\n', '350204195111180040\n', '350204193408120023\n', '320623197907040021\n', '350420195103080083\n', '350204194903243017\n', '350204193709093014\n', '350221197711162511\n', '350203194702260017\n', '379009197309095724\n', '350204194610211011\n', '350202194810060032\n', '350204194311281036\n', '352601194208141013\n', '350204199206062045\n', '350204199410193026\n', '350204195411200031\n', '350204196008134024\n', '350203196610152026\n']

    for ident in ident_list:
        main(ident)
    # pool = ThreadPool(10)
    # pool.map(main,ident_list)
    # pool.close()

while 1:
    # display = Display(visible=0, size=(1920, 1080))
    # display.start()
    auto()
    # display.stop()

# print open('ident.txt').readlines()

  
    
