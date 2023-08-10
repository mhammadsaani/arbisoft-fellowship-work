## error vs exception


## try block contains the code which we think can cause an exception
## except block is used to catch the exception that can be produced in try block
## else block is executed when no exception is raised (will execute after try block)
## finally block will be executed whether the exception is raised or not

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")
        
        
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ZeroDivisionError:
#         print("Oops!  That was no valid number.  Try again...")


## raise vs except (one catch exception and 
## one raise exception once a certain condition is met)

# try:
#     a = int(input("Enter a number :"))
#     if a == 10:
#         raise ValueError("Invalid Input")
#     print('value is ', a)
# except ValueError as error:
#     print(error)


# class B(Exception):
#     pass

# class C(B):
#     pass

# class D(C):
#     pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")
        
        
# class B(Exception):
#     pass

# class C(B):
#     pass

# class D(C):
#     pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except B:
#         print("B")
#     except D:
#         print("D")
#     except C:
#         print("C")
    
    



# If an exception occurs during execution of the try clause, the exception 
# may be handled by an except clause. If the exception is not handled by an except 
# clause, the exception is re-raised after the finally clause has been executed.

# try: 
#     print('Hello World')
# except ValueError('Value Error') as ve:
#     print(ve)
# finally:
#     print("I will execute irrespective of exception")
    

# try: 
#     print(5 / 0)
# except ZeroDivisionError:
#     print("Zero Division Error, cannot divide with zero")
# finally:
#     print("I will execute irrespective of exception")



# try: 
#     print(5 / 0)
# except ZeroDivisionError:
#     print("Zero Division Error, cannot divide with zero")
#     raise ValueError
# finally:
#     print("I will execute irrespective of exception")

    