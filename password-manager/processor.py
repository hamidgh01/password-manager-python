"""organizer and manager of the app (password-manager)"""

import secrets
import string
from configparser import ConfigParser
from cryptography.fernet import Fernet
from DB_handler import DBHandler


def get_encryption_key():
    """
    returns the encryption_key (saved in confs.ini) or
    generates that using 'Fernet.generate_key()' and then returns.
    """
    
    config_parser = ConfigParser()
    try:
        # except the first execution, this block will be executed all the times.
        config_parser.read_file(open("confs.ini"))
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
        with open("confs.ini", "w") as conf_file:
            config_parser.write(conf_file)
        return encryption_key


class App:
    """main engine"""
    
    def __init__(self):
        self.database = DBHandler("database.db")
    
    def login_required(self, method):
        """login required decorator"""
        pass
    
    def register_user(self):
        """register user"""
        pass
    
    @login_required
    def login(self):
        """login"""
        pass
    
    @login_required
    def change_password(self):
        """change password"""
        pass
    
    @login_required
    def add_entity(self):
        """add new entity"""
        pass
    
    @login_required
    def show_entities(self):
        """show entities"""
        pass
    
    @login_required
    def update_entity(self):
        """update entity"""
        pass
    
    @login_required
    def delete_entity(self):
        """delete entity"""
        pass
