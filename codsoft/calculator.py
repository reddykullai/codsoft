def Addition(x,y):
    return x+y

def Subtraction(x,y):
    return x-y

def Multiplication(x,y):
    return x*y

def Division(x,y):
    if y==0:
        return "Error!! Division by zero!!!"
    else:
        return x/y

def main():
    print("Simple calculator:\n")
    print("Select operation:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division")

    while True:
        choice =input("Enter your choice(1 to 4): ")
        if choice in ('1','2','3','4'):
            try:
                num1=float(input("Enter first number: "))
                num2=float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a valid number ")
                continue

            if choice =='1':
                print(f"Result of {num1}+{num2}:",Addition(num1,num2))
            elif choice =='2':
                print(f"Result of {num1}-{num2}:",Subtraction(num1,num2))
            elif choice =='3':
                print(f"Result of {num1}*{num2}:",Multiplication(num1,num2))
            elif choice =='4':
                print(f"Result of {num1}/{num2}:",Division(num1,num2))
                continue
        else:
            print("Invalid option!!")
            continue
        data = input("Would you like to perform another calculation? (yes/no): ")
        if data.lower() not in ('yes', 'y'):
            print("Exiting program.")
            break 
            
if __name__=="__main__":
    main()
