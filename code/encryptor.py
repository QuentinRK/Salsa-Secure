from Crypto.Cipher import AES, Salsa20
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA3_256
import json
import os
import shutil
import stdiomask
from base64 import b64decode, b64encode


"""
User input and the alterations of threading settings are needed

"""

class encryptor:
    def __init__(self):
        self.mode = AES.MODE_CBC
        self.salt = get_random_bytes(32)
        self.filename = None

    # TODO: User input needs to generate a key 
    def encrypt(self, key, file):
        file_name = file.split("/")[-1].strip("tar")
        file_name = file_name[:-1]
        newfile = file_name + " binary.tar"

        old_file = open(file, "rb")
        new_file = open(newfile, 'wb')
            
        items = old_file.read()
        
        key = get_random_bytes(32)
        cipher = Salsa20.new(key=key)
        msg = cipher.nonce + cipher.encrypt(items)

        new_file.write(key)
        new_file.write(msg)

        old_file.close()
        new_file.close()
        os.remove(file)

    
    # TODO: Need to create a function for password validation 
    def decrypt(self, file):
        newfile = file.split()
        newfile = "".join(newfile[:-1]) + ".tar"

        file = open(file, 'rb')
        new_file = open(newfile, 'wb')

        key = file.read(32)
        msg_nonce = file.read(8)
        msg = file.read()

        cipher = Salsa20.new(key=key, nonce=msg_nonce)
        content = cipher.decrypt(msg)
        new_file.write(content)

        file.close()
        new_file.close()
        os.remove(file)
        
if __name__ == "__main__":
    encryptor()