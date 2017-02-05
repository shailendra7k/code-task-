a= ["hello","world","i","am","here"] 
print  "\n \t\t","hello world i am here ""\n\n"

a[0]
if a[0]=="hello":
 if a[1]=="world":
  if a[2]=="i":
   z=raw_input("enter ur name for  replace  your 'i' bye your name  :-         ")
   a[2]=z
   if a[3]=="am":
    a[3]="is"
    print "\n\t\t", a[0],a[1],a[2],a[3],a[4]
   else :
    print "a3 error"
  else :
   print "a2"
 else :
   print "a1"
else :
 print "fi"
