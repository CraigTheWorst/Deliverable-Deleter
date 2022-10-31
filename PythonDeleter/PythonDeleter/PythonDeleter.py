import sys
import platform
import os
from time import sleep

# variables
path = r"C:\\Users\\CRAIG\\Pictures\\myDeliverables\\"
dir_list = os.listdir(path)
dir_list.sort()

gb1 = "          Goodbye..."


# ----- functions defined here -----


def menu():
    clr_scr()
    print()
    print("     DELIVERABLE DELETER")
    print("  --------------------------")
    print()
    print("   [1] Delete Deliverables")
    print("   [2] List All Files")
    print("   [3] Exit Program")
    print()


def clr_scr():
    # Check if the platform is Windows or linux
    # If Platform is Windows then run command os.system(�cls�) else os.system(�clear�)
    if platform.system().lower() == "windows":
        runcmd = 'cls'
    else:
        runcmd = 'clear'

    os.system(runcmd)
# ----- end functions -----


menu()
option = int(input("  Choose an option: "))

while option != 0:
    if option == 1:
        # do option 1 stuff
        for file_name in os.listdir(path):
            file = path + file_name
            if os.path.isfile(file) and file_name.startswith('deliverable_') and file_name.endswith('.jpg'):
                try:
                    os.remove(file)
                except FileNotFoundError:
                    print("file not found")
                    print()

                except PermissionError:
                    print("You do not have permission to delete this file")
                    print()

                except OSError:
                    print("Error, cannot delete file.")
                    print()

                else:
                    print()
                    print(" Deliverable has been successfully deleted!")
                    print()
                    sleep(2)

    elif option == 2:
        clr_scr()
        print()
        print(" Files and directories in '", path, "':")
        print()
        print()
        for file in dir_list:
            print(" ", file)
        print()
        print()
        input(" Press Enter to continue...")

    elif option == 3:
        clr_scr()
        print()
        print("     DELIVERABLE DELETER")
        print("  --------------------------")
        print()
        print(gb1)
        sleep(1)
        clr_scr()
        sys.exit()

    else:
        print("invalid option.")
        sleep(2)
        clr_scr()

    clr_scr()
    menu()
    option = int(input("  Enter an option: "))


