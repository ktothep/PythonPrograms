#This code replaces all the chracters after excpet last 3 with #.Like in our credit cards.
def maskify(cc):
   x=len(cc)
   for i in range(0,x-3):
      cc=cc.replace(cc[i],"#",1)
   print(cc)

maskify(input("Enter a String for masking"))