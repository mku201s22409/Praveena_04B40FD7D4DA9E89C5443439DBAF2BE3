# 1.1 Implement a recursive function to calculate the factorial of a given number  




def fact_rec(n) :
  #factorial calculate of using recursive function
def fact(n):
   if(n==0 or n==1):
     return 1
   else:
     return n*fact(n-1)

n=int(input("enter the number:"))
res=fact(n)
print("find the result will be factorial number is:",(res))