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
The encryptor is responsible for the running the ciphers during
encryption and decryption

"""
class encryptor:

    def encrypt(self, file, key=None):

        # strip the file extension of the string
        strip_file_extension = file.split("/")[-1].strip("tar")

        # From the list retrieve the file name 
        file_name = strip_file_extension[:-1]

        # Form a new name for the encrypted tar file 
        encrypted_file = file_name + " (encrypted).tar"

        # Open a new file and the file that needs to be encrypted 
        old_file = open(file, "rb")
        new_file = open(encrypted_file, 'wb')

        # items stores the contents of the old file
        items = old_file.read()

        if key:

            # create a second hash using SHA256 for the key 
            new_hash = SHA256.new(key)
            key = new_hash.digest()

            # Salsa20 is implemented as the cipher 
            cipher = Salsa20.new(key=key)
            msg = cipher.nonce + cipher.encrypt(items)

            # pad the encrypted file with salt 
            new_file.write(get_random_bytes(32))

            # write the key to the file 
            new_file.write(key)

            # write the encrypted content to the new file
            new_file.write(msg)
            
            # close all files and remove the old file 
            old_file.close()
            new_file.close()
            os.remove(file)
        else:
            print("error no key")

    def decrypt(self, file, key=None):

        # split the current directory to remove encrypted string 
        split_directory = file.split()

        # form a new name for the decrypted file 
        decrypted_file = "".join(split_directory[:-1]) + ".tar"

        # the users key is hashed  
        new_hash = SHA256.new(key)
        input_key = new_hash.digest()

        old_file = open(file, 'rb')
        new_file = open(decrypted_file, 'wb')

        # extract the salt and orignal key from the encrypted file 
        salt = old_file.read(32)
        key = old_file.read(32)

        # validate the original key with the users input 
        if key == input_key:

            # Salsa20 decryption 
            msg_nonce = old_file.read(8)
            msg = old_file.read()
            cipher = Salsa20.new(key=key, nonce=msg_nonce)
            content = cipher.decrypt(msg)
            new_file.write(content)

            # close all files and remove encrypted file 
            old_file.close()
            new_file.close()
            os.remove(file)
            return True

        # if key is invalid close all files and remove the new file 
        else:
            old_file.close()
            new_file.close()
            os.remove(decrypted_file)
            return False



if __name__ == "__main__":
    encryptor()