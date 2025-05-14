# Add the project root directory to sys.path
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


# Task 2, 5, 9: Import modules here


# Task 2, 6, 10, 18: Redefine the main() function
def main():
    pass

if __name__ == "__main__":
    main()
    print("Welcome to the Airline Database Program!")
    print("Please Select an Option: ")
    print("1 - Login ")
    print("2 - Register ")
    print("3 - Exit ")
    choice = None
    while choice != '3':
        choice = input("Make your selection now: ")
        if choice == '1':
            print("Temporary Login")
        elif choice == '2':
            print("Temporary register")
        elif choice == '3':
            print("Goodbye, and thank you for using the Airline Database Program!")
        else:
            print(choice, "is not an option, please select options 1, 2, or 3.")
    
    