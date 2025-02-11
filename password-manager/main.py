"""main"""

from processor import App
from DB_handler import DBHandler
from time import sleep


with DBHandler(":memory:") as database:
    app = App(database)
    
    print("PASSWORD MANAGER")
    while True:
        sleep(0.5)
        print("1. Login")
        print("2. Register (if you don't have an account)")
        print("3. Exit")
        option = input("\n>>> ")
        
        if option == "1":
            if result := app.login():
                sleep(0.5)
                app.start_app()
                continue
        elif option == "2":
            if result := app.register_user():
                sleep(0.5)
                print("your registration was done successfully.\n"
                      "now you can login to the app!\n")
                continue
        elif option == "3":
            sleep(0.5)
            break
        else:
            sleep(0.5)
            print("Invalid choice! Please choose a correct option (1 or 2 or 3).\n")
    
    print("---*---*---*---*" * 4)
    print("have a good day! :)))")
