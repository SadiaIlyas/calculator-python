num1=int(input("enter first number"))
num2=int(input("enter second number"))
print("which operation you want to perform")
print("+\n-\n*\n%\n/ \n**\n please enter the symbol")
sym=input()
if(sym=="+"):
    sum=num1+num2
    print("the sum is:",sum)
elif(sym=="-"):
    diff=num1-num2
    print("the difference is:",diff)
elif(sym=="*"):
    product=num1**num2
    print("the product is:",product)
elif(sym=="/"):
    division=num1/num2
    print("the division of numbers is:",division)
elif(sym=="%"):
    modulus=num1%num2
    print("the module is:",modulus)
elif(sym=="**"):
    power=num1**num2
    print(f"{num1} raise to power {num2} is:",power)
else:
    print("enter a valid symbol")

