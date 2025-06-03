# try-except-finally example in Python 
#-------------------------------------------

#try and except block to handle exceptions
try:
    print(x)
except NameError:
    print("Variable 'x' is not defined.")
except:
    print("An unexpected error occurred.")


# try-except-else block to handle exceptions
try:
    print("Hello, World!")
except:
    print("An error occurred while printing.")
else:
    print("No errors occurred during the print operation.") 


# try-except-finally block to handle exceptions
try:
    print(x)
except:
    print("Variable 'x' is not defined.")
finally:
    print("This block always executes, regardless of an error.")


#try-except-finally with file operations
try:
    f = open("non_existent_file.txt", "w")
    try:
        f.write("Hello, World!")
    except:
        print("An error occurred while writing to the file.")
    finally:
        f.close()
        print("File closed successfully.")
except FileNotFoundError:
    print("File not found. Please check the file path.")

