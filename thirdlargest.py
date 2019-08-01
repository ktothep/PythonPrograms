s=[1,77,44,9,100,324,999,5445]
numlargest=s[0]
numsec=s[1]
tlargest=s[3]
for i in s:
   if i>numlargest:
      tlargest=[numsec]
      numsec=numlargest
      numlargest=i
   elif  numlargest>i>numsec:
      tlargest=numsec
      numsec=i
   elif numsec>i>tlargest:
         tlargest=i


print(numlargest)
print(numsec)
print(tlargest)




