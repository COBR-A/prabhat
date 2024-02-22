from feb21 import lst_find, fibb, sb
a = 'yes'
while a=='yes':
    print("""
    1. Find minimum and maximum from a list
    2. Print Fibonacci series
    3. Calculate sum of cubes \n""")
    
    choice = input("Enter your choice: \n")

    if choice == '1':
        min_val, max_val = lst_find()
       
    elif choice == '2':
        num = int(input("Enter a number: \n"))
        fibb(num)

    elif choice == '3':
        num = int(input("Enter a number: \n"))
        result = sb(num)
        print("Sum of cubes of positive integers smaller than", num, "is:", result)

    else:
        print("Invalid choice! Please enter a number between 1 and 4.\n")
    a=input("yes to continue and no fo exit again.\n")

