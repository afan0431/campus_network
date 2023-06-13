import sys
import time

import ddddocr
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By

url = ''#引号内输入校园网登录地址
bro = webdriver.()#括号前面输入使用浏览器的名称
# 访问网站
bro.get(url)
# 隐式等待
bro.implicitly_wait(10)
# 窗口最大化
bro.maximize_window()
#去浏览器查看路径，如网站没有设立frame可跳过这一步
#定位到frame分支
frame = bro.find_element(By.XPATH, '')#引号内填入账号密码所在的frame的XPATH
# 进入分支
bro.switch_to.frame(frame)
# 输入用户名和密码
bro.find_element(By.XPATH, '').send_keys('')#前一个引号内填用户名的定位XPATH，后一个引号输入校园网账号
time.sleep(0.001)
bro.find_element(By.XPATH, '').send_keys('')#前一个引号输入密码框的定位XPATH，后一个引号输入校园网密码
time.sleep(0.001)
# 定位验证码图片
captcha = bro.find_element(By.XPATH, '')#获取验证码的XPATH填入引号内
# 全屏截图保存到本地文件夹
bro.save_screenshot('\\captcha_1.png')#在本地建立一个存放验证码截图的文件夹，双斜杠前填入文件夹地址，下面代码双斜杠前同样填入
# 定位验证码坐标
print(captcha.location)
left = captcha.location['x']
top = captcha.location['y']
right = captcha.size['width'] + left
height = captcha.size['height'] + top

img = Image.open('\\captcha_1.png')
# 抠图
frame = img.crop((left, top, right, height))
frame.save('\\captcha_2.png')
# 识别验证码
ocr = ddddocr.DdddOcr()
with open('C码\\captcha_2.png', 'rb') as f:
    image = f.read()
    res = ocr.classification(image)
print(res)
# 输入验证码
bro.find_element(By.XPATH, '').send_keys(str(res))#引号内填入验证码输入框的XPATH
time.sleep(0.001)
# 点击登录
bro.find_element(By.XPATH, '').click()#引号内填入登录按钮的XPATH
time.sleep(0.001)
# 退出网页
bro.quit()
# 关闭程序
sys.exit()