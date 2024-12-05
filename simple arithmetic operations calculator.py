First_no = float(input("enter first number: "))
Second_no = float(input("enter second number: "))

operation = input("choose an operation(+, -, *, /): ")

if operation == "+" :
    result = First_no + Second_no
    print(f" The result is {result}")
elif operation == "-" : 
     result = First_no - Second_no
     print(f" The result is {result}")
    
elif operation == "-" : 
     result = First_no - Second_no
     print(f" The result is {result}")
     
elif operation == "/" : 
     result = First_no / Second_no
     print(f" The result is {result}")
else:
    print("invalid operation")
         

