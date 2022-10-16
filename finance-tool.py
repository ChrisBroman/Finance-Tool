from functions import *

def main():
    check_file()
    while True:
        print("\nEnter an option:\n")
        print("1. Update file with CSV")
        print("2. Analyse Data")
        print('3. Exit')
        print()
        selection = input(">> ")
        print()
        if selection == "1":
            update_file()
        elif selection == "2":
            analyse_file()
        elif selection == '3':
            sys.exit(0)
        

main()