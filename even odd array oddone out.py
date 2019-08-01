#This code replaces all the chracters after excpet last 3 with #.Like in our credit cards.
def find_outlier(cc):




  countereve=0
  counterodd=0
  outliereve=0
  outlierodd=0
  for x in cc:
   if x>0:
      x=x
      if x % 2 == 0:
         countereve = countereve + 1
         outliereve = x
      else:
         counterodd = counterodd + 1
         outlierodd = x

   else:
      x=-x
      if x % 2 == 0:
         countereve = countereve + 1
         outliereve = -x
      else:
         counterodd = counterodd + 1
         outlierodd = -x

  if countereve<=1:
    print("Even")
    print(outliereve)
  else:
    print("Odd")
    print(outlierodd)


find_outlier([2, 4, 0, 100, 4, -11, 2602, 36])