#Calculator using Python ---- Try & Retry
print(" Calculator :- choose - 1.Addition 2.Substraction 3. Multiplication 4.Division :" )
choice = int(input("Enter Your Choice : "))
num1 = float(input("Enter First Number :"))
num2 = float(input("Enter Second Number :"))

if choice == 1:
    print("Sum = ",num1+num2)
elif choice == 2:
    print("Result = ",num1-num2)
elif choice == 3:
    print("Result = ",num1*num2)
elif choice == 4:
    print("Result = ",num1//num2)
else:
    print("Your choice is Incorrect, please try again ")
     

