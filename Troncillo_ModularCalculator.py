Num_1 = float(input("Enter your first number"))
Num_2 = float(input("Enter your second number"))

Sum = Num_1 + Num_2
Difference = Num_1 - Num_2
Product = Num_1 * Num_2
Division = Num_1/Num_2

Operation = int(input("Choose an operation"))

if Operation == 1:
    print("You have selected Addition")
    print(f"Your sum is equal to {Sum}")

elif Operation == 2:
    print("You have selected Subtraction")
    print(f"Your difference is equal to {Difference}")

elif Operation == 3:
    print("You have selected Multiplication")
    print(f"Your product is equal to {Product}")

elif Operation == 4:
    print("You have selected Division")
    if Num_2 != 0:
        Quotient = Num_1/Num_2
        print(f"Your quotient is equal to {Quotient}")
    else:
        print("sorry you cannot divide by zero")

else:
    print("That is not a valid operation.")


    

    
