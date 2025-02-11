"""main"""

from processor import App
from DB_handler import DBHandler
from time import sleep


with DBHandler("database.db") as database:
    app = App(database)
    
    print("\nWelcome to PASSWORD MANAGER (by: github.com/hamidgh01)\n")
    while True:
        sleep(0.5)
        print("1. Login")
        print("2. Register (if you don't have an account)")
        print("3. Exit")
        option = input("\n>>> ")
        
        if option == "1":
            sleep(0.5)
            if result := app.login():
                sleep(0.5)
                app.start_app()
                continue
        elif option == "2":
            sleep(0.5)
            result = app.register_user()
            if result is None:
                sleep(0.5)
                print("exiting process...\n")
            elif result:
                sleep(0.5)
                print("\nyour registration was done successfully.\n"
                      "now you can login to the app!\n")
                sleep(0.5)
            else:
                sleep(0.5)
                print("your registration was failed...\ntry again please!\n")
            continue
        elif option == "3":
            sleep(0.5)
            break
        else:
            sleep(0.5)
            print("Invalid choice! Please choose a correct option (1 or 2 or 3).\n")
    
    print("have a good day!!! :)))\n")
