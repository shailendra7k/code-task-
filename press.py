#!/usr/bin/python


print"\n         press 1 for check current date and time" 

print"\n         press 2 for access calculator          "

print"\n         press 3 for access firefox             "

print"\n         press 4 for check ip address           " 

print"\n         press 5 for shutdown your computer     "

a=input("\n\n\t     PRESS A  NUMBER :-  " )



if a==1:

 import os
 a="date"
 x=os.system(a)
 print ""

elif a==2 :
  import os
  a="bc"
  x=os.system(a)
  print ""
 
elif a==3:
  import os 
  a="firefox"
  x=os.system(a)
  print ""

elif a==4:
  import os 
  a="ifconfig"
  x=os.system(a)
  print ""

elif a==5:
  import os 
  a="poweroff"
  x=os.system(a)
  print ""


else :

 print "enter right key "




