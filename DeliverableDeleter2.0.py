import os

path = "/sdcard/Pictures/"  # set the path to the folder where the pictures are stored

def show_files():
    print("The following files starting with 'deliverable' are present in the folder:")
    print()
    for file in os.listdir(path):
        if file.startswith("deliverable"):
            print(file)
    if not any(f.startswith("deliverable") for f in os.listdir(path)):
        print("No files starting with 'deliverable' were found.")

def delete_files():
    print()
    confirm = input("You are about to delete all images beginning with the word 'deliverable'. Do you wish to continue? Y/N: ").strip()
    if confirm.upper() == "Y":
        for file in os.listdir(path):
            if file.startswith("deliverable"):
                os.remove(path+file)
                print(f"{file} deleted.")
                print()
        print("All files starting with 'deliverable' have been deleted.")
    else:
        print()
        print("Deletion of files canceled.")

def menu():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Deliverable Deleter 2.0.1")
        print()
        print("1. Show All Deliverables")
        print("2. Delete All Deliverables")
        print("3. Exit")
        print()
        choice = input("Enter your choice: ")
        if choice == "1":
            print()
            show_files()
        elif choice == "2":
            delete_files()
        elif choice == "3":
            print()
            print("Exiting...")
            break
        else:
            print()
            print("Invalid choice. Please try again.")
        if choice == "1" or choice == "2":
            print()
            input("Press 'Enter' to continue...")

menu()
