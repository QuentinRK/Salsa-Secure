from Crypto.Cipher import AES, Salsa20
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256
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
    def encrypt(self, file, key=None):


        file_name = file.split("/")[-1].strip("tar")
        file_name = file_name[:-1]
        newfile = file_name + " (encrypted).tar"

        old_file = open(file, "rb")
        new_file = open(newfile, 'wb')
        items = old_file.read()
    
        if key:
            new_hash = SHA256.new(key)
            key = new_hash.digest()
            cipher = Salsa20.new(key=key)
            msg = cipher.nonce + cipher.encrypt(items)

            new_file.write(key)
            new_file.write(msg)

            old_file.close()
            new_file.close()
            os.remove(file)
        else:
            print("error no key")

    
    # TODO: Need to create a function for password validation 
    def decrypt(self, file, key=None):
        newfile = file.split()
        newfile = "".join(newfile[:-1]) + ".tar"
        new_hash = SHA256.new(key)
        input_key = new_hash.digest()

        old_file = open(file, 'rb')
        new_file = open(newfile, 'wb')
        key = old_file.read(32)

        if key == input_key:
            msg_nonce = old_file.read(8)
            msg = old_file.read()
            cipher = Salsa20.new(key=key, nonce=msg_nonce)
            content = cipher.decrypt(msg)
            new_file.write(content)
            old_file.close()
            new_file.close()
            os.remove(file)
            return True

        else:
            old_file.close()
            new_file.close()
            os.remove(newfile)
            return False



if __name__ == "__main__":
    encryptor()