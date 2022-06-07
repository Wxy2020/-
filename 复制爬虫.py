#-*-coding:utf-8 -*-
import requests
from lxml import etree

def gettext_body(wfjm):
    divs = wfjm.xpath('//*[@id="article-content"]')#拿到页面全部信息
    for div in divs:
        body = div.xpath("./p/text()")
        print(body)


def main():
    BASE_url = "https://www.liuxue86.com/a/3417781.html"
    head = {'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36"}
    resp = requests.get(BASE_url,verify=False,headers = head)
    print(resp.text)
    resp.encoding = 'UTF-8'
    wfjm = etree.HTML(resp.text)
    gettext_body(wfjm)
main()