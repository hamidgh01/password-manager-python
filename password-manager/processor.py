"""organizer and manager of the app (password-manager)"""

from configparser import ConfigParser
from cryptography.fernet import Fernet
import secrets
import string
from time import sleep
from getpass import getpass
from DB_handler import DBHandler


def get_encryption_key():
    """
    returns the encryption_key (saved in _confs.ini) or
    generates that using 'Fernet.generate_key()' and then returns.
    """
    
    config_parser = ConfigParser()
    try:
        # except the first execution, this block will be executed all the times.
        config_parser.read_file(open("_confs.ini"))
        if config_parser.has_option("configurations", "encryption_key"):
            encryption_key = config_parser["configurations"]["encryption_key"]
            return encryption_key.encode()
        else:
            raise FileNotFoundError
    except FileNotFoundError:
        # only in the first execution, this block will be executed.
        encryption_key = Fernet.generate_key()
        enc_key = encryption_key.decode()
        config_parser["configurations"] = {"encryption_key": enc_key}
        with open("_confs.ini", "w") as conf_file:
            config_parser.write(conf_file)
        return encryption_key


class App:
    """main engine"""
    
    def __init__(self, database: DBHandler):
        self.database = database
        self.encryption_key = get_encryption_key()
        self.cipher_suite = Fernet(self.encryption_key)
    
    def register_user(self):
        """register user"""
        print(
            "NOTE:\n4 <= username <= 32 characters\n"
            "8 <= password <= 32 characters\n"
            "*** space ' ' isn't valid for both\n"
        )
        
        def is_valid(data: str, for_: str):
            """validation for username and password"""
            if " " in data:
                print("space ' ' isn't valid...\ntry again please!\n")
                sleep(1)
                return False
            at_least = 4 if for_ == "username" else 8
            if len(data) < at_least or len(data) > 32:
                print(f"ERROR: {at_least} <= {for_} <= 32 characters\n"
                      f"try again please!\n")
                sleep(1)
                return False
            return True
        
        def exit_if_q(input_: str) -> bool:
            """enter 'q' to exit this process"""
            return True if input_.lower() == "q" else False
        
        print("(enter 'q' to exit this process)")
        username = input("username: ")
        if exit_if_q(username):
            return None
        if not is_valid(username, for_="username"):
            return self.register_user()
        
        password = getpass("password: ")
        if exit_if_q(password):
            return None
        if not is_valid(password, for_="password"):
            return self.register_user()
        if password == username:
            print("username and password can't be similar...\n"
                  "try again please!\n")
            sleep(1)
            return self.register_user()
        
        confirm_password = getpass("confirm password: ")
        if exit_if_q(confirm_password):
            return None
        if password == confirm_password:
            password = password.encode()
            encrypted_password = self.cipher_suite.encrypt(password)
            return self.database.register_user(
                username=username,
                password=encrypted_password.decode()
            )
        else:
            sleep(0.5)
            print(f"\n* passwords aren't similar... please try again!\n")
            sleep(1)
            self.register_user()
    
    def login(self):
        """login"""
        pass
    
    def change_password(self):
        """change password"""
        pass
    
    def add_entity(self):
        """add new entity"""
        pass
    
    def show_entities(self):
        """show entities"""
        pass
    
    def update_entity(self):
        """update entity"""
        pass
    
    def delete_entity(self):
        """delete entity"""
        pass
    
    @staticmethod
    def automatically_generate_password(length: int = 12) -> str:
        """automatically generate password"""
        characters = string.ascii_letters + string.digits + "!@#$%&*_-+=."
        password = "".join(secrets.choice(characters) for _ in range(length))
        return password
    
    def start_app(self):
        """app"""
        print("PASSWORD MANAGER")
        while True:
            print("1. Show services and passwords")
            print("2. Add a service & password")
            print("3. Delete a service & password")
            print("4. Update a service & password")
            print("-----------------------------------")
            print("a. Change your account's password")
            print("q. Exit Account (Logout)")
            # print("Delete-Account")
            
            choice = input("\n>>> ")
            
            if choice == '1':
                print("change_password()")
            elif choice == '2':
                print("you should fill 3 inputs: service/website - username - password")
                print("add_password()")
            elif choice == '3':
                print("view_passwords()")
            elif choice == '4':
                print("delete_password()")
            elif choice.lower() == "a":
                self.change_password()
            elif choice.lower() == 'q':
                break
            else:
                print("Invalid choice! Please select again.\n")
                sleep(1)
