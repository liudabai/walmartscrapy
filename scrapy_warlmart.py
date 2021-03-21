import re
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import subprocess
import time
import json
import pdb
import codecs
import random
chrome_options = Options()

chrome_options.debugger_address="127.0.0.1:9222"
driver = webdriver.Chrome(options=chrome_options)
MinDenyTime=1
MaxDenyTime=2
loginUrl='https://www.walmart.com/'


page=1
cat_id='5440_202072_2243339'




nowtime=time.strftime("%Y%m%d%H%M%S", time.localtime())

oneLine=['brand','title','productPageUrl','offerPrice','quantity','standardUpc']

def open_csv(cat_id,nowtime):
    new=open(cat_id+nowtime+'.csv','w',newline='')
    w = csv.writer(new, delimiter=',', quotechar='"')
    w.writerow(oneLine)
    return w


def checklogin(driver):
    driver.get(loginUrl)
    if driver.current_url!=loginUrl:
        subprocess.call("pause",shell=True)
    return 1
    





def checkdetail(res,n):
    detail=[]
    print('第'+str(n)+'个')
    try:
        brand=res["brand"][0]
    except:
        brand='none'
    title=res["title"]

    productPageUrl=res["productPageUrl"]
    try:
        offerPrice=res["primaryOffer"]['offerPrice']
    except:
        offerPrice=res["primaryOffer"]['minPrice']
    quantity=res["quantity"]
 #   if n==34:
#        pdb.set_trace()
    try:

        standardUpc=res['standardUpc'][0]   
    except:
        try:
            standardUpc=res['upc']
        except:
            standardUpc='none'
            
    detail.append(brand)
    detail.append(title)
    detail.append(productPageUrl)
    detail.append(offerPrice)
    detail.append(quantity)
    detail.append(standardUpc)
    return detail
        
    
def loadhtml(driver,productsUrlnow):
    time.sleep(random.randint(MinDenyTime,MaxDenyTime))
    driver.get(productsUrlnow)
    html=driver.page_source
    soup = BeautifulSoup(html,'lxml')
    ss=soup.select('pre')[0]
    res=json.loads(ss.text)
    return res

def main():
    productsUrl='https://www.walmart.com/search/api/preso?cat_id='
   # checklogin(driver)
    newOpen=open_csv(cat_id,nowtime)
    print(driver.title)
    productsUrl=productsUrl+cat_id+'&prg=desktop&page='
    for i in range(1, 26):
        n=0
        productsUrlnow=productsUrl+str(i)
        print(productsUrlnow)
        print('正在执行第'+str(i)+'页')
        res=loadhtml(driver,productsUrlnow)   
        items=res['items']
        for product in  items:

            detail=checkdetail(product,n)
            newOpen.writerow(detail)
            n=n+1
        
    print('执行完毕')

if __name__=='__main__':
    #checklogin(driver)
    main()



    
    
