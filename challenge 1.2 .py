year=int(input("Enter the number:"))
if((year%400==0)or(year%100!=0)):
  print("The year is a leap year")
if(year%4==0):
  print("The year is not a leap year")
  