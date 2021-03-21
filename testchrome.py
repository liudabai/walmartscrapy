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
    if n==43:
        pdb.set_trace()
    standardUpc=res['standardUpc'][0]   
    detail.append(brand)
    detail.append(title)
    detail.append(productPageUrl)
    detail.append(offerPrice)
    detail.append(quantity)
    detail.append(standardUpc)
    return detail

def loadhtml(driver):
    html=driver.page_source
    soup = BeautifulSoup(html,'lxml')
    ss=soup.select('pre')[0]
    res=json.loads(ss.text)
    return res

def main():
    productsUrl='https://www.walmart.com/search/api/preso?cat_id='
   # checklogin(driver)
    res=loadhtml(driver,productsUrlnow)   
    items=res['items']
    n=0
    print(n)
    for product in  items:

        detail=checkdetail(product,n)
        n=n+1
        
    print('执行完毕')