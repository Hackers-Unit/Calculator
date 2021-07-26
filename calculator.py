print("Hackers United Calculator")
print("Contact Us: https://hackersunited.ml")
print("Created By Teniola Ayodele")


def add(a,b):
    result=a+b
    print("First Number+Second Number= ",result)

def sub(a,b):
    result=a-b
    print("First Number-Second Number= ",result)

def mul(a,b):
    result=a*b
    print("First Number*Second Number= ",result)

def div(a,b):
    result=a/b
    print("First Number/Second Number= ",result)

a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
op=input("Enter the operator: ")

if op=="+":
    add(a,b)
elif op=="-":
    sub(a,b)
elif op=="*":
    mul(a,b)
elif op=="/":
    div(a,b)
else:
    print("Invalid Operator")
