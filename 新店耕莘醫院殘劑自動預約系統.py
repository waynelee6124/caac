import muggle_ocr 
from selenium import webdriver 
import numpy as np 
from webdriver_manager.chrome import ChromeDriverManager 
import cv2, time, datetime 
print("請輸入要搶的時間點(每台電腦的時間不一樣，建議參考 https://time.artjoey.com/taiwan.htm”的時間差並斟酌輸入)：") 
h = int(input("時(24小時制)：")) 
m = int(input("分：")) 
s = int(input("秒：")) 
options = webdriver.ChromeOptions() 
options.add_argument("-incognito") # 啟動無頭模式 
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options = options)
while True: 
    if datetime.datetime.now().hour >= h and datetime.datetime.now().minute >= m and datetime.datetime.now().second >= s: 
        print("starting！") 
        t = time.time() 
        driver.get("https://webreg.cth.org.tw/Covid19VaccineResidue/") 
        script = """ 
        var L0= document.getElementsByClassName("tdfrist"); 
        var L1=[NaN,NaN,NaN,NaN]; 
        var L2=[NaN,NaN];
        var k = 0; 
        var t = 0 
        for(var i=0;i<L0.length;i++){ 
        if(L0[i].innerHTML!= "證件類別："&&L0[i].innerHTML!= "生日："){ L1[k]=L0[i];console.log(L0[i]) 
        k ++; 
        }else{ 
        L2[t]=L0[i]; 
        t ++; 
        } 
        } 
        var L = [ 
        document.getElementsByTagName("input")[3], 
        document.getElementsByTagName("input")[4], 
        document.getElementsByTagName("input")[6], 
        document.getElementsByTagName("input")[7], 
        ] 
        window.scrollTo(0,document.body.scrollHeight); 
        for(var i=0;i<L1.length-1;i++){ 
        if( L1[i].innerHTML == "姓名：") 
        L[i].value=("name"); 
        if( L1[i].innerHTML == "性別：") 
        L[i].click() 
        if( L1[i].innerHTML == "證件字號：") 
        L[i].value=("Y012345678"); 
        if (L1[i].innerHTML == "聯絡電話：") 
        L[i].value=(“0969123456”); 
        } 
        L = document.getElementsByTagName("select"); 
        var id = "身分證"; 
        var year =41; 
        var month = 12; 
        var day = 27; 
        if(L2[0].innerHTML=="生日："){ 
        L[0].value=year; 
        L[1].value=month; 
        L[2].value=day; 
        L[3].value=id; 
        } 
        else{ 
        L[0].value=id; 
        L[1].value=year; 
        L[2].value=month; 
        L[3].value=day; 
        }
        """ 
        driver.execute_script(script) 
        # 驗證碼 
        driver.save_screenshot("screenshot359A.png") 
        img = cv2.imread("screenshot359A.png") 
        # img = cv2.imread("screenshot2.png") 
        # x 200 360 
        # y 286 336 
        # 裁切區域的 x 與 y 座標（左上角） 
        x = 200 
        y = 286 
        # 裁切區域的長度與寬度 
        w = 360-200 
        h = 336-286 
        # 裁切圖片 
        crop_img = img[y:y+h, x:x+w] 
        # cv2.imshow("num", crop_img) 
        cv2.imwrite("num.png", crop_img) 
        # driver.get("https://webreg.cth.org.tw/Covid19VaccineResidue/") 
        # # 初始化；model_type 包含了 ModelType.OCR/ModelType.Captcha 两种 # sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.OCR) # # ModelType.OCR 可识别光学印刷文本 这里个人觉得应该是官方文档写错 了 官方文档是ModelType.Captcha 可识别光学印刷文本 
        # with open(r"num.png", "rb") as f: 
        # b = f.read() 
        # text = sdk.predict(image_bytes=b) 
        # print(text) 
        # ModelType.Captcha 可识别4-6位验证码 
        sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha) 
        with open(r"num.png", "rb") as f: 
            b = f.read() 
        text2 = sdk.predict(image_bytes=b) 
        print(text2) 
        # ———————————————— 
        # 版权声明：本文为CSDN博主「mopaoroutang」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。 
        # 原文链接：https://blog.csdn.net/mopaoroutang/article/details/115006922 
        driver.find_elements_by_tag_name("input")[8].send_keys(text2.upper()[0:4]) #
        f = open("v.html", "w", encoding="utf-8") 
        f.write(driver.page_source) 
        f.close() 
        # driver.execute_script(""" 
        # document.getElementsByTagName("input")[8].value = "%s"; 
        # document.getElementsByTagName("input")[9].click(); 
        # """%(text2[0:4].upper())) 
        driver.find_elements_by_tag_name("input")[9].click(); 
        print(time.time()-t) 
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") 
        driver.save_screenshot("end359.png") 
        break 
    print("not yet", end = "\r")
