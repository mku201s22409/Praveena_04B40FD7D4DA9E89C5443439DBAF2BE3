# Write a program that determines whether a year entered by the user is a leap year or not using ifelif-else statements






def leap(year):
  if(year %4==0 and year%100!=0 or year %400==0):
    return True
  else: 
    return False

year=int(input("Enter the year :"))

if leap(year):
    print("is a leap year:",year)
else:
   print("is a not leap year:", year)