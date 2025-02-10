"""gen"""

import secrets
import string
from configparser import ConfigParser
from cryptography.fernet import Fernet


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
