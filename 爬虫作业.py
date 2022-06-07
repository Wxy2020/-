#-*-coding:utf-8 -*-
from __future__ import division
from cgitb import html
from turtle import position, title
import requests
from lxml import etree
import time
from html.parser import HTMLParser

requests.packages.urllib3.disable_warnings()

def getnew_title(wfjm):
    divs = wfjm.xpath('//*[@id="main"]/div/div[2]/div')#拿到每一条新闻
    for div in divs:
        title = div.xpath("./ul/li/a/text()")
        data = div.xpath("./ul/li/a/span/text()")
        for x,y in zip(title,data):
            print(x+"\n"+y)
'''
        #print(title)
        for i in title:
                with open("NEWS.txt",'r+',encoding="GBK") as f:
                    f.write(str(i))
                    f.write('\n')
                print(i)
                continue
        #print(data)
        for u in data:
                with open("NEWS.txt",'r+',encoding="GBK") as f:
                    f.write(str(i))
                    f.write('\n')
                print(u)
                continue
        continue
'''

def getnew_bodyurl(html):
    divs = html.xpath('//*[@id="main"]/div/div[2]/div')#拿到每一条新闻
    for div in divs:
        bodyurl = div.xpath("./ul/li/a//@href")#拿到新闻内容的url后部
        return bodyurl

def get_url2(head,bodyurl):#拿到新闻所在网页url
    for i in bodyurl:
        url2 = "https://www.qfnu.edu.cn/" + str(i)
        resp2 = requests.get(url2, verify=False, headers = head)
        resp2.encoding = 'UTF-8'
        wfjm2 = etree.HTML(resp2.text)
        divs = wfjm2.xpath('/html/body/div[3]/div/div[2]')
        for div in divs:
            body = div.xpath('./div/div/form/div[2]/div/div/p[position()>last()-2]/span/text()')
            '''for index in range(len(divs)):
                if (index % 2) == 0:
                    print(body[index].text) '''
            for i in body:
                '''with open("NEWS.txt",'a+',encoding="UTF-32") as f:
                    f.write(i)
                    f.write('\n')'''
                print(i)
            

def main():
    for i in range (1,298):
        BASE_url = "https://www.qfnu.edu.cn/xxyw/"+ str(i)+".htm"
        head = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"}
        resp = requests.get(BASE_url,verify=False,headers = head)
        resp.encoding = 'UTF-8'
        wfjm = etree.HTML(resp.text)
        getnew_title(wfjm)
        url = getnew_bodyurl(wfjm)
        time.sleep(1)
        get_url2(head,url)
main()