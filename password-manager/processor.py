"""gen"""

import secrets
import string
from configparser import ConfigParser
from cryptography.fernet import Fernet


config_parser = ConfigParser()
config_parser.read("confs.ini")
encryption_key = config_parser["configurations"]["encryption_key"].encode()


# with orm.xxxx?
#     codes
#     .
#     .
#     .
