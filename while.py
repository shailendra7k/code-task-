import os 
a=4
while(a<5):

 print "\npress 1 for check date and time:  "
 print "\npress 2 for print message:  "
 print "\npress 3 for access calculator :\n "
 print "\npress 4 for exit  :\n "
 
 i=input()
 if i==1:
   os.system("date")
 elif i==2:
   c=raw_input("enter your message:-")
   print "\n\t"+ c
 elif i==3:
   os.system("bc")
 elif i==4:
   os.system("killall python")
 else :
   print "press correct key "
