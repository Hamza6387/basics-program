import math

def mainUserInput():
    while True:
        try:
            choice= int(input("please enter the input:  "))
            if choice<0:
                print("please enter the postive number: ")
                
            else:
                return choice
        except:
            print("Invalid number !please re-enter: ")
    

# Find Maximum of two numbers in Python
def max(a,b):
  if a==b:
      return f"a and b both are equal"
  elif a<b:
      return f"{ b } is greater than {a}"
  else:
      return f"{ a } is greater than {b} "
     
    
# Factorial of a Number
def factorial(n):
    result=1
    for i in range(1,n+1):
     result=result*i
    return result

# Factorial of a number 

def fact(n):
    factorial=1
    if n==0 or n==1:
        return 1
    else:
        factorial=n*fact(n-1)
        return factorial
    
def armstrong(n):
    result=0
    num=str(n)
    length =len(num)
    for i in num:
     result+=pow(int(i),length)
    print(f"converted number: {num} and  length of string is {length}")
    if result==n:     
     return "Number is an Armstrong number"
    else: 
     return "NUmber is not an Armstrong number"

def reverseNum(num):
    numReverse=0
    while num>0:
        if num==0:
            break
        else:
         lastDigit=num%10
         numReverse=(numReverse * 10)+ lastDigit
         num=num//10
    return numReverse

def simpleInterest(principal,years,rateInterest):
    Si=principal*years*rateInterest/100
    return Si

def compoundInterest(principle,rate,time):
    amount=principle*(pow((1+rate/100),time))
    ci=amount-principle
    return ci
    
def areaOfCirlce(radius):
    result=3.17*pow(radius,2)
    return result
 
def primeInterval(x,y):
    list=[]
    for num in range(x,y+1):
     if num<2:
           continue
     for j in range(2,int(num ** 0.5) + 1):
           if  num%j==0:
                 break
           
     else:
       list.append(num)
    return list        

# def fibonnaci(n):
#     a=0
#     b=1
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
    
#     else:
#         for i in range(2,n+1):
#            c=a+b
#            a=b
#            b=c
#     return c
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        c=fib(n-1)+fib(n-2)
    return c

def checkFib(n):
    a=math.sqrt(5 * pow(n,2)+4)
    b=math.sqrt(5 * pow(n,2)-4)
    if a==int(a)  or b==int(b):

        return f"{n} is a fibonacci number "
    else:
        return f"{n} is not a fibonacci number "

def ascii(ch):
  asci=ord(ch)
  return(f"The ASCII value of {ch} is {asci}")



while True:
    try:
          print("""
            1. Find Maximum of two numbers in Python
            2. find  factorial of a  number
            3. find  factorial using recursion
            4. armstrong number
            5. revrse an integer
            6. calculate s.i
            7. calculate c.i
            8. calculate area of circle
            9. primeInterval
            10.fibonnaci  nth 
            11.check number is fibonacci or not
            12.print ASCII value of  a character
            15. exit
                
          """)
          choice=int(input("Please enter the choice: "))
       
          match choice:
            case 1:
                    a=mainUserInput()
                    b=mainUserInput()
                    rsult=max(a,b)
                    print(rsult)
                
            case 2:
                  n=mainUserInput()
                  result=factorial(n)
                  print(f"Factorial  is { result}") 

            case 3:
                 n=mainUserInput()
                 res=fact(n)
                 print(f"The factorial of {n}  is {res}")
            
            case 4:
                  n=mainUserInput()
                  num=armstrong(n)
                  print(num)

            case 5:
                n=mainUserInput()
                num=reverseNum(n)
                print(num)

            case 6:
                print("Enter input for principal amount: ")
                p=mainUserInput()
                print("Enter input for period or time: ")
                y=mainUserInput()
                print("Enter input for interest rate: ")
                i=mainUserInput()
                print(f"The simpleInterest is  { simpleInterest(p,y,i) } ")

            case 7:
                print("Enter input for principal amount: ")
                p=mainUserInput()
                print("Enter input for period or time: ")
                t=mainUserInput()
                print("Enter input for interest rate: ")
                r=mainUserInput()
                print(f"The compoundInterest is  { compoundInterest(p,t,r) } ")

            case 8:

                print("Enter input for radius of cirlce: ")
                radius=mainUserInput()
                print(f"Area of circle is : {areaOfCirlce(radius)}")

            case 9:
                  x=mainUserInput()
                  y=mainUserInput()
                  print(f"Following are prime number: { primeInterval(x,y) }")

            case 10:
                  n=mainUserInput()
                  print(f"The fibonnaci of {n} is: {fib(n)} ")

            case 11:
                n=mainUserInput()
                print(checkFib(n))

            case 12:
                ch=input("PLease enter : ")
                print(ascii(ch))
                 


            case 15:
                    print("Exit")
                    break
            case _:
               print("invalid number")
    except:
     print("please enter a valid choice!")
