import datetime
import sys
from bs4 import BeautifulSoup 
from selenium import webdriver
import requests as rq
import re
import random as r
chrome_options = webdriver.ChromeOptions() 
chrome_options.add_argument('--headless') # 啟動無頭模式 
chrome_options.add_argument('--disable-gpu') # windowsd必須加入此行 
chrome = webdriver.Chrome(chrome_options=chrome_options, executable_path='C:/chromedriver.exe') 
chrome.get("http://www.thsh.tp.edu.tw/nss/s/thsh/111")
chrome.find_element_by_xpath('//*[@title="二愛"]').click()
# 06/15健康關懷填報表單(分享班級連結)
m = datetime.datetime.now().month
d = datetime.datetime.now().day
html = chrome.page_source
soup = BeautifulSoup(html, features="html.parser")
if m < 10: m = '0' + str(m)
if d < 10: d = '0' + str(d)
print('%s/%s健康關懷填報表單(分享班級連結)'%(m, d))
url = chrome.execute_script(" return document.getElementsByClassName('m-l m-r noticespan')[0].href")
print(url)
response = rq.get(url)
print(response.json)
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())  #輸出排版後的HTML內容
fields = soup.find_all('script', {'type': 'text/javascript'})
form_info = fields[1]
# print(form_info)
match = re.findall('(?<=\[\[)(\d+)', str(form_info)) 
print(match)
results = [x for x in match[1:len(match)-1:1]] # Skip the first item, which is 831400739
def press_entry(results):
    r = []
    for res in results:
        r.append("entry." + res)
    return r
    pass
results = press_entry(results)


post_url = soup.find('form', attrs={'id': 'mG61Hd'})
u = post_url['action']
for res in results:
    print(res)


fbzx = soup.find('input', {'name':'fbzx'})['value']
print(fbzx)

fvv = soup.find('input', {'name':'fvv'})['value']
payload = {
    # 第一頁
    results[0]:'二誠',
    results[1]:'26',
    results[2]:'李胤緯',
    results[3]:str(r.randint(360, 370) / 10),
    results[4]:'無（跳答下階段）',
    # 第二頁
    results[5]:'',
    # 第三頁
    results[6]:'__other_option__',
    results[6]+".other_option_response":'無( 如有請點選下方"其他"並填入"被通知日期與時間")',
    results[7]:'__other_option__',
    results[7]+".other_option_response":'無( 如有請點選下方"其他"，填寫"與學生關係"及"被通知日期與時間"兩項)',
    results[8]:'__other_option__',
    results[8]+".other_option_response":'無( 如有請點選下方"其他"並填入"被通知日期與時間")',
    results[9]:'__other_option__',
    results[9]+".other_option_response":'無(如有請點選下方"其他"，填寫"與學生關係"及"被通知日期與時間"兩項)',
    results[10]:'__other_option__',
    results[10]+".other_option_response":'無( 如有請點選下方"其他"並填入"被通知日期與時間")',
    results[11]:'__other_option__',
    results[11]+".other_option_response":'無( 如有請點選下方"其他"，填寫"與學生關係"及"被通知日期與時間"兩項)',
    'draftResponse':'[]',
    'fvv':fvv,
    'pageHistory': '0,2',
    'fbzx':fbzx,
}
#  ( 如有請點選下方"其他"並填入"被通知日期與時間")
print(payload)
res = rq.post(u, payload)
res.raise_for_status()
print(res.status_code)
chrome.quit()
sys.exit()
