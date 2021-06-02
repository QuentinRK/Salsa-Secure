from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
import json
import os
import shutil
import stdiomask
from base64 import b64decode, b64encode


class encryptor:
    def __init__(self):
        self.mode = AES.MODE_CBC
        self.salt = get_random_bytes(32)
        self.filename = None
        self.key = None

    def encrypt(self, key, file):
        key = self.passwordToKey('123456')
        output_file = 'encrypted/' + file  # + (file.strip('.zip'))
        newfile = self.convertToBytes(file)
        cipher = AES.new(key, AES.MODE_CBC)
        ciphered_data = cipher.encrypt(pad(newfile, AES.block_size))
        base = os.getcwd()
        encrypted_path = base + '/encrypted'

        if not os.path.exists(encrypted_path):
            os.makedirs(os.path.join(base, 'encrypted'))

        with open(output_file, 'wb') as f:
            f.write(self.salt)
            f.write(cipher.iv)
            f.write(ciphered_data)
        os.remove(file)

    def convertToBytes(self, file):
        with open(file, 'rb') as f:
            items = f.read()
        return items

    def decrypt(self, key, file):
        file_in = open(file, 'rb')
        salt = file_in.read(32)
        iv = file_in.read(16)
        ciphered_data = file_in.read()
        file_in.close()
        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size)
        name = file.strip('.bin').lstrip('encrypted')

        with open((os.getcwd() + f'{name}.zip'), 'wb') as f:
            f.write(original_data)

        shutil.rmtree('encrypted')
        print('decryption complete')

    def retrieve_salt(self, file):
        with open(file, 'rb') as f:
            salt = f.read(32)

        self.salt = salt

    def passwordToKey(self, password):
        key = PBKDF2(password, self.salt, dkLen=32)
        return key

    # def main(self):
    #     choice = input('would you like to (e)ncrypt or (d)ecrypt: ')

    #     if choice == 'e':
    #         file = input('what is the file name: ')
    #         password = stdiomask.getpass()
    #         self.encrypt(self.PasswordToKey(password), file)
    #         print('encryption complete')
    #     elif choice == 'd':
    #         file = input('what is the file name: ')
    #         password = stdiomask.getpass()
    #         self.retrieve_salt(file)
    #         self.decrypt(self.PasswordToKey(password), file)
    #     else:
    #         print('no option selected')


# e = encryptor()
# e.main()


# # e.decrypt('encrypted/encrypted.bin')


if __name__ == "__main__":
    encryptor()
