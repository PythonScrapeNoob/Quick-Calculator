choice = input("Choose between M,D,A,S")
num1 = int(input("Please input first number "))
num2 = int(input("please input 2nd number "))

car = 0

def calc():
    num3 = 0
    if choice == "M":
         num3 = num1 * num2
    elif choice == "D":
         num3 = num1/num2
    elif choice == "A":
         num3 = num1 + num2 
    elif choice == "S": 
         num3 = num1 - num2
    else: 
        print("Something is wrong with your inputs maybe number...")
    print(num3)
 

calc()
